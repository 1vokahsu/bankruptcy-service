

document.addEventListener('DOMContentLoaded', function () {
  var bankruptcyElement = document.querySelector('.bankruptcy-tooltip-collapsible');
  var insolvencyElement = document.querySelector('.insolvency-tooltip-collapsible');

  if (bankruptcyElement) {
    bankruptcyElement.addEventListener('click', function () {
      var bankruptcyTooltipText = document.getElementById('bankruptcy-tooltip-collapsible-text');
      if (bankruptcyTooltipText) {
        bankruptcyTooltipText.style.display = (bankruptcyTooltipText.style.display === 'none') ? 'block' : 'none';
        bankruptcyTooltipText.style.backgroundColor = '#ffe5f5';
        bankruptcyTooltipText.style.borderRadius = '8px';
        bankruptcyTooltipText.style.border = '1px solid #ffe5f5';
      }
    });
  }

  if (insolvencyElement) {
    insolvencyElement.addEventListener('click', function () {
      var insolvencyTooltipText = document.getElementById('insolvency-tooltip-collapsible-text');
      if (insolvencyTooltipText) {
        insolvencyTooltipText.style.display = (insolvencyTooltipText.style.display === 'none') ? 'block' : 'none';
        insolvencyTooltipText.style.backgroundColor = '#e5ffef';
        insolvencyTooltipText.style.textAlign = 'center';
        insolvencyTooltipText.style.border = '1px solid #e5ffef';
        insolvencyTooltipText.style.borderRadius = '8px';
      }
    });
  }
});




//функция отвечает за отображение подсказок по "неплатежеспособности", "недостаточности имущества" и "критериев" на
//странице теста (test.html)
document.addEventListener('DOMContentLoaded', function () {
	var tooltips = document.querySelectorAll(
		'.bankruptcy-tooltip, .insolvency-tooltip, .criteria-tooltip'
	)
    var activeTooltipText = null
    var activeTooltip = null
	tooltips.forEach(function (tooltip) {
		tooltip.addEventListener('click', function () {
			// Отображаем подсказку, соответствующую кликнутому элементу
			var tooltipTextId =
				tooltip.getAttribute('class').split('-')[0] + '-tooltip-text'
			var tooltipText = document.getElementById(tooltipTextId)
            //При клике на подсказку предыдущая подсказка убирается
            if (activeTooltipText && tooltipText != activeTooltipText) {
            activeTooltipText.style.display = 'none'
            tooltip.style.backgroundColor = '#fff'
            activeTooltip.style.backgroundColor = '#fff'
            activeTooltipText = null
            activeTooltip = null
            }

			// Открывается при первом клике и закрывается при втором, а также слово и подсказка окрашиваются в зеленый цвет
			if (tooltipText.style.display === 'block') {
				tooltipText.style.display = 'none'
				tooltip.style.backgroundColor = '#fff'
			} else {
				tooltipText.style.display = 'block'
				tooltip.style.backgroundColor = '#e5ffef'
				tooltip.style.borderRadius = '8px'
				activeTooltipText = tooltipText
				activeTooltip = tooltip
			}
			tooltipText.style.backgroundColor = '#e5ffef'
			tooltipText.style.borderRadius = '8px'
			console.log(activeTooltipText)
		    console.log(activeTooltip)
		    console.log(tooltipText.style.display)
		    console.log(tooltip)

		})
	})
})


document.addEventListener('DOMContentLoaded', function () {
	var collapsibleContainers = document.querySelectorAll('.collapsible-container')
	collapsibleContainers.forEach(function (container) {
		var collapsibleTitle = container.querySelector('.collapsible-title')
		var collapsibleIcon = container.querySelector('.collapsible-icon')
		var content = container.nextElementSibling

		function toggleContent() {
			content.classList.toggle('active')
			if (content.style.display === 'block') {
				content.style.display = 'none'
			} else {
				content.style.display = 'block'
			}
		}

		collapsibleTitle.addEventListener('click', toggleContent)
		collapsibleIcon.addEventListener('click', toggleContent)
	})

	var link = document.querySelector('a[href="#days30"]')
	if (link) {
	link.addEventListener('click', function (event) {
		event.preventDefault()
		var target = document.querySelector('#days30')
		target.scrollIntoView({ behavior: 'smooth' })
		var container = target.closest('.collapsible-container')
		var content = container.nextElementSibling
		content.style.display = 'block'
	})
	}
})


//функция отвечает за подсветку активного названия раздела на навигационном меню
document.addEventListener('DOMContentLoaded', function () {
    var navItems = document.querySelectorAll('.navbar-nav .nav-item');
    var currentPage = window.location.pathname;

    navItems.forEach(function (navItem, index) {
        var link = navItem.querySelector('a');
        if (link.getAttribute('href') === currentPage) {
            navItem.classList.add('active');
        }

        navItem.addEventListener('click', function () {
            navItems.forEach(function (otherNavItem) {
                otherNavItem.classList.remove('active');
            });
            navItem.classList.add('active');
        });
    });

    var logo = document.querySelector('.navbar-brand');
    logo.addEventListener('click', function () {
        navItems.forEach(function (navItem) {
            navItem.classList.remove('active');
        });
        navItems[0].classList.add('active');  // Предполагая, что "Главная" - это первый элемент
    });
});




