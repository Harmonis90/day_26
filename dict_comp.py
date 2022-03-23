import random
import pandas
sentence = "Hey there big boy."
# make a dictionary from each word in sentence as key and len as value
# words = sentence.split(" ")
# result = {word: len(word) for word in words}
# print(result)

result = {word:len(word) for word in sentence.split(" ")}
print(result)
# create a  list of students with random test scores and sift out the baddies

students = [
    "James",
    "Oscar",
    "Amber",
    "Violet",
    "Alford",
    "Dale",
    "Vivian",
    "Presto",
    "Camila",
    "Kelvin",
    "Brad",
    "Briony",
    "Abraham",
    "Kelvin",
    "Sawyer",
    "Cadie",
    "Kimberl",
    "Kristia",
    "Carina"
]
scores = {student: random.randint(55, 100) for student in students}
segregate_students = {good_student: score for (good_student, score) in scores.items() if score >= 90}
print(segregate_students)

