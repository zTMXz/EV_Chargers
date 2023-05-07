function init() {
    // Получаем координаты пользователя
    navigator.geolocation.getCurrentPosition(function(position) {
        var userLat = position.coords.latitude;
        var userLng = position.coords.longitude;

        // Создаем карту с координатами пользователя
        var myMap = new ymaps.Map('map', {
            center: [userLat, userLng],
            zoom: 15,
            controls: []
        });

        // Создадим экземпляр элемента управления «поиск по карте»
        // с установленной опцией провайдера данных для поиска по организациям.
        var searchControl = new ymaps.control.SearchControl({
            options: {
                provider: 'yandex#search',
                noPopup: true
            }
        });

        myMap.controls.add(searchControl);

        // Программно выполним поиск определённых кафе в текущей
        // прямоугольной области карты.
        searchControl.search('Электрозаправка');

        // Подписывается на событие получения результатов поиска с сервера.
        searchControl.events.add('load', function (e) {
            var count = searchControl.getResultsCount();
            // console.log("Количество найденных результатов поиска: " + count);
        })
    });
}

ymaps.ready(init);
