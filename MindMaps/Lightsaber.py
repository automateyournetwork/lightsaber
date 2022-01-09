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

# film_template = env.get_template('film.j2')
# film = requests.request("GET", "https://swapi.dev/api/films/", headers=headers)
# filmsJSON = film.json()
# filmList = filmsJSON['results']

# -------------------------
# Single Film
# -------------------------

# filmFilmList = []
# filmPersonList = []
# for film in filmList:
#     singleFilm = requests.request("GET", film['url'], headers=headers)
#     singleFilmJSON = singleFilm.json()
#     if singleFilmJSON not in filmFilmList:
#         filmFilmList.append(singleFilmJSON)

# -------------------------
# Characters
# -------------------------
    # if film['characters']:
    #     for person in film['characters']:
    #         person = requests.request("GET", person, headers=headers)
    #         personJSON = person.json()
    #         if personJSON not in filmPersonList:
    #             filmPersonList.append(personJSON)

# -------------------------
# Film Template
# -------------------------

    # parsed_all_output = film_template.render(
    #     singleFilm = singleFilmJSON,
    #     filmPersonList = filmPersonList
    #     )

# -------------------------
# Save Films File
# -------------------------

    # with open(f"StarWars/Films/Episode_{ singleFilmJSON['episode_id'] }_{ singleFilmJSON['title'] }.md", "w") as fh:
    #     fh.write(parsed_all_output)                
    #     fh.close()

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
    #filmFilmList = filmFilmList,
    #filmPersonList = filmPersonList
    )

# -------------------------
# Save Star Wars File
# -------------------------

with open("StarWars/StarWars.md", "w") as fh:
    fh.write(parsed_all_output)               
    fh.close()