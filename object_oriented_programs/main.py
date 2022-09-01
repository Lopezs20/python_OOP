from . import car

toyota = car(2019,"Toyota","New",60000)
hundai = car(2014,"Hundai", "Good",55000)
subaru = car(2013,"subaru", "Fair",45000)
honda = car(2011,"Honda", "Poor",30000)
ford = car(2015,"ford","",78000)
chevy = car(2020, "chevy","Good",85000)
Vehicles = {
    'Japanese made' : [toyota, hundai, subaru, honda],
    'American made' : [ford, chevy]
}

print(Vehicles.get('Japanese made'))
