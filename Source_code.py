# In this project i have used file io basic




while(True):

    import datetime
    DT = datetime.datetime.now()
    print(DT)

    print("1)Lock\n2)retrieve")
    lock_or_retrieve = int(input())
    print("1)AYON\n2)KARMAKAR\n3)HARRY")
    name_of_the_clint = int(input())

    
    def to_do():
        print("1)Excersise\n2)Food")

    def what_to_add_in_the_file():
        content_of_Excersise_or_food = input()
        list.write("\n--------------------------------------------------\nDate and Time :-")
        list.write(str(DT))
        list.write("\n")
        list.write(content_of_Excersise_or_food)
        list.write("\n--------------------------------------------------")


    if (lock_or_retrieve == 1):
        if (name_of_the_clint == 1):
            to_do()
            food_or_excersise = int(input())

            if (food_or_excersise == 1):
                print("what would u like to save in Excersise")
                list = open("AYON_Excersise.TXT", "a")
                what_to_add_in_the_file()
            elif (food_or_excersise == 2):
                print("what would u like to save in food")
                list = open("AYON_Food.TXT", "a")
                what_to_add_in_the_file()

        elif (name_of_the_clint == 2):
            to_do()
            food_or_excersise = int(input())

            if (food_or_excersise == 1):
                print("what would u like to save in Excersise")
                list = open("KARMAKAR_Excersise.TXT", "a")
                what_to_add_in_the_file()
            elif (food_or_excersise == 2):
                print("what would u like to save in food")
                list = open("KARMAKAR_Food.TXT", "a")
                what_to_add_in_the_file()

        elif (name_of_the_clint == 3):
            to_do()
            food_or_excersise = int(input())

            if (food_or_excersise == 1):
                print("what would u like to save in Excersise")
                list = open("HARRY_Excersise.TXT", "a")
                what_to_add_in_the_file()
            elif (food_or_excersise == 2):
                print("what would u like to save in food")
                list = open("HARRY_Food.TXT", "a")
                what_to_add_in_the_file()


    elif (lock_or_retrieve == 2):
        if (name_of_the_clint == 1):
            to_do()

            food_or_excersise = int(input())
            if (food_or_excersise == 1):
                list = open("AYON_Excersise.TXT")
                print(list.read())
            elif (food_or_excersise == 2):
                list = open("AYON_Food.TXT")
                print(list.read())

        elif (name_of_the_clint == 2):
            to_do()
            food_or_excersise = int(input())

            if (food_or_excersise == 1):
                list = open("KARMAKAR_Excersise.TXT")
                print(list.read())
            elif (food_or_excersise == 2):
                list = open("KARMAKAR_Food.TXT")
                print(list.read())

        elif (name_of_the_clint == 3):
            to_do()
            food_or_excersise = int(input())

            if (food_or_excersise == 1):
                list = open("HARRY_Excersise.TXT")
                print(list.read())
            elif (food_or_excersise == 2):
                list = open("HARRY_Food.TXT")
                print(list.read())
