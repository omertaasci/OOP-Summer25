class Country():
    def __init__(self, name, population, biggest_cities):
        self.name = name
        self.population = population
        self.biggest_cities = biggest_cities


Poland = Country('Poland', 38000000, ['Warszawa', 'Krakow', 'Gdansk'])

print(f'Name {Poland.name} Population {Poland.population} Biggest cities {Poland.biggest_cities}')