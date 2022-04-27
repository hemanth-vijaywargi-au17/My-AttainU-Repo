var findBtn = document.getElementById("findBtn")
var googleBtn = document.getElementById("googleBtn")
var coordinatesBox = document.getElementById("coordinates")
var locationBox = document.getElementById("locationBox")

function allowed(location){
    var latitude = location.coords.latitude
    var longitude = location.coords.longitude
    coordinatesBox.innerText = `Latitude is ${latitude}°, longitude is ${longitude}°.`
    googleBtn.style.visibility = "visible"
    googleBtn.setAttribute("href",`http://www.google.com/maps/search/?api=1&query=${latitude}%2C${longitude}`)
}

function blocked(){
    coordinatesBox.innerText = "Please Allow the website to Access you Location."
}

findBtn.addEventListener("click",function(){
    window.navigator.geolocation.getCurrentPosition(allowed,blocked)
})