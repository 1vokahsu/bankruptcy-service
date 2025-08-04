
# Bankruptcy-service <img src="app/static/img/logo.png" width="100">

A service for determining the possibility of bankruptcy of an individual, taking into account the risks
and consequences.

## Technology stack

- Backend 
![Python](https://img.shields.io/badge/-Python-333?style=for-the-badge&logo=Python) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
- Frontend
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![JS](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E) ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
- DB
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
- Developing, shipping, and running
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
- Web serving, reverse proxying, caching, load balancing
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)


## Project Structure

```tree
.
├── README.md
├── app
│   ├── Dockerfile
│   ├── config.py
│   ├── main.py
│   ├── requirements.txt
│   ├── static
│   │   ├── css
│   │   │   └── main.css
│   │   └── js
│   │       └── main.js
│   └── templates
│       ├── account.html
│       ├── base.html
│       ├── history.html
│       ├── img
│       │   ├── calendar.png
│       │   └── calendar.svg
│       ├── index.html
│       ├── login.html
│       ├── register.html
│       ├── results.html
│       └── test.html
├── docker-compose.dev.yml
├── nginx
│   ├── Dockerfile
│   └── nginx.conf
└── pg_db
```

## Usage
- Download `docker` and `docker-compose`
- Run app or system daemon `docker`
- Go to the folder `/project_kplus`
- If you have never created images or lifted containers yet, run these commands in the terminal, located in the `/project_kplus` folder
  ```bash
  docker-compose -f docker-compose.dev.yml build
  docker-compose -f docker-compose.dev.yml up
  ```
- After doing the above in the new terminal, do this
  ```bash
  docker exec bankruptcy_app flask --app main create_db
  ```
- To go to the site in the browser, enter `http://localhost:80` or `http://127.0.0.1:80`
- If you changed/added/deleted something, run these commands in the terminal, located in the `/project_kplus` folder
  ```bash
  docker-compose -f docker-compose.dev.yml up --build
  ```
- If you want to stop everything, press `Ctrl+C`



## Contributing

Contributions to the Project_kplus are welcome! Whether it's feature requests, bug reports, or code contributions, please feel free to make a pull request or open an issue in the repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Project participants
[![GitHub](https://img.shields.io/badge/-galyeonh-333?style=for-the-badge&logo=GitHub&logoColor=fff)](https://gitlab.com/galyeonh)
