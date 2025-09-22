# Variables = a container

# String: 
# name = "Dylan"

# Integer:
# Age = 14

# Float:
# Bank_Amount = 100000000.422

# Boolean:
# Online = True
# Offline = False 

# print(type(name))
# print(f"his name ios {name}")
# if Online:
#     print("He is online")
# elif Offline:
#     print("He is offline")
# else:
#     print("Not online")







# Typecasting = Changing one data type into another
# explicit vs implicit casting

# Explicit = manual changing one data type into another
# name = "Dylan"
# age = 14
# gpa = 5.8
# student = True

# age = bool(age)
# print(age) if age = 0 then it is false, else it is true 
# print(type(age)) 

# student = bool(student)
# print(student) if student = "" then it is false, else it is true 
# print(type(student)) 

# age = float(age)
# print(type(age))

# student = str(student)
# print(type(student))

# print(f"he is {age} and gpa of {gpa}") f strings count

# Implicit = a variable data type that can be preformed when doing certain stuff like operations

# x = 2
# y = 2.0
# x = x/y 

# print(x) x will be a float even though there are 2 data types 



# Input = what the user puts into the website to get something out of it

# name  = input("Enter your name: ")  ---- question
# age = int(input("Age: "))
# age = float(input("Age: "))
# age = age + 1 

# print(f"Hello {name}")
# print(f"You are {age}")

# cube excercise

# length = float(input("Length: "))
# width = float(input("width: "))
# height = float(input("height: "))

# volume = length * width * height 

# print(f"the volume is {volume} cm^3")

# shopping excercise 

# item = input("what do you want to buy: ")
# quantity = int(input("how much of the item do you want to purchase: "))
# value = float(input("what is the price: "))

# price = quantity * value 

# print(f"you bought {item} this many times {quantity}")
# print(f"The price of the tiem is {value} and in the end is {round(price, 2)}") round rounds it to the nearist 2nd decimal 




# python quiz game senerio


# questions = ("name: ",
#              "age: ", 
#              "sex: ", 
#              "grade: ", 
#              "ethnicity: ")

# options = (("d", "hi", "bye", "lie"), ("d", "hi", "bye", "lie"), ("d", "hi", "bye", "lie"), ("d", "hi", "bye", "lie"), ("d", "hi", "bye", "lie"))
# answer = ("d", "d", "d", "d", "d")
# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("_____")
#     print(question)
#     for option in options[question_num]:
#         print(option)
    
#     guess = input("Enter(answer): ").lower()
#     guesses.append(guess)
#     if guess == answer[question_num]:
#         score +=1
#         print("correct")
#     else:
#         print(f"incorrect, answer: {answer[question_num]}")
#     question_num += 1


# print("answers: ", end="")
# for answe in answer:
#     print(answe, end="")
# print()

# print("guesses: ", end="")
# for guess in guesses:
#     print(guess, end="")
# print()

# score = int(score/len(questions) * 100)

# print(f"score: {score}")







# Operations in pyuthon symplified 

# stuff = stuff + 1 addition
# stuff += 1 

# stuff = stuff - 1 subtraction
# stuff -= 1 

# stuff = stuff * 1 mutiplication
# stuff *= 1 

# stuff = stuff / 1 division
# stuff /= 1 

# stuff = stuff ** 1 exponents
# stuff **= 1 

# stuff = stuff % 1 remainder


# print(stuff)


# built in functions 

# x = 3.14
# y = -4 
# z = 5

# thing = round(x, anything) rounds it to the nearist anything you want 

# thing = abs(y) gets the absoulute value of y 

# thing = pow(4, 3) it raises 4 to the power of 3

# thing = max(x, y, z) maximium value out of the three 

# thing = min(x, y, z) mininium value out of the three 


# module 

# import math 

# l = 9

# li = 9.1

# lix = 9.9

# print(math.pi)

# print(math.e)

# thing = math.sqrt(l) square root 

# thing = math.ceil(li) rounds the number up 

# thing = math.floor(lix) rounds the number down


# circle area 

# import math 

# r = float(input("what is the radius of the circle: "))
# e = math.pi
# r2 = pow(r,2)
# solution = e * r2

# print(round(solution, 2))

# hypothenuse 

# import math

# a = float(input("what is the first side of the triangle? "))
# b = float(input("what is the second side of the triangle? "))

# answer = pow(a, 2) + pow(b, 2)

# c = math.sqrt(answer)

# print(round(c, 2))




# if = do some code only IF some condition is true Else do something else 

# age = int(input("Enter age: "))
# if age >= 18 and age <= 99: 
#     print("You are now signed up! ")
# elif age < 0:
#     print("you havent been born yet!")
# elif age > 100:
#     print("you are dead ")
# else:
#     print("you are not signed up")

# response 

# response = input("Eat food? (Y/N) \n")
# if response == "Y":
#     print("your food")
# else:
#     print("F u ")

# name = bool(input("Enter your name: "))

# if name:
#     print(f"hello {name}")
# else:
#     print("type ur name")




# logical operators

# and = check two or more conditions are ture 
# or = checks if at least one condition is true 
# not = True if condition is false, vice versa

# # temp = 25 
# sunny = True

# # if temp > 0 and temp < 30:
# #     print("the temepertature is good ") if the tempertature meets the requirment, it prints this
# # else:
# #     print("it is bad") else, it prints this statement

# # if temp > 0 or temp < 30:
# #     print("the temepertature is bad ") if the tempertature meets the requirment, it prints this
# # else:
# #     print("it is good") else, it prints this statement

# if not sunny:
#     print("it is sunny") if true, it prints this 
# else:
#     print("it is cloudy") if false, it prints this

# if sunny:
#     print("it is sunny") if true, it prints this 
# else:
#     print("it is cloudy") if false, it prints this







# conditional expression = A one line shortcut for the if else statements (ternary operator) Print or assign one of two values based on a condition X if condition else Y

# num = 6
# a = 2
# b = 7
# temperature = 30
# user_role = "admin"


# print("Positive" iif num >0 else "Negative")
# result = "even" if num % 2 == 0 else "odd"
# max_num = a if a > b else b 
# min_num = a if a < b else b 
# status = "adult" if age >= 18 else "child"
# weather = "hot" if temperature > 20 else "cold"
# access_level = "full access" if user_role == "admin" else "limited acess"

# print(anything)



# string methods

# name = input("Enter your full name: ")


# result = len(name) length of the name
# result = name.find(" ") it finds the first occurance of this and it happens to start at 0
# result = name.rfind("") the same thing but last occurance
# name = name.caplitalize() captitlizes the first index
# name = name.upper() all upper
# name = name.lower() all lower
# result = name.isdigit() its a boolean if the string only contains digits, its true 
# result = name.isalpha() return a boolean if the string is only letters without space its true, else false
# result = name.count("a") counts how many a's are in the code
# name.replace(",", "a") it replaces one thing on the left to the right
# print(help(str)) all the different things for striungs with descrioptions


# print(result)
# print(name)


# Excercise 

# username = input("whats your name: ")
# name = 12 
# if len(username) <= 12:
#     if username.isalpha():
#         print(username)
#     elif not username. find(" ") == -1:
#         print(" cant have spaces")
#     else:
#         print("try again, your username can not contain numbers")
# else:
#     print("try again, your name needs to be shorter or equal to 12")






# indexing = accessing elements of a sequence using [] indexing op, [start: end: step]

# number = "1234567899"

# lastdigit = number[-4:]
 
# reverse = number[::-1] 

# print(reverse) it prints it in reverse

# print(f"{lastdigit}")


# print(number[0]) first digit
# print(number[0:4]) the last number is exclusive the first number is inclusive
# print(number[0:10:2]) every two digits\
# print(number[-1]) is last digit
# print(number[-3]) is the 3rd last and its like that
# print(number[::2]) its starts at the start, ends at the end and goes by 2




# Email Slice Excercise

# email = input("Enter your emal: ")

# index = email.index("@")
# username = email[:index]
# domain = email[index + 1: ]

# print(f"your username is {username} and domain is {domain}")






# format specifiers = {value:flags} format a value absed on what flags are inserted 

# price_1 = 30000000.1415
# price_2 = -999.22
# price_3 = 12.939



# print(f"first price ${price_1: .2f}") is 2 decimals , {pric_1: .2 } is 2 digits
# print(f"first price ${price_1: >10}") right align
# print(f"first price ${price_1: <10}") left align
# print(f"first price ${price_1: ^10}") Center
# print(f"first price ${price_1: }") lined up evenly 
# print(f"first price ${price_1:+}") makes it plus or minus 
# print(f"first price ${price_1:,}") each thousand place is matched with a comma







# While loops = infinte loop unless false

# name = input("Enter your name: ")

# while name == "":
#     print("no name")
#     name = input("Enter your name: ")
# else:
#     print(f"{name}")


# age = int(input("Enter your age: "))

# while age < 0:
#     print("age is not negative")
#     age = int(input("Enter your age: "))

# print("age")


# food = input("enter food(q is quit): ")

# while not food =="q":
#     print(f"you like {food}")
#     food = input("enter food(q is quit): ")

# print("bye")


# num = int(input("number 1 - 10: "))

# while num < 1 or num > 10:
#     print("num is not valid")
#     num = int(input("number 1 - 10: "))

# print(f"{num}")





# compound intrest calc

# principle = 0 
# rate = 0 
# time = 0 

# principle = int(input("whats ur amount?: "))
# rate = int(input("whats ur rate?: "))
# time = int(input("whats ur time?: "))

# while principle <= 0:
#     print("principle cant be less than or eqaul to 0")
#     principle = float(input("enter a principle: "))
#     if principle <= 0:
#         print("principle cant be zero")


# while time <= 0:
#     print("time cant be less than or eqaul to 0")
#     time = int(input("enter a time: "))
#     if time <= 0:
#         print("time cant be zero")


# while rate <= 0:
#     print("rate cant be less than or eqaul to 0")
#     rate = float(input("enter a principle: "))
#     if rate <= 0:
#         print("rate cant be zero")

# total = principle * pow((1 + rate/100), time)

# print(f"balance after{time} years: {total:.2f}")





# for loops = execute a block of code a fixed number of times. You can iterate over a range, string, sequence or more! 


# for x in reversed(range(1, 11, 2)): reverses the loop
#     print(x)

# credit_card = "1234_5678_9012_3456"

# for x in credit_card:
#     print(x)

# for x in range(1,21):
#     if x == 13:
#         continue it skips the code
#         break breaks out of the loop 
#     else:
#         print(x)




# nested loops = a loop within another loop (outer, inner)

# for x in range(1,11):
#     print(x, end="") put it on the same line


# for x in range(3):
#     for y in range(1,10):
#         print(y, end="")
#     print() prints on different lines


# rows = int(input("number:"))
# column = int(input("number:"))
# symbol = input("symbol")

# for x in range(rows):
#     for y in range(column):
#         print(symbol, end="")
#     print()



# import time

# mytime = int(input("time: "))

# for x in range(0, mytime, -1):
#     seconds = x % 60
#     minutes = int(x/60) % 60
#     hour = int(x/3600)
#     print(f"{hour:02}:{minutes:02}:{seconds:02}")
#     print(x)
#     time.sleep(1)

# print("wake")




# collection = single "variable" used to store values like a list, set or a tuple 

# list = [] is ordered and changeable. Duplicates are Ok
# set = ordered and immutable, but add/remove ok. No dublicates
# tuple = () ordered and unchangeable. Duplicates ok. Faster than list


# list

# fruits= ["apple", "orange", "banana", "coconut"]

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0,"pineapple")
# fruits.clear()
# fruits.sort()
# fruits.reverse()

# fruits.count("banana")
# fruits.index("apple")



# set

# stuff = {"apple", "orange", "banana", "coconut"}

# stuff.add("pineapple")
# stuff.remove("apple")
# stuff.clear()


# tuple = same as list but less functions but faster




# shopping cart program

# foods = []
# prices = []
# total = 0 

# while True:
#     food = input("Enter a food: (q = quit): " )
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"price of {food}: "))
#         foods.append(food)
#         prices.append(price)

# print("your cart: ")

# for food in foods:
#     print(food, end=" ")
# for price in prices:
#     total += price

# print(total)






# 2d list = is a nested list

# fruit = ["apple", "orange", "banana", "coconut"]
# vegetable = ["carrot", "tomato", "potato"]
# meat = ["chicken", "fish", "turkey"]

# groceries = [fruit,vegetable,meat]

# print(groceries) entire list flat out 

# print(groceries[0][0]) its like cordinates, this giver you apple

# you dont need to give names to the variables in the 2d list

# groceries = [
# ["apple", "orange", "banana", "coconut"],
# ["carrot", "tomato", "potato"],
# ["chicken", "fish", "turkey"]]

# tuple and sets both work

# for collection in groceries:
#     for food in collection:
#         print(food, end="")
#     print()


# 2d keypad

# num = [(1,2,3),(4,5,6),(7,8,9,)("*",0,"#")]

# for rows in num:
#     for num_pad in rows:
#         print(num_pad,end=" ")







# dictionary = collection of {key:value} pairs, ordered and changeable. No dubl;icagtes 



# thing = {"i": "I", 
#          "j": "J",
#          "h": "H"}

# print(dir(thing)) gives you the commands
# print(help(thing)) helps you understand
# print(thing.get("i")) gets teh value

# if thing.get("i"):
#     print("hi")
# else:
#     print("try again")

# thing.update({"d": "D"}) you can update this into the dict

# thing.update({"i": "D"}) you can update a new value inthe dict

# thing.pop("i") deletes this 

# thing.popitem() pops the last item

# thing.clear() clears the whole thing 
# thing.keys() gives you all the keys 
# print(thing)

# thing.value() gives you all teh values 

# you can iterate over a dict

# thing.items() gives you the whole 2d list printed

# for key, value in thing.items():
#     print(f"{key}: {value}")





# Concession Stand code 


# menu = {"pop": 200,
#         "candy": 100,
#         "fruit": 50}

# cart = []
# total = 0 

# print("menu: ")

# for key, value in menu.items():
#     print(f"{key}: ${value}")

# print("___________")

# while True:
#     food = input("Select item(q = quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
# print("your order")
# for food in cart:
#     total += menu.get(food)
#     print(food, end="")

# print()
# print(f"total = {total:.2f}")



# random number 


# import random 

# # print(help(random)) teaches you the methods

# low = 1
# high = 100 

# options = ("rock","paper","scissor")
# cards = ["2", "3","4","5"]

# num = random.randint(low,high) integer

# number = random.random() float

# print(num)

# opt = random.choice(options) string 

# print(opt)

# random.shuffle(cards) shuffles the list or array of numbers



# Number guessing game


# import random 

# low = 1 
# high = 100 

# guesses = 0 

# number = random.randint(low,high)

# while True:
#     guess = int(input(f"Enter a number between {low} - {high}: "))
#     guesses += 1 


#     if guess < number:
#         print(f"{guess} is low ")
#     elif guess > number:
#         print(f"{guess} is high ")
#     else:
#         print(f"{guess} is correct")
#         break

# print(f"This took {guesses} guesses")







# import random 

# thing = ("rock", "paper", "scissor")
# points = 0 

# running = True
# while running:
    
#     player = None
#     computer = random.choice(thing)
#     while player not in thing:
#         player = input("Enter rock paper or scissor:  ")

#     print(f"player {player}")
#     print(f"computer {computer}")

#     if player == computer:
#         print("tie")
#     elif player == "rock" and computer == "scissor":
#         print("you win")
#         points += 1
#     elif player == "scissor" and computer == "paper":
#         print("you win")
#         points += 1
#     elif player == "paper" and computer == "rock":
#         print("you win")
#         points += 1
#     else:
#         print("you lose")
    
#     if not input("play again? (y/n):  ").lower() == "y":
#         running = False

# print(points)







# Ascy art : unicode characters

# import random 
# # ● ┌ ─ ┐ │ └ ┘


# dice_art = {
#     1: ("┌─────────┐",
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘"),
#     2: ("┌─────────┐",
#         "│  ●      │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘"),
#     3: ("┌─────────┐",
#         "│  ●      │",
#         "│    ●    │",
#         "│      ●  │",
#         "└─────────┘"),
#     4: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│         │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     5: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│    ●    │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     6: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "└─────────┘")
# }

# dice = []
# total = 0
# num_of_dice = int(input("How many dice?: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line) 




# for die in dice:
#     total += die
# print(f"total: {total}")







# encyrpting a mesage: hiding a message

# import random 

# import string

# char = " " + string.punctuation + string.digits + string.ascii_letters

# chars = list(char)



# key = chars.copy()
# random.shuffle(key)
# print(f"chars: {chars}")
# print(f"keys: {key}")

# message = input("message: ")
# cipher = ""

# for letter in message: 
#     index = chars.index(letter)
#     cipher += key[index]

# print(f"original message: {message}")
# print(f"encyrpted message: {cipher}")





# functions = a block of reusable code . place () after the function name to invoke it 



# def dappy():
#     print("happy phone")


# dappy()



# def dappy(name, age): 
#     # input things in the parameters to be more interactive 

#     print(f"happy phone: {name}")
#     print(f"you are {age}")


# dappy("DYlan", 20)
# dappy("Duan", 15)



# display function


# def displa_voice(username, amount, due_date):
#     print(f"hello {username}")
#     print(f"Your Bill {amount:.2f} at this {due_date}")

# displa_voice("dill", 100.040404040, "01/20")





# Return = statement used to end a dunction and send a result back to the caller 

# def add(x,y):
#     z = x + y
#     return z 

# print(add(1,2))



# def fullname(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last

# full_name = fullname("dylan", "duan")

# print(full_name)





# default arguments = A default value for certain parameters/ default is used when that argument is ommites / make your functions more fleciable and reduces the number of argumernts. 
# 1. postional, 2. Default, 3. keyword, 4. arbitary 



# def net_price(list_price, discount = 0, tax = 0.05):
#     return list_price * (1 - discount) * (1 + tax)
# # print(net_price(500)) 1 argument
# print(net_price(500,0.1, 0))


# postional arguments in front of default numbers which are the non default arguments 


# import time 

# def count(end, start = 0, ):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("hi")

# # count(0,10)
# count(10)





# Keyword arguments = an argument preceded an identifier helps with readability, order of arguyments doesn't matter
# 1. positional 2. default 3. keyword 4. arbitrary


# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last} ")

# hello("hello", title = "mr.", last = "Duan" , first = "Dylan")
# # the order doesnt matter


# for x in range(1, 11):
#     print(x, end = " ")
# key word argument 

# print("1","2","3", sep="-")


# def phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"
# num = phone(country=1, area=123,first=456,last=789)

# print(num)





# Arbitary Arguments = random/various arguments (pass non key arguments)
# Kwargs = allows you to pass multiple non - key arguments 
# Unpacking operator
# 1. Positional 2. Keyword 3. Default 4. Arbitrary

# def add(a,b):
#     return a + b 

# print(add(1,2)) Only accepts 2 

# args can be anything
# def add(*args):
#     total = 0 
#     for arg in args: 
#         total += arg
#     return total 

# print(add(1))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Dr.","Dylan Duan ")
# # Stackable 


# pack into a dictonary
# items is for both key and value 
# def print_address(**kwargs):
#     for value,key in kwargs.items():
#         print(f"{key}: {value}")


# print_address(street="somethign ave", city="Vancouver", provence="BC", zip="fiofiodshjiohdoi")

# def shippinglabel(*args, **kwargs):
#     for arg in args:
#         print(arg, end="")
#     print()
#     # for key,value in kwargs.items():
#     #     print(value, key, end="")
#     print(f"{kwargs.get('street')}")

# # for kwargs, '' quotation only works 
# # conditionals work

# shippinglabel("Dr. Dylan", "Duan", "is him", street = "didjd", age = "fhuhdfiohiod", thing = "fghiuhdfuhidf")





# Iterables = an object/collection that can return its elements one at a time, allowing it to be iterated over in a loop 


# list are iterable
# numbers = [1,2,3,4,5]

# for number in numbers: 
#     print(number)

# for number in reversed(numbers): 
#     print(number, end = "-")

# name = "Dylan Duan"

# for i in name:
#     print(i, end="")

# tuples

# numbers = (1,2,3,4,5)

# for i in numbers:
#     print(i)


# set

# you can not reverse in a set

# fruits = {"apple", "orange", "banana", "coconut"}

# for i in fruits:
#     print(i)

# dictonary 

# dict1 = {"a": 1, "b": 2}

# for key,value in dict1.items():
#     print(f"{key} = {value}")



# Membership operators = used to test wether a value or variable is found in a sequence (string, list, tuple, or dictionary)
# 1. in 
# 2. not in 

# word = "apple"

# letter = input("what letter in the secret word: ")

# if letter in word:
#     print(f"there is a letter in {letter}")
# else:
#     print(f"{letter} not in word")


# if letter not in word:
#     print(f"there is a letter in {letter}")
# else:
#     print(f"{letter} not in word")

# list

# student = {"Dylan", "Duan", "St. Georges"}

# students = input("Enter the name of a student: ")

# if students in student:
#     print(f"{students} is here")
# else:
#     print(f"{students} isn't here")


# Dict

# grades = {"Dylan": 4,
#           "Duan": 2,
#           "Lmao": 3}

# thiohtio = input("Enter the name of a student: ")

# if thiohtio in grades:
#     print(f"{thiohtio}'s grade is {grades[thiohtio]}")
# else:
#     print("not found")

# Str


# email = "BroCode@Gmail.com"

# if "@" in email and "." in email:
#     print("Valid Email")
# else:
#     print("Invalid Email")


# List Comprehension = A concise way to creat lists in Python. Compact and easier to read than traditional loops 
# [expression for value in iterable if condition]

# doubles = []
# for x in range(1,11):
#     doubles.append(x)

# print(doubles)
# Takes too long to write and slower CPU 


# doubles =[x * 2 for x in range(1,11)]

# print(doubles)

# triples = [y*3 for y in range (1,11)]
# print(triples)

# more concise way 


# str 

# fruits = ["apple", "orange", "pineapple"]

# # fruits = [fruit.upper() for fruit in fruits]
# fruits = [fruit[0] for fruit in fruits]

# print(fruits)

# num

# numbers = [1,-2,3,-4,5,6]

# # positivenums = [num for num in numbers if num >= 0]
# # even = [num for num in numbers if num % 2 == 0]

# print(even)


# grades

# grades = [60,3,4,70,100,94]
# passinggrades = [grade for grade in grades if grade >= 60]

# print(passinggrades)








# module - a file containting code you want to include in your program use "import" to include a module (built in or your own) useful to break up a large program resusable spearate files 

# import math 
# print(math.pi)

# import math as m - giving it a nickname
# print(math.pi)

# from math import pi
# print(pi)

# There may be name conflicts like 
# from math import e 
# a,b,c,d,e = 1,2,3,4,5
# print(math.e ** a ) is less confusing than print(e ** a)


# pi = 3.1415

# def square(x):
#     return x ** 2

# def cube(x):
#     return x ** 3

# You can use these modules on another file but your need to import the pythong file e.g. import Python101




# variable scope = where a variable is visible and accessible
# scope resolution = {LEGB} Local - enclosed - global - built in 

# def func():
#     a = 1
#     print(b)

# def func2():
#     b = 2
#     print(a)

# func()
# func2()

# You can not see a variable inside another function, thats why variable scope is useful 

# def func1():
#     x = 1
#     def func2():
#         print(x)
#     func2()
# func1()

# enclosed scope - - /

# def func1():
#     print(x)
# def func2():
#     print(x)

# x = 1
# func1()
# func2()
# prints the global variable 1 

# from math import e --- built in 

# def func1():
#     print(e)

# e  = 3





# if __name__ == __main__: (this script can be imported or run standalone) Functions and classes in this moduile can be reused without the main block of code executing
# libary = all the comands in python 

# Functions and classes in this module can be reused without the main block of code executing
# Good practice (code is modular, helps with readablility, leaves no global variables, avoid uninteneded executions)
# ex libary = import library for functionality/ When running libary directly, display a help page

# create two new scipts - combines the all scripts in the folder 
# from scipt import *  - it imports all the functions into the the doc that you are working in kind of like public classes in java 

# def favourite_food(food):
#     print(f"Your favourite food is {food}")

# def main():
#     print("This is scipt")
#     favourite_food("pizza")
#     print(favourite_food)


# if __name__ == "__main__":
#     main()






# Python Credit CVard Validator Program 

# sum_odd_digits = 0 
# sum_even_digits = 0 
# total = 0

# # Step one 
# cardnumber = input("enter credit card number: ")
# cardnumber = cardnumber.replace("-", "")
# cardnumber = cardnumber.replace(" ", "")
# cardnumber = cardnumber[::-1]

# # Step 2 

# for x in cardnumber[::2]:
#     sum_odd_digits += int(x) 

# # Step 3

# for x in cardnumber[1::2]:
#     x = int(x * 2)
#     if x >= 10:
#         sum_even_digits += 1 + (x % 10)
#     else:
#         sum_even_digits += x 
    
# #step 4 

# total = sum_odd_digits + sum_even_digits

# # Step 5 

# if total % 10 == 0:
#     print("VALID")
# else:
#     print("INVALID")








# Python Banking Program 
# balance = 0 

# def show_balance():
#     print(f"your balance is {balance}")

# def deposit():
#     global balance
#     amount = float(input(f"how much do you want to deposit? "))
#     if amount < 0:
#         print("thats not right")
#         return 0 
#     else:
#         balance += amount

# def withdraw():
#     global balance
#     amount = float(input("How much do you want to withdraw? "))

#     if amount > balance:
#         print("not right")
#         return 0
#     elif amount < 0:
#         print("not right")
#     else:
#         balance -= amount



# def main():
#     is_running = True 

#     while is_running:
#         print("Banking Program \n")
#         print("1. Show Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")

#         choice = input("Enter your choice(1 - 4): ")

#         if choice == "1":
#             show_balance()
#         elif choice == "2":
#             deposit()
#         elif choice == "3":
#             withdraw()
#         elif choice == "4":
#             is_running = False
#         else:
#             print("try again")


#     print("Thank you, enjoy this fine day shawty")

# if __name__ == '__main__':
#     main()








# ** Important
# object = A bundle of related attributes (variables) and methods (functions)
# Ex. phones. cup. book
# You need a class to create many objects 

# class = (blueprint) used to design the structure and layout of an object 

# Constructors like Java 

# dunder = double underscore

# You could import your car and make it into another file 

# from (The file) import (the class)

# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year 
#         self.color = color
#         self.for_sale = for_sale

#     def drive(self):
#         print(f"drive {self.color} {self.model}")
#     def stop(self):
#         print(f"you stop the {self.color} {self.model}")
#     def describe(self):
#         print(f"{self.year} {self.color} {self.model}")
    

# car1 = Car("Mustang", 2021, "Red", False)
# # . is very important accessing the memory of the car1
# car2 = Car("Lamborgini", 1929, "Black", True)
# print(car1.model)

# car1.stop()
# car2.drive()
# car1.describe()






# Class variables = SShared among all instances of a class 
# Defined outside the constructor 
# Allow you to share data among all objects created from that Class


# class Student:

#     class_year = 2025
#     numofstudents = 0 
#     # use class because it was already defined and not iterated as an instance

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.numofstudents += 1
    
# student1 = Student("Dylan", 16)
# student2 = Student("Duan", 20)
# student3 = Student("Typeshii", 22)
# student4 = Student("fiojf", 30)

# print(student1.name)
# print(student2.age)
# print(Student.class_year)

# print(f"my graduating class of {Student.class_year} has {Student.numofstudents} students")


# Inheritance = Allows a class to inherit attributes and methods from another class
# Helps with code reusablility and extensibility 
# class Child(Parent)


# class Animal:
#     def __init__(self, name):
#         self.name = name 
#         self.isalive = True
    
#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping ")
    

# class Dog(Animal):
#     def speak(self):
#         print("woof")

# class Cat(Animal):
#     def speak(self):
#         print("meow")

# class Mouse(Animal):
#     def speak(self):
#         print("squeek")


# dog = Dog("Scooby")
# cat = Cat("Garfeild")
# mouse = Mouse("Jerry")

# print(dog.name)
# print(dog.isalive)
# dog.eat()
# dog.sleep()
# dog.speak()

# Multiple inheritance = inherit from more than one parent class C(A,B)
# Multi Level INheritance = inherit from a parent which inherits from another parent C(B) <- B(A) <- A

# class Animal:
#     def __init__(self, name):
#         self.name = name


#     def eat(self):
#         print(f"This {self.name} is eating")

#     def sleep(self):
#         print(f"This {self.name} is sleeping")

# class Prey(Animal):
#     def flee(self):
#         print(f"this {self.name} is fleeing")
        
# class Predator(Animal):
#     def hunt(self):
#         print(f"this {self.name} is hunting")
# class Rabbit(Prey):
#     pass
# class Hawk(Predator):
#     pass
# class Fish(Prey, Predator):
#     pass

# rabbit = Rabbit("Tony")
# hawk = Hawk("LeBron")
# fish = Fish("Curry")

# rabbit.flee()
# hawk.hunt()
# fish.hunt()
# fish.flee()


# rabbit.eat()
# fish.sleep()





# Abstract class: A class that cannot be instantiated on its own; Meant to be subclassed 
# They can contain abstract methods, which are declared but have no implementation 
# 1. Prevents instatiation of the class itself 
# 2. Requires children to use inherited abstract methods 


# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass


# class Car(Vehicle):
#     def go(self):
#         print("you drive the car")

#     def stop(self):
#         print("you stop the car")
#         # define variables 

# class Motorcycle(Vehicle):
#     def go(self):
#         print("you ride the motorcycle")

#     def stop(self):
#         print("you stop the motorcyle")
#         # define variables 

# class Boat(Vehicle):
#     def go(self):
#         print("you drive the car")

#     def stop(self):
#         print("you stop the car")
#         # has to apply for both, it is extremely confusing 

# car = Car()

# car.go()

# boat = Boat()

# boat.stop()



# super() = Function used in a c hild class to call methods from a parent class (superclass). Allows you to extend the functionality fo the inherited methods 
# class Shape:
#     def __init__(self, color, filled):
#         self.color = color
#         self.filled = filled
    
#     def describe(self):
#         print(f"the color if {self.color} amd {'filled'if self.filled else 'not filled'}")

# class Circle(Shape):
#     def __init__(self, color, filled , radius):
#         super().__init__(color, filled)
#         self.radius = radius

#     def describe(self):
#         print(f"{self.color}")
#         super().describe()


# class Square(Shape):
#      def __init__(self, color, filled, width):
#         super().__init__(color, filled)
#         self.radius = width

#      def describe(self):
#         print(f"{self.color}")
#         super().describe()

# class Triangle(Shape):
#      def __init__(self, color, filled, width, height):
#         super().__init__(color, filled)
#         self.radius = width
#         self.height = height 

#      def describe(self):
#         # Method overriding
#         print(f"{self.color}")
#         super().describe()

# circle = Circle(color ="red", filled = True, radius = 5)

# square = Square(color ="blue", filled = True, width = 6)

# triangle = Triangle(color ="yellow", filled = False, width = 5, height = 6)

# print(circle.color)
# print(square.filled)
# print(f"{triangle.height}cm")

# circle.describe()




# Polymorphism = Greek word that means to "have many forms or faces" Poly = Many Morphe = Form 

# from abc import ABC, abstractmethod

# class Shape:

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self, side) -> None:
#         self.side = side

#     def area(self):
#         return self.side ** 2

# class Triangle(Shape):
#     def __init__(self, base, height) -> None:
#         self.base = base
#         self.height = height

#     def area(self):
#         return self.base * self.height * 0.5

# class Pizza(Circle):
#     def __init__(self, topping, radius):
#         self.topping = topping
#         super().__init__(radius)

# shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("peperoni", 15)]

# for shape in shapes:
#     print(f"{shape.area()} cm^2")






# Duck Typing = Another way to achieve polymorphism besides Inheritance/ Object must have the minimun necessary attributes/methods / "If it looks like a duck and quaks like a duck, it must be a duck"



# class Animal:
#     alive = True

# class Dog(Animal):
#     def speak(self):
#         print("Woof")

# class Cat(Animal):
#     def speak(self):
#         print("MEOW")

# class Car:
#     alive = False

#     def speak(self):
#         print("honk")

# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()

#     print(animal.alive)

#     # Has the minimum necessary attributes 
#     # Even if its different, if it has the same requirments, it would still be considered to be in the class 




# Aggregation = Repersents a relationship where one object (the whole )
# Contains references to one or more independent objects(the parts)

# class Libary:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.books = []
    
#     def add_book(self, book):
#         self.books.append(book)

#     def list_books(self):
#         return [f"{book.title} by {book.author}" for book in self.books]

# class Book:
#     def __init__(self, title, author) -> None:
#         self.title = title
#         self.author = author 


# libary = Libary("New York Public Libary")

# book1 = Book("Harry Potter", "Sukmi")
# book2 = Book("SUkdfn", "Dylan")
# book3 = Book("The giver", "Duan")

# # books are independent 

# libary.add_book(book1)
# libary.add_book(book2)
# libary.add_book(book3)

# print(libary.name)

# for book in libary.list_books():
#     print(book)




# Composition = The composed object directly owns its componenets, which cannot ecist independently "owns-a" relationship 


# class Engine():
#     def __init__(self, horse_power):
#         self.horse_power = horse_power

# class wheel():
#     def __init__(self, size):
#         self.size = size 

# class Car:
#     def __init__(self, make, model, horse_power, wheel_size):
#         self.make = make 
#         self.model = model
#         self.engine = Engine(horse_power)
#         self.wheels = [wheel(wheel_size) for _ in range(4)]

#     def display_car(self):
#         return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}"
    
# car1 = Car(make="Ford", model="Mustang", horse_power= 500, wheel_size= 18)

# print(car1.display_car())





# Nested Class = A class defined within another class 
# Class outer: 
    # Class Inner 

# Benifits: ALlows you to logically group classes that are closely related 
# Encapsulates private details that aren't relevant outside of the outer class 
# Keeps the namespace clean; reduces the possibility of naming conflicts 

# class Company:
#     class Employee:

#         def __init__(self, name, position):
#             self.name = name 
#             self.position = position
            
#         def get_details(self):
#             return f"{self.name} {self.position}"

#     def __init__(self, company_name):
#         self.company_name = company_name 
#         self.employees = []


#     def add_employee(self, name , position):
#         new_employee = self.Employee(name, position)
#         self.employees.append(new_employee)

#     def list_employees(self):
#         return [employee.get_details() for employee in self.employees]


# company = Company("Dylan Duan")
# company1 = Company("Chums Dylan")

# company.add_employee("Dylan", "Manager")
# company.add_employee("Duan", "Boss")
# company.add_employee("DD", "Killua")

# company1.add_employee("Dylan1", "Manager2")
# company1.add_employee("Duan1", "Boss2")
# company1.add_employee("DD1", "Killua2")

# for employee in company.list_employees():
#     print(employee)

# for employee in company1.list_employees():
#     print(employee)






# Static methods = A method that belong to a class rather than any object from that class (instance) Usally used for general utility 
# Instance methods = Best for operations on instances of classes (objects)
# Static methods = best for utility functions that do not need access to class data 

# class Employee:

#     def __init__(self, name, position):
#         self.name = name 
#         self.position = position

#     def get_info(self):
#         return f"{self.name} = {self.position}"
    
#     @staticmethod
#     def isvalidposition(position):
#         valid_positions = ["manager", "cashier", "cook"]
#         return position in valid_positions

# employee = Employee("Eugene", "manager")
# employee2 = Employee("Squidward", "cashier")
# employee3 = Employee("Dylan", "cook")
# # instance (object) method 

# print(Employee.isvalidposition("manager"))
# # Static method
# print(employee.get_info())



# Class method = allow operations related to class itself/ take (cls) as the first parameter, which repersents the class itself

# class Student:

#     count = 0 
#     total_gpa = 0

#     def __init__(self, name, gpa):
#         self.name = name 
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa

#     def getinfo(self):
#         return f"{self.name} {self.gpa}"
    
#     @classmethod
#     def defcount(cls):
#         return f"total amount of students: {cls.count}"
    
#     @classmethod
#     def averagegpa(cls):
#         if cls.count == 0:
#             return 0 
#         else: 
#             return f"the accumlated gpa for everysingle student is {cls.total_gpa / cls.count}"
    
# student1 = Student ("Spongebob", 4.0)
# student2 = Student ("Dylan", 4.0)
# student3 = Student ("Duan", 2.0)
    

# print(Student.defcount())
# print(Student.averagegpa())




# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
# They are automatically called by many python's built in operations. 
# They allow developers to define or customize the behaviouur of objects


# class Book:
#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self):
#         # Like the override method
#         return f"'{self.title}' by {self.author}"
    
#     def __eq__(self, other):
#         return self.title == other.title and self.author == other.author
    
#     def __lt__(self, other):
#         # less than
#         return self.num_pages < other.num_pages
    
#     def __gt__(self, other):
#         # less than
#         return self.num_pages > other.num_pages
    
#     def __add__(self, other):
#         return self.num_pages + other.num_pages
    
#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author
    
#     def __getitem__(self, key):
#         if key == "title":
#             return self.title
#         elif key == "author":
#             return self.author
        
#         elif key == "num_pages":
#             return self.num_pages
#         else:
#             return f"Key {key} was not found"
        
        


# book1 = Book("The Hobbit", "J.R,.R", 310)
# book2 = Book("The Hobbit", "J.R,.R", 320)
# book3 = Book("The bobit", "Sig", 3234)
# print(book1 == book2)
# print(book2 + book3)

# # finding smth

# print("bobit" in book3)

# # title

# print(book1['title'])
# print(book1['author'])
# print(book1['num_pages'])
# print(book1['audio'])





# # @property = Decorator used to define a mtheod as a propertu (it can be accessed like an atribute ) 
# # benifits: add additiobnal logic when read, write or delete attributes 
# # Gives you getter, setter and deleter methods 



# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width  
#         self._height = height

# # getter methods
#     @property
#     def width(self):
#         return f"{self._width:.1f} cm"

#     @property
#     def height(self):
#         return f"{self._height:.1f} cm"
    
#     # setter methods

#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
        
#         else:
#             print("Width > 0")

#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._hieght = new_height
        
#         else:
#             print("Height > 0")

#     # deleter method

#     @width.deleter
#     def width(self):
#         del self._width
#         print("Width has been deleted")

#     @height.deleter 
#     def height(self):
#         del self._height
#         print("Height has been deleted")


# rectangle = Rectangle(3, 4)

# rectangle.width = 5

# del rectangle.width
# del rectangle.height








# Decorator = Function that extends the behavior of another cunction w/o modifying the base function
# pass the base function as an argument

# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("you added sprinkles")
#         func(*args, **kwargs)
#     return wrapper

# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("you added fudge")
#         func(*args, **kwargs)
#     return wrapper

# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#     print(f"here is your {flavor} ice cream")

# get_ice_cream("vanilla")


# Lamada functions = A small anonymous fucntion for a one time use (throw away function), they take any numebr fo arguments but have only 1 extression. It helps keep the namespace clean like "sort()" or "map() " or "filter()" or "reduce()"
    
# double = lamdba x: x * 2

# print(double(4))




# map(function, collection) = Applies a given fuynction to all items in a collection 

# def c_to_f(temp):
#     return (temp * 9/5) + 32
# normal function

# celsius_temps = [0.0, 1, 2, 3.6]

# fahrenheit_temps = map(lambda temp: (temp * 9/5), celsius_temps)

# lambda (random functiion)

# for temp in fahrenheit_temps:
#     print(temp)



# filter(function, collection) = return all elements that pass a condition

# def is_passing(grade):
#     return grade >= 69


# grades = [91, 32, 83, 44, 75, 56, 67]


# # passing_grades = filter(is_passing, grades)

# passing_grades = list(filter(lambda grade: grade >= 60, grades))


# for grade in passing_grades:
#     print(grade)