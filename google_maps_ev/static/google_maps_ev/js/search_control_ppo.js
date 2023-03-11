function init() {
    var myMap = new ymaps.Map('map', {
        center: [53.902292, 27.561821],
        zoom: 13,
        controls: []
    });
    
    // Создадим экземпляр элемента управления «поиск по карте»
    // с установленной опцией провайдера данных для поиска по организациям.
    var searchControl = new ymaps.control.SearchControl({
        options: {
            provider: 'yandex#search'
        }
    });
    
    myMap.controls.add(searchControl);
    
    // Программно выполним поиск определённых кафе в текущей
    // прямоугольной области карты.
    searchControl.search('Электрозаправка');

    // Подписывается на событие получения результатов поиска с сервера.
    searchControl.events.add('load', function (e) {
        var count = searchControl.getResultsCount();
        console.log("Количество найденных результатов поиска: " + count);
    })

}



ymaps.ready(init);

