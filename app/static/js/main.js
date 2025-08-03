//
//document.addEventListener('DOMContentLoaded', function() {
//  // Находим элементы, которые должны показывать подсказки
//  var bankruptcyElement = document.querySelector('.bankruptcy-tooltip');
//  var insolvencyElement = document.querySelector('.insolvency-tooltip');
//  var criteriaElement = document.querySelector('.criteria-tooltip');
//
//  // Обработчик события 'click' для "неплатежеспособности"
//  bankruptcyElement.addEventListener('click', function() {
//    var bankruptcyTooltipText = document.getElementById('bankruptcy-tooltip-text');
//    bankruptcyTooltipText.style.display = bankruptcyTooltipText.style.display === 'none' ? 'block' : 'none';
//  });
//
//  // Обработчик события 'click' для "недостаточности имущества"
//  insolvencyElement.addEventListener('click', function() {
//    var insolvencyTooltipText = document.getElementById('insolvency-tooltip-text');
//    insolvencyTooltipText.style.display = insolvencyTooltipText.style.display === 'none' ? 'block' : 'none';
//  });
//
//  // Обработчик события 'click' для "критериев"
//  criteriaElement.addEventListener('click', function() {
//    var criteriaTooltipText = document.getElementById('criteria-tooltip-text');
//    criteriaTooltipText.style.display = criteriaTooltipText.style.display === 'none' ? 'block' : 'none';
//  });
//});

document.addEventListener('DOMContentLoaded', function () {
	var tooltips = document.querySelectorAll(
		'.bankruptcy-tooltip, .insolvency-tooltip, .criteria-tooltip'
	)

	tooltips.forEach(function (tooltip) {
		tooltip.addEventListener('click', function () {
			// Сначала скрываем все подсказки
			document.querySelectorAll('.tooltip-text').forEach(function (el) {
				el.style.display = 'none'
			})

			// Затем отображаем подсказку, соответствующую кликнутому элементу
			var tooltipTextId =
				tooltip.getAttribute('class').split('-')[0] + '-tooltip-text'
			var tooltipText = document.getElementById(tooltipTextId)
			tooltipText.style.display = 'block'
		})
	})
})
