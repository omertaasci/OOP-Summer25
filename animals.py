def create_animal(name, group, number_of_legs, skills):
    return {
        "name": name,
        "group": group,
        "number_of_legs": number_of_legs,
        "skills": skills
    }

animals = [
    create_animal("Cat", "Mammals", 4, ["Jumping", "Climbing", "Hunting"]),
    create_animal("Dog", "Mammals", 4, ["Running", "Swimming", "Guarding"]),
    create_animal("Eagle", "Birds", 2, ["Flying", "Hunting", "Sharp Vision"]),
    create_animal("Frog", "Amphibians", 4, ["Jumping", "Swimming", "Camouflage"]),
    create_animal("Snake", "Reptiles", 0, ["Slithering", "Camouflage", "Hunting"])
]

for animal in animals:
    print(animal)