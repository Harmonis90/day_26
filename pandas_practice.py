import random
from colorama import Fore, Back, Style
import pandas

def green_text(text):
    return Fore.GREEN + str(text) + Fore.RESET

def red_text(text):
    return Fore.RED + str(text) + Fore.RESET

students_names = [
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
scores = [69, 95, 70, 94, 94, 74, 91, 63, 74, 100, 76, 97, 91, 83, 82, 68, 81, 91, 55]
student_scores = {
    "students": students_names,
    "scores": scores,
}
student_df = pandas.DataFrame(student_scores)


# pandas has iterrows which will iterate through dict[row[i]] for each column
# example
for (index, row) in student_df.iterrows():
    if row.scores >= 90:
        print(green_text(row))
    elif row.scores < 60:
        print(red_text(row))
    else:
        print(row)