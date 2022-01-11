import requests
import json
import time
# -------------------------
# Jinja2
# -------------------------
from jinja2 import Environment, FileSystemLoader
template_dir = 'Templates/'
env = Environment(loader=FileSystemLoader(template_dir))
starWars_template = env.get_template('StarWars.j2')

# -------------------------
# Headers
# -------------------------
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
}

# -------------------------
# All People
# -------------------------

person_template = env.get_template('person.j2')
people = requests.request("GET", "https://swapi.dev/api/people/", headers=headers)
peopleJSON = people.json()
peopleList = peopleJSON['results']
while peopleJSON['next']:
    people = requests.request("GET", peopleJSON['next'], headers=headers)
    peopleJSON = people.json()
    peopleList.extend(peopleJSON["results"])

# -------------------------
# Single Person
# -------------------------
peoplePersonList = []
peopleHomeworldList = []
peopleFilmList = []
peopleSpeciesList = []
peopleVehicleList = []
peopleStarshipList = []
for person in peopleList:
    singlePerson = requests.request("GET", person['url'], headers=headers)
    singlePersonJSON = singlePerson.json()
    if singlePersonJSON not in peoplePersonList:
        peoplePersonList.append(singlePersonJSON)

# -------------------------
# Homeworld
# -------------------------
    homeworld = requests.request("GET", person['homeworld'], headers=headers)
    homeworldJSON = homeworld.json()
    if homeworldJSON not in peopleHomeworldList:
        peopleHomeworldList.append(homeworldJSON)

# -------------------------
# Films
# -------------------------
    if person['films']:
        for film in person['films']:
            film = requests.request("GET", film, headers=headers)
            filmJSON = film.json()
            if filmJSON not in peopleFilmList:
                peopleFilmList.append(filmJSON)

# -------------------------
# Species
# -------------------------
    if person['species']:
        for species in person['species']:
            species = requests.request("GET", species, headers=headers)
            speciesJSON = species.json()
            if speciesJSON not in peopleSpeciesList:
                peopleSpeciesList.append(speciesJSON)

# -------------------------
# Vehicles
# -------------------------
    if person['vehicles']:
        for vehicle in person['vehicles']:
            vehicle = requests.request("GET", vehicle, headers=headers)
            vehicleJSON = vehicle.json()
            if vehicleJSON not in peopleVehicleList:
                peopleVehicleList.append(vehicleJSON)

# -------------------------
# Starships
# -------------------------
    if person['starships']:
        for starship in person['starships']:
            starship = requests.request("GET", starship, headers=headers)
            starshipJSON = starship.json()
            if starshipJSON not in peopleStarshipList:
                peopleStarshipList.append(starshipJSON)

# -------------------------
# Person Template
# -------------------------

    parsed_all_output = person_template.render(
        singlePerson = singlePersonJSON,
        homeworld = homeworldJSON,
        film = peopleFilmList,
        species = peopleSpeciesList,
        vehicle = peopleVehicleList,
        starship = peopleStarshipList
        )

# -------------------------
# Save Characters File
# -------------------------

    with open(f"StarWars/Characters/{ singlePersonJSON['name'] }.md", "w") as fh:
        fh.write(parsed_all_output)                
        fh.close()

# -------------------------
# All Films
# -------------------------

film_template = env.get_template('film.j2')
film = requests.request("GET", "https://swapi.dev/api/films/", headers=headers)
filmsJSON = film.json()
filmList = filmsJSON['results']

# -------------------------
# Single Film
# -------------------------

filmFilmList = []
filmPersonList = []
filmPlanetList = []
filmStarshipList = []
filmVehicleList = []
filmSpeciesList = []
for film in filmList:
    singleFilm = requests.request("GET", film['url'], headers=headers)
    singleFilmJSON = singleFilm.json()
    if singleFilmJSON not in filmFilmList:
        filmFilmList.append(singleFilmJSON)

# -------------------------
# Characters
# -------------------------
    if film['characters']:
        for person in film['characters']:
            person = requests.request("GET", person, headers=headers)
            personJSON = person.json()
            if personJSON not in filmPersonList:
                filmPersonList.append(personJSON)

# -------------------------
# Planets
# -------------------------
    if film['planets']:
        for planet in film['planets']:
            planet = requests.request("GET", planet, headers=headers)
            planetJSON = planet.json()
            if planetJSON not in filmPlanetList:
                filmPlanetList.append(planetJSON)

# -------------------------
# Starships
# -------------------------
    if film['starships']:
        for starship in film['starships']:
            starship = requests.request("GET", starship, headers=headers)
            starshipJSON = starship.json()
            if starshipJSON not in filmStarshipList:
                filmStarshipList.append(starshipJSON)

# -------------------------
# Vehicles
# -------------------------
    if film['vehicles']:
        for vehicle in film['vehicles']:
            vehicle = requests.request("GET", vehicle, headers=headers)
            vehicleJSON = vehicle.json()
            if vehicleJSON not in filmVehicleList:
                filmVehicleList.append(vehicleJSON)

# -------------------------
# Species
# -------------------------
    if film['species']:
        for species in film['species']:
            species = requests.request("GET", species, headers=headers)
            speciesJSON = species.json()
            if speciesJSON not in filmSpeciesList:
                filmSpeciesList.append(speciesJSON)

# -------------------------
# Film Template
# -------------------------

    parsed_all_output = film_template.render(
        singleFilm = singleFilmJSON,
        filmPersonList = filmPersonList,
        filmPlanetList = filmPlanetList,
        filmStarshipList = filmStarshipList,
        filmVehicleList = filmVehicleList,
        filmSpeciesList = filmSpeciesList,
        )

# -------------------------
# Save Films File
# -------------------------

    with open(f"StarWars/Films/Episode_{ singleFilmJSON['episode_id'] }_{ singleFilmJSON['title'] }.md", "w") as fh:
        fh.write(parsed_all_output)                
        fh.close()

# -------------------------
# All Planets
# -------------------------

planet_template = env.get_template('planet.j2')
planet = requests.request("GET", "https://swapi.dev/api/planets/", headers=headers)
planetJSON = planet.json()
planetList = planetJSON['results']
while planetJSON['next']:
    planet = requests.request("GET", planetJSON['next'], headers=headers)
    planetJSON = planet.json()
    planetList.extend(planetJSON["results"])

# -------------------------
# Single Planet
# -------------------------

planetPlanetList = []
planetPersonList = []
planetFilmList = []
for planet in planetList:
    singlePlanet = requests.request("GET", planet['url'], headers=headers)
    singlePlanetJSON = singlePlanet.json()
    if singlePlanetJSON not in planetPlanetList:
        planetPlanetList.append(singlePlanetJSON)

# -------------------------
# Characters
# -------------------------
    if planet['residents']:
        for person in planet['residents']:
            person = requests.request("GET", person, headers=headers)
            personJSON = person.json()
            if personJSON not in planetPersonList:
                planetPersonList.append(personJSON)

# -------------------------
# Films
# -------------------------
    if planet['films']:
        for film in planet['films']:
            film = requests.request("GET", film, headers=headers)
            filmJSON = film.json()
            if filmJSON not in planetFilmList:
                planetFilmList.append(filmJSON)

# -------------------------
# Planet Template
# -------------------------

    parsed_all_output = planet_template.render(
        singlePlanet = singlePlanetJSON,
        planetPersonList = planetPersonList,
        planetFilmList = planetFilmList
        )

# -------------------------
# Save Planets File
# -------------------------

    with open(f"StarWars/Planets/{ singlePlanetJSON['name'] }.md", "w") as fh:
        fh.write(parsed_all_output)                
        fh.close()

# -------------------------
# All Species
# -------------------------

species_template = env.get_template('species.j2')
species = requests.request("GET", "https://swapi.dev/api/species/", headers=headers)
speciesJSON = species.json()
speciesList = speciesJSON['results']
while speciesJSON['next']:
    species = requests.request("GET", speciesJSON['next'], headers=headers)
    speciesJSON = species.json()
    speciesList.extend(speciesJSON["results"])

# -------------------------
# Single Species
# -------------------------

speciesSpeciesList = []
speciesPersonList = []
speciesFilmList = []
for species in speciesList:
    singleSpecies = requests.request("GET", species['url'], headers=headers)
    singleSpeciesJSON = singleSpecies.json()
    if singleSpeciesJSON not in speciesSpeciesList:
        speciesSpeciesList.append(singleSpeciesJSON)

# -------------------------
# Characters
# -------------------------
    if species['people']:
        for person in species['people']:
            person = requests.request("GET", person, headers=headers)
            personJSON = person.json()
            if personJSON not in speciesPersonList:
                speciesPersonList.append(personJSON)

# -------------------------
# Films
# -------------------------
    if species['films']:
        for film in species['films']:
            film = requests.request("GET", film, headers=headers)
            filmJSON = film.json()
            if filmJSON not in speciesFilmList:
                speciesFilmList.append(filmJSON)

# -------------------------
# Species Template
# -------------------------

    parsed_all_output = species_template.render(
        singleSpecies = singleSpeciesJSON,
        speciesPersonList = speciesPersonList,
        speciesFilmList = speciesFilmList
        )

# -------------------------
# Save Species File
# -------------------------

    with open(f"StarWars/Species/{ singleSpeciesJSON['name'] }.md", "w") as fh:
        fh.write(parsed_all_output)                
        fh.close()

# -------------------------
# All Starships
# -------------------------

starship_template = env.get_template('starships.j2')
starship = requests.request("GET", "https://swapi.dev/api/starships/", headers=headers)
starshipJSON = starship.json()
starshipList = starshipJSON['results']
while starshipJSON['next']:
    starship = requests.request("GET", starshipJSON['next'], headers=headers)
    starshipJSON = starship.json()
    starshipList.extend(starshipJSON["results"])

# -------------------------
# Single Starship
# -------------------------

starshipStarshipList = []
starshipFilmList = []
for starship in starshipList:
    singleStarship = requests.request("GET", starship['url'], headers=headers)
    singleStarshipJSON = singleStarship.json()
    if singleStarshipJSON not in starshipStarshipList:
        starshipStarshipList.append(singleStarshipJSON)

# -------------------------
# Films
# -------------------------
    if starship['films']:
        for film in starship['films']:
            film = requests.request("GET", film, headers=headers)
            filmJSON = film.json()
            if filmJSON not in starshipFilmList:
                starshipFilmList.append(filmJSON)

# -------------------------
# Starship Template
# -------------------------

    parsed_all_output = starship_template.render(
        singleStarship = singleStarshipJSON,
        starshipFilmList = starshipFilmList
        )

# -------------------------
# Save Starship File
# -------------------------

    with open(f"StarWars/Starships/{ singleStarshipJSON['name'] }.md", "w") as fh:
        fh.write(parsed_all_output)                
        fh.close()

# -------------------------
# All Vehicles
# -------------------------

vehicles_template = env.get_template('vehicles.j2')
vehicles = requests.request("GET", "https://swapi.dev/api/vehicles/", headers=headers)
vehiclesJSON = vehicles.json()
vehiclesList = vehiclesJSON['results']
while speciesJSON['next']:
    vehicles = requests.request("GET", vehiclesJSON['next'], headers=headers)
    vehiclesJSON = vehicles.json()
    vehiclesList.extend(vehiclesJSON["results"])

# -------------------------
# Single Species
# -------------------------

vehiclesVehiclesList = []
vehiclesPersonList = []
vehiclesFilmList = []
for vehicles in vehiclesList:
    singleVehicles = requests.request("GET", vehicles['url'], headers=headers)
    singleVehiclesJSON = singleVehicles.json()
    if singleVehiclesJSON not in vehiclesVehiclesList:
        vehiclesVehiclesList.append(singleVehiclesJSON)

# -------------------------
# Characters
# -------------------------
    if vehicles['pilots']:
        for person in vehicles['pilots']:
            person = requests.request("GET", person, headers=headers)
            personJSON = person.json()
            if personJSON not in vehiclesPersonList:
                vehiclesPersonList.append(personJSON)

# -------------------------
# Films
# -------------------------
    if vehicles['films']:
        for film in vehicles['films']:
            film = requests.request("GET", film, headers=headers)
            filmJSON = film.json()
            if filmJSON not in vehiclesFilmList:
                vehiclesFilmList.append(filmJSON)

# -------------------------
# Species Template
# -------------------------

    parsed_all_output = vehicles_template.render(
        singleVehicles = singleVehiclesJSON,
        vehiclesPersonList = vehiclesPersonList,
        vehiclesFilmList = vehiclesFilmList
        )

# -------------------------
# Save Species File
# -------------------------

    with open(f"StarWars/Vehicles/{ singleVehiclesJSON['name'] }.md", "w") as fh:
        fh.write(parsed_all_output)                
        fh.close()

# -------------------------
# Star Wars Template
# -------------------------

parsed_all_output = starWars_template.render(
    peoplePersonList = peoplePersonList,
    peopleHomeworldList = peopleHomeworldList,
    peopleFilmList = peopleFilmList,
    peopleSpeciesList = peopleSpeciesList,
    peopleVehicleList = peopleVehicleList,
    peopleStarshipList = peopleStarshipList,
    filmFilmList = filmFilmList,
    filmPersonList = filmPersonList,
    filmPlanetList = filmPlanetList,
    filmStarshipList = filmStarshipList,
    filmVehicleList = filmVehicleList,
    filmSpeciesList = filmSpeciesList,
    planetPlanetList = planetPlanetList,
    planetPersonList = planetPersonList,
    planetFilmList = planetFilmList,
    speciesSpeciesList = speciesSpeciesList,
    speciesPersonList = speciesPersonList,
    speciesFilmList = speciesFilmList,
    starshipStarshipList = starshipStarshipList,
    starshipFilmList = starshipFilmList,
    vehiclesVehiclesList = vehiclesVehiclesList,
    vehiclesPersonList = vehiclesPersonList,
    vehiclesFilmList = vehiclesFilmList
    )

# -------------------------
# Save Star Wars File
# -------------------------

with open("StarWars/StarWars.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()