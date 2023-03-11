const form = document.querySelector("form");
const locationInput = document.querySelector("#location-input");
const sortByInput = document.querySelector("#sort-by");
const mapContainer = document.querySelector("#map");
const chargingStationsContainer = document.querySelector("#charging-stations");

form.addEventListener("submit", event => {
  event.preventDefault();
  const location = locationInput.value;
  const sortBy = sortByInput.value;

  fetch(`https://api.openchargemap.io/v3/poi/?output=json&countrycode=US&maxresults=20&latitude=37.7749&longitude=-122.4194&distance=50&sortby=${sortBy}`)
    .then(response => response.json())
    .then(data => {
      const chargingStations = data.map(chargingStation => {
        return `
          <div class="charging-station">
            <h2>${chargingStation.AddressInfo.Title}</h2>
            <p>Address: ${chargingStation.AddressInfo.AddressLine1}, ${chargingStation.AddressInfo.City}, ${chargingStation.AddressInfo.StateOrProvince}</p>
            <p>Charging Ports: ${chargingStation.NumberOfPoints}</p>
            <p>Charging Speed: ${chargingStation.UsageType.Title}</p>
          </div>
        `;
      });

      chargingStationsContainer.innerHTML = chargingStations.join("");
    });

  const map = new google.maps.Map(mapContainer, {
    zoom: 10,
    center: { lat: 37.7749, lng: -122.4194 }
  });

  data.forEach(chargingStation => {
    const marker = new google.maps.Marker({
      position: {
        lat: chargingStation.AddressInfo.Latitude,
        lng: chargingStation.AddressInfo.Longitude
      },
      map: map,
      title: chargingStation.AddressInfo.Title
    });
  });
});

function sortByDistance(a, b) {
  return a.AddressInfo.Distance - b.AddressInfo.Distance;
}

function sortByRating(a, b) {
  return b.UserComments[0].Rating - a.UserComments[0].Rating;
}





// const form = document.querySelector("form");
// const locationInput = document.querySelector("#location-input");
// const mapContainer = document.querySelector("#map");
// const chargingStationsContainer = document.querySelector("#charging-stations");

// form.addEventListener("submit", event => {
//   event.preventDefault();
//   const location = locationInput.value;

//   // Use a placeholder API to get the charging stations near the given location
//   const url = `https://api.openchargemap.io/v3/poi/?output=json&latitude=37.7749&longitude=-122.4194&distance=25&distanceunit=Miles`;

//   fetch(url)
//     .then(response => response.json())
//     .then(data => {
//       const chargingStations = data.map(chargingStation => {
//         return `
//           <div class="charging-station">
//             <h2>${chargingStation.AddressInfo.Title}</h2>
//             <p>Address: ${chargingStation.AddressInfo.AddressLine1}</p>
//             ...
//             <p>Charging Ports: ${chargingStation.NumberOfPoints}</p>
//             <p>Charging Speed: ${chargingStation.UsageType.Title}</p>
//           </div>
//         `;
//       });

//       chargingStationsContainer.innerHTML = chargingStations.join("");
//     });

//   const map = new google.maps.Map(mapContainer, {
//     zoom: 10,
//     center: { lat: 53.911994534142195, lng: 27.59481529279003 }
//   });

//   data.forEach(chargingStation => {
//     const marker = new google.maps.Marker({
//       position: {
//         lat: chargingStation.AddressInfo.Latitude,
//         lng: chargingStation.AddressInfo.Longitude
//       },
//       map: map,
//       title: chargingStation.AddressInfo.Title
//     });
//   });
// });
