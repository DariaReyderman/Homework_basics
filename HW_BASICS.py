# Exercise 1

for i in range(12, 24 + 1):
    print(i, end=" ")
print()

# Exercise 2

for i in range(7, 31 + 1):
    if i % 2 != 0:
        print(i, end=" ")
print()

# Exercise 3

for i in range(10, 20 + 1):
    if i % 2 == 0:
        print(i, end=" ")
print()

# Exercise 4

for i in range(1, 45 + 1):
    if i % 3 == 0:
        print(i, "Fizz", end=" ")
    elif i % 5 == 0:
        print(i, "Buzz", end=" ")
    else:
        if i % 3 == 0 and i % 5 == 0:
            print(i, "FizzBuzz", end=" ")
print()


# Exercise 5

def sum_of_numbers(numbers: list[int]) -> int:
    number: int = 0
    for num in numbers:
        number += num

    return number


print(sum_of_numbers([1, 13, 22, 123, 49, 34, 5, 24, 57, 45]))

# Exercise 6

students = [
    {"id": 123456789, "first name": "Emma", "last name": "Watson", "age": 34, "country": "France",
     "city": "Paris"},
    {"id": 112233445, "first name": "Kate", "last name": "Winslett", "age": 49, "country": "UK",
     "city": "Reding"},
    {"id": 132435467, "first name": "Scarlett", "last name": "Johansson", "age": 40, "country": "USA",
     "city": "New York"}
]


def unwanted_data(students: list, inf: any) -> list:
    for student in students:
        if inf in student:
            del student[inf]

    return students


def properties_of_students(students: list):
    for student in students:
        for key, value in student.items():
            print(f"{key}: {value}", end=", ")
        print()


def sorted_by_age(students: list) -> list:
    sorted_students = sorted(students, key=lambda student: student['age'], reverse=True)

    return sorted_students


print("After removing one of properties", unwanted_data(students, "country"))
print("List of students' properties", properties_of_students(students))
print("List of students sorted by age", sorted_by_age(students))

# Exercise 7

our_pets = [
    {"animal_type": "cat",
     "names": ["Meowzer", "Fluffy", "Kit-Cat"]},
    {"animal_type": "dog",
     "names": ["Spot", "Bowser", "Frankie"]}
]


def cat_type(pets: list) -> str:
    for pet in pets:
        if pet.get("animal_type") == "cat":
            return "animalType: cat"
        else:
            return None


print("Cat only:", cat_type(our_pets))


def names_of_pets(pets: list, pet_type: str) -> list:
    for pet in pets:
        if pet.get("animal_type") == pet_type:
            return pet.get("names", None)


print("Names of each animal type", names_of_pets(our_pets, "cat"))


def new_name(pets: list, name: str) -> list:
    for pet in pets:
        if name not in pet.get("names"):
            pet["names"].append(name)

    return pets


print("New name", new_name(our_pets, "Fluffy"))
