'''
author = Michal Kroupa
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

#Vytvoření slovníku s uživatelským jménem a heslem
Users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
oddelovac = "----------------------------------------"

#Vstup uživatele
username = input("username: ")
password = input("password: ")
print(oddelovac)

#Ověření uživatelského jména a hesla
if username in Users:

    if Users[username] == password:
        print(f"Welcome to the app, {username}")
        print(f"We have {len(TEXTS)} texts to be analyzed.")
        print(oddelovac)

    else:
        print("Incorrect password")
        print("Ending program...")
        print(oddelovac)
        quit()

else:
    print("Incorrect username")
    print("Ending program...")
    print(oddelovac)
    quit()

#výběr textu
choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
print(oddelovac)
#ověření vstupu od uživatele, zda jde o int a zda daný text existuje
if choice.isnumeric():
    choice = int(choice)
    if choice > len(TEXTS):
        print(f"Invalid number, max number of texts is {len(TEXTS)}")
        print("Ending program...")
        print(oddelovac)
        quit()
else:
    print("Invalid input")
    print("Ending program...")
    print(oddelovac)
    quit()


words_count = 0
titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
numeric_count = 0
numbers = []

#Procházení slov ve vybraném textu
for word in TEXTS[choice-1].split():
    word = word.strip(".:,")
    #Zkouška zda je slovo číslo
    if word.isnumeric():
        numeric_count+=1
        numbers.append(int(word))
        words_count += 1
    #Pokud je slovo string
    else:
        words_count += 1
        #Pokud je slovo psané velkým písmem, a pokud v tom není číslo
        if word.isupper() and word.isalpha():
            uppercase_count += 1
        #Pokud je velké počáteční písmenu
        elif word == word.title():
            titlecase_count += 1
        #Pokud je slovo psané malým písmem
        elif word.islower():
            lowercase_count += 1

#Výpis analýzy textu
print(f"There are {words_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {sum(numbers)}")

print(oddelovac)
print("LEN| OCCURENCES    |NR.")
print(oddelovac)

word_length = dict()
#Procházení textu a ukládání jeho délky a počet výskytu do slovníku
for word in TEXTS[choice-1].split():
    word = word.strip(".:,")
    if len(word) not in word_length:
        word_length.setdefault(len(word), 1)
    else:
        word_length[len(word)] += 1

star = "*"
#Seřadí slovník, vypíše pořadí a počet výskytu vyjádřený hvězdami a číslem
for occurence in sorted(word_length.items()):
    print(f"{occurence[0]:>2}|{star * occurence[1]:<15} | {occurence[1]}")


