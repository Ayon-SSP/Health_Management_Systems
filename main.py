# In this project i have used file io basic
import datetime
DT = datetime.datetime.now()
print(DT)

print("1)Lock\n2)retrieve")
lock_or_retrieve = int(input())
print("1)AYON\n2)Hacker\n3)Carry")
name_of_the_clint = int(input())


def to_do():
    print("1)Exercise\n2)Food")

def what_to_add_in_the_file():
    content_of_Exercise_or_food = input()
    list.write("\n--------------------------------------------------\nDate and Time :-")
    list.write(str(DT))
    list.write("\n")
    list.write(content_of_Exercise_or_food)
    list.write("\n--------------------------------------------------")
    list.close()
    print("UPDATE IS DONE👺")


if (lock_or_retrieve == 1): 
    if (name_of_the_clint == 1):
        to_do()
        food_or_Exercise = int(input())

        if (food_or_Exercise == 1):
            print("what would u like to save in Exercise")
            list = open("AYON_Exercise.TXT", "a")
            what_to_add_in_the_file()
        elif (food_or_Exercise == 2):
            print("what would u like to save in food")
            list = open("AYON_Food.TXT", "a")
            what_to_add_in_the_file()

    elif (name_of_the_clint == 2):
        to_do()
        food_or_Exercise = int(input())

        if (food_or_Exercise == 1):
            print("what would u like to save in Exercise")
            list = open("Hacker_Exercise.TXT", "a")
            what_to_add_in_the_file()
        elif (food_or_Exercise == 2):
            print("what would u like to save in food")
            list = open("Hacker_Food.TXT", "a")
            what_to_add_in_the_file()

    elif (name_of_the_clint == 3):
        to_do()
        food_or_Exercise = int(input())

        if (food_or_Exercise == 1):
            print("what would u like to save in Exercise")
            list = open("CARRY_Exercise.TXT", "a")
            what_to_add_in_the_file()
        elif (food_or_Exercise == 2):
            print("what would u like to save in food")
            list = open("CARRY_Food.TXT", "a")
            what_to_add_in_the_file()


elif (lock_or_retrieve == 2):
    if (name_of_the_clint == 1):
        to_do()

        food_or_Exercise = int(input())
        if (food_or_Exercise == 1):
            list = open("AYON_Exercise.TXT")
            print(list.read())
        elif (food_or_Exercise == 2):
            list = open("AYON_Food.TXT")
            print(list.read())

    elif (name_of_the_clint == 2):
        to_do()
        food_or_Exercise = int(input())

        if (food_or_Exercise == 1):
            list = open("KARMAKAR_Exercise.TXT")
            print(list.read())
        elif (food_or_Exercise == 2):
            list = open("KARMAKAR_Food.TXT")
            print(list.read())

    elif (name_of_the_clint == 3):
        to_do()
        food_or_Exercise = int(input())

        if (food_or_Exercise == 1):
            list = open("HARRY_Exercise.TXT")
            print(list.read())
        elif (food_or_Exercise == 2):
            list = open("HARRY_Food.TXT")
            print(list.read())
  