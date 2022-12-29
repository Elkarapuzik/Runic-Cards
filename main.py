import file_operations
from faker import Faker
from random import randint
import random
import json


with open("skills.json", "r", encoding="UTF-8") as my_file:
    file_contents = my_file.read()
skills = json.loads(file_contents)

with open("runic_alphabet.json", "r", encoding="UTF-8") as my_file:
    file_contents = my_file.read()
runic_alphabet = json.loads(file_contents)

fake = Faker("ru_RU")


          
for i in range(10):
    three_random_skills = random.sample(skills,3)

    for letter in three_random_skills[0] :
        three_random_skills[0] = three_random_skills[0].replace(letter , runic_alphabet[letter] )

    for letter in three_random_skills[1] :
        three_random_skills[1] = three_random_skills[1].replace(letter , runic_alphabet[letter] )

    for letter in three_random_skills[2] :
        three_random_skills[2] = three_random_skills[2].replace(letter , runic_alphabet[letter] )

    genders = [
        'male',
        'female'
    ]

    genders_choosen = random.choice(genders)

    if genders_choosen == 'male' : 
        last_name = fake.last_name_male()
        first_name = fake.first_name_male()

    if genders_choosen == 'female' : 
        last_name = fake.last_name_female()
        first_name = fake.first_name_female()

    context = { 
        "job" : fake.job() ,
        "town" : fake.city() ,
        "first_name" : first_name ,
        "last_name" : last_name ,
        "strength" : randint(1, 9) ,
        "agility" : randint(1, 9) ,
        "endurance" : randint(1, 9) ,
        "intelligence" : randint(1, 9) ,
        "luck" : randint(1, 9) ,
        "skill_1" : three_random_skills[0],
        "skill_2" : three_random_skills[1],
        "skill_3" : three_random_skills[2],
    }

    file_operations.render_template("charsheet.svg", f"img/result{i}.svg" , context )
        


