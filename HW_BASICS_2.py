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

# Exercise 8

student: dict = {
    'name': 'John',
    'age': 20,
    'hobbies': ['reading', 'games', 'coding'],
}


def student_data(data_dict: dict):
    for key, value in data_dict.items():
        print(f"{key}: {value}", end="")
        print()


student_data(student)


def new_hobby(data_dict: dict, new_in_hobbies: str) -> dict:
    if new_in_hobbies not in data_dict.get("hobbies"):
        data_dict["hobbies"].append(new_in_hobbies)
    return data_dict


print(new_hobby(student, 'music'))

student_data(student)


def remove_hobby(data_dict: dict, hobby: str) -> dict:
    if hobby in data_dict.get("hobbies"):
        data_dict["hobbies"].remove(hobby)
    return data_dict


print(remove_hobby(student, 'reading'))

student_data(student)

student['family_name'] = "White"
print(student)

# Exercise 9

matrix: list = [[1, 2], [3, 4], [5, 6]]


def print_matrix(matrix1: list):
    for lists in matrix1:
        for item in lists:
            print(item, end=" ")
    print()


print_matrix(matrix)

# Exercise 10

matrix = [[0, 1, 1], [0, 1, 0], [1, 0, 0]]


def zero_count(matrix1: list) -> int:
    zeros: int = 0
    for lists in matrix1:
        for item in lists:
            if item == 0:
                zeros += 1
    return zeros


print(zero_count(matrix))

# Exercise 11

arr: list[int] = [4, 2, 34, 4, 1, 12, 1, 4]


def find_dup(numbers: list[int]) -> list[int]:
    duplications: list[int] = []
    for number in numbers:
        if numbers.count(number) > 1:
            if number in duplications:
                continue
            duplications.append(number)
    return duplications


print(find_dup(arr))

# Exercise 12

arr: list = [43, "what", 9, True, "cannot", False, "be", 3, True]


def reverse_order(array: list) -> list:
    new_order: list = []
    for item in range(len(array) - 1, -1, -1):
        new_order.append(array[item])
    return new_order


print(reverse_order(arr))


# Exercise 13

def sum_of_each_pair(list1: list[int], list2: list[int]) -> list[int]:
    if len(list1) != len(list2):
        raise ValueError("Assume both lists are of the same length")
    return [list1[i] + list2[i] for i in range(len(list1))]


print(sum_of_each_pair([4, 6, 7], [8, 1, 9]))


# Exercise 14

def check_palindromes(word: str) -> bool:
    word = word.lower()
    return word == word[::-1]


print(check_palindromes("racecar"))
print(check_palindromes("Java"))

# Exercise 15

counter: int = 1
while True:
    number: int = int(input("Enter a number: "))
    counter *= 2
    if counter >= 100:
        break
print(counter)

# Exercise 16

counter: int = 900000
while True:
    number: int = int(input("Enter a number: "))
    counter /= 2
    if counter <= 50:
        break
print(f"{counter:.2f}")


# Exercise 17

def duplicates_array(words: list[str]) -> list[str]:
    new_list: list[str] = []
    index: int = 0
    while index < len(words):
        if words[index] in words[index + 1:] and words[index] not in new_list:
            new_list.append(words[index])
        index += 1

    return new_list


print(duplicates_array(['apple', 'banana', 'strawberry', 'apple', 'banana']))


# Exercise 18

def array_without_duplicates(names: list[str]) -> list[str]:
    result: list[str] = []
    index = 0
    while index < len(names):
        if names[index] not in result:
            result.append(names[index])
        index += 1
    return result


print(array_without_duplicates(['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']))


# Exercise 19

def without_pete(names: list[str]) -> list[str]:
    result: list[str] = []
    index = 0
    while index < len(names):
        if names[index] not in result and names[index] != 'Pete':
            result.append(names[index])
        index += 1
    return result


print(without_pete(['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']))


# Exercise 20

def find_repeated_index(array: list[bool]) -> int:
    index = 1
    while index < len(array):
        if array[index] == array[index - 1]:
            return index
        index += 1
    return -1


print(find_repeated_index([True, False, False, True, True, False]))
print(find_repeated_index([True, False, True, False, True, True]))
print(find_repeated_index([True, False, True, False, True, False]))

# Exercise 21

full_name: str = ""
age: int = 0
email: str = ""

while True:
    try:
        full_name: str = input("Enter your full name: ")
        if len(full_name.split()) > 2:
            print("You need to enter your first name and last name only, let's try again")
            continue

        age: int = int(input("Enter your age: "))
        if not 1 <= age <= 130:
            print("I hope you're joking, try again, please")
            continue

        email: str = input("Enter your email address: ")
        if '@' not in email:
            print("You need to use '@' sign, let's try again")
            continue
        else:
            print("Thank you!")
            break

    except ValueError as e:
        print("Please, use valid symbols for each category.", e)
