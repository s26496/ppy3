import random

cities = ["Warszawa", "Kraków", "Wrocław", "Łódź", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Białystok"]
num_of_cities_to_visit = random.randint(1,10)
trip = random.sample(cities, num_of_cities_to_visit)

print("Plan wycieczki:")
for city in trip:
    print("Miasto "+str(trip.index(city)+1)+": "+city)