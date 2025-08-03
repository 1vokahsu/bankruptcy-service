from flask import Flask, render_template, url_for, request, redirect, Blueprint
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import JSONB
from config import config
from flask import session
import hashlib
import json
import os

app = Flask(__name__, )
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# bp = Blueprint('commands', __name__)

# app.register_blueprint(bp)

app.secret_key = os.urandom(24)


class Users(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)
    form_personal_data = db.Column(JSONB)
    form = db.relationship(
        'UsersData', backref=db.backref('user', lazy=True))
    salt = db.Column(db.String(32), nullable=False)

    def __repr__(self) -> str:
        return '<Article %r>' % self.id


class UsersData(db.Model):

    __tablename__ = "users_data"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    form = db.Column(JSONB)
    result = db.Column(db.Text, nullable=True)
    time_create = db.Column(db.DateTime(timezone=True),
                            server_default=func.now())

    def __repr__(self) -> str:
        return '<Article %r>' % self.id


with app.app_context():
    # db.drop_all()
    db.create_all()
    
    
@app.cli.command("create_db")
def create_db():
    with app.app_context():
        # db.drop_all()
        db.create_all()


# Функция, возвращающая рез-т исходя из логики
def get_result(form: dict) -> dict:
    result = {
        0: "",
        1: -1
    }
    if ((form["Сумма задолженности"] == "От 25 до 500 тысяч рублей" or form["Сумма задолженности"] == "Менее 25 тысяч рублей") and form["Удовлетворяет"] == "Да") or (
        (form["Сумма задолженности"] == "Менее 25 тысяч рублей" or form["Сумма задолженности"] == "Более 1 млн рублей"
         or (form["Сумма задолженности"] == "От 500 тысяч до 1 млн рублей" and form["Соответствуете"] == "Нет"))
        and (form["Удовлетворяет"] == "Нет" and form["Вы отвечаете"] == "Да")
    ):
        result[0] = "Вы ВПРАВЕ обратиться только в СУД с заявлением о признании банкротом (при доказательстве НЕПЛАТЕЖЕСПОСОБНОСТИ и НЕДОСТАТОЧНОСТИ имущества)"
        result[1] = 0
        return result
    elif ((form["Сумма задолженности"] == "От 25 до 500 тысяч рублей" or form["Сумма задолженности"] == "Более 1 млн рублей"
           or (form["Сумма задолженности"] == "От 500 тысяч до 1 млн рублей"
               and form["Соответствуете"] == "Нет"))
          and form["Удовлетворяет"] == "Нет" and form["Вы отвечаете"] == "Нет"
          ):
        result[
            0] = "Вы можете подать заявление в суд, но, скорее всего, Вам откажут в удовлетворении требований.\nВы можете претендовать на банкротство в судебном порядке только при доказательстве НЕПЛАТЕЖЕСПОСОБНОСТИ и НЕДОСТАТОЧНОСТИ имущ-ва.\nВы имеет право обратиться в МФЦ при соблюдении УСЛОВИЙ (ст. 223.2)"
        result[1] = 1
        return result
    elif (form["Сумма задолженности"] == "От 25 до 500 тысяч рублей" or (
            form["Сумма задолженности"] == "От 500 тысяч до 1 млн рублей" and form["Соответствуете"] == "Да")
          and (form["Удовлетворяет"] == "Нет" and form["Вы отвечаете"] == "Да")
          ):
        result[0] = "Вы имеете ПРАВО обратиться либо в СУД, либо в МФЦ, по Вашему усмотрению (для МФЦ - дописать дополнительные для этого условия иЗ Ст. 223.2)"
        result[1] = 2
        return result
    elif (form["Сумма задолженности"] == "Менее 25 тысяч рублей" or form["Сумма задолженности"] == "Более 1 млн рублей"
          and (form["Удовлетворяет"] == "Нет" and form["Вы отвечаете"] == "Нет")
          ):
        result[0] = "Вы можете подать заявление в СУД, но, скорее всего, Вам откажут в удовлетворении требований.\nВы можете претендовать на банкротство в судебном порядке только при доказательстве НЕПЛАТЕЖЕСПОСОБНОСТИ и НЕДОСТАТОЧНОСТИ имущества"
        result[1] = 3
        return result
    elif (form["Сумма задолженности"] == "Более 1 млн рублей"
          or (form["Сумма задолженности"] == "От 500 тысяч до 1 млн рублей")
          and (form["Удовлетворяет"] == "Да")
          ):
        result[0] = "Вы ОБЯЗАНЫ обратиться в СУД с заявлением о признании банкротом.\nУ Вас есть на это 30 дней"
        result[1] = 4
        return result


@app.route("/", methods=["GET", "POST"])
def get_index():
    return render_template("index.html")


@app.route("/test", methods=["GET", "POST"])
def vote():
    if request.method == "POST":
        qw1 = request.form.get("qw1")
        qw2 = request.form.get("qw2")
        qw3 = request.form.get("qw3")
        qw4 = request.form.get("qw4")

        form = {
            "Сумма задолженности": qw1,
            "Удовлетворяет": qw2,
            "Вы отвечаете": qw3,
            "Соответствуете": qw4
        }
        print(form)
        result = get_result(form=form)
        print(result)
        if 'email' in session:
            try:
                user = Users.query.filter_by(email=session['email']).first()
                user_data = UsersData(user_id=user.id, form=json.dumps(
                    form, ensure_ascii=False), result=result[0])
                db.session.add(user_data)
                db.session.commit()
                return render_template("results.html", result=result[1])
            except Exception as ex:
                print(ex)
                return "При заполнении анкеты произошла ошибка"
        return render_template("results.html", result=result[1])

    return render_template("test.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Users.query.filter_by(email=email).first()
        if user:
            hashed_password = hashlib.sha256(
                (password + user.salt).encode()).hexdigest()
            if hashed_password == user.password:
                session['email'] = email
                return redirect(url_for('account'))
        return render_template('login.html', message='Пользователь не найден')
    if 'email' in session:
        return redirect(url_for('account'))
    return render_template('login.html', message='')


@app.route('/account')
def account():
    if 'email' in session:
        user = Users.query.filter_by(email=session['email']).first()
        user_personal_data = json.loads(user.form_personal_data)
        user_personal_data['email'] = user.email
        return render_template('account.html', user_personal_data=user_personal_data)
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']

        user_exists = Users.query.filter_by(email=email).first()
        if user_exists:
            return render_template('register.html', message='Пользователь с такой почтой уже существует!')

        salt = os.urandom(16).hex()
        hashed_password = hashlib.sha256(
            (password + salt).encode()).hexdigest()
        user_data = {
            'name': name,
            'surname': surname,
            'age': age
        }
        user = Users(email=email, password=hashed_password, salt=salt,
                     form_personal_data=json.dumps(user_data, ensure_ascii=False))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login', registered=True))
    return render_template('register.html')


@app.route('/history')
def history():
    if 'email' in session:
        user = Users.query.filter_by(email=session['email']).first()
        user_data = UsersData.query.filter_by(user_id=user.id).order_by(
            UsersData.time_create.desc()).all()

        if not user_data:
            return render_template('history.html', message='Анкета еще не была пройдена.')

        history_data = []
        for data in user_data:
            form_data = json.loads(data.form)
            history_data.append({
                'time': data.time_create.strftime('%d-%m-%Y %H:%M:%S'),
                'questions': {
                    'Сумма задолженности': form_data['Сумма задолженности'],
                    'Удовлетворяет': form_data['Удовлетворяет'],
                    'Вы отвечаете': form_data['Вы отвечаете'],
                    'Соответствуете': form_data['Соответствуете']
                },
                'result': data.result
            })
        return render_template('history.html', user_data=history_data)
    return render_template('history.html', message='Чтобы просматривать историю прохождения анкеты, необходимо войти в систему!')


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('get_index'))


if __name__ == "__main__":
    app.run(debug=True)
# host = "0.0.0.0"