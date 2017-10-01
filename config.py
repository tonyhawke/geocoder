
server = {
    "name":"localhost",
    "port":8000
}

geocoder = {
    "primary":"here",
    "secondary":"googlemaps"
}

provider = {
    "googlemaps" : {
        "key":"***",
        "url":"https://maps.googleapis.com/maps/api/geocode/json?"
    },
    "here" : {
        "appId":"***",
        "appCode":"***",
        "url":"httttps://geocoder.cit.api.here.com/6.2/geocode.json?"
    }
}
