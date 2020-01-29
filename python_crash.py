# 9.4 Number Served


# 9.3 Users
# class User:
# 	def __init__(self, first_name, last_name, age, gender):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.age = age
# 		self.gender = gender

# 	def describe_user(self):
# 		print(f"{self.first_name} {self.last_name} is a {self.gender} and is {self.age} years old.")

# 	def greet_user(self):
# 		print(f"Hello {self.first_name}!")

# justin = User("Justin", "Shotwell", 41, "Male")
# justin.describe_user()
# justin.greet_user()

# 9.2 Three Restaurants
# class Restaurant:
# 	""" A simple attempt to represent a restaurant """

# 	def __init__(self, restaurant_name, cuisine_type):
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type

# 	def describe_restaurant(self):
# 		print(f"{self.restaurant_name} serves {self.cuisine_type}!")

# 	def open_restaurant(self):
# 		print(f'{self.restaurant_name} is open!')

# mcdonalds = Restaurant("McDonald's", "Burgers")
# mcdonalds.describe_restaurant()

# taco_bell = Restaurant("Taco Bell", "Tacos")
# taco_bell.describe_restaurant()

# jimmy_johns = Restaurant("Jimmy John's", "Sandwiches")
# jimmy_johns.describe_restaurant()



# 9.1 Restaurant
# class Restaurant:
# 	""" A simple attempt to represent a restaurant """

# 	def __init__(self, restaurant_name, cuisine_type):
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type

# 	def describe_restaurant(self):
# 		print(self.restaurant_name)
# 		print(self.cuisine_type)

# 	def open_restaurant(self):
# 		print(f'{self.restaurant_name} is open!')

# restaurant = Restaurant('Mcdonalds', 'Burgers')

# restaurant.describe_restaurant()
# restaurant.open_restaurant()


# 7.5 Movie Tickets
# age = int(input('How old are you? '))
# if age < 3:
# 	cost = 0
# elif age < 12:
# 	cost = 10 
# else:
# 	cost = 15

# print(f'Your ticket will cost ${cost}.')

# 7.4 Pizza Toppings
# active = True
# while active:
# 	topping = input("What topping would you like? ")
# 	if topping == "quit":
# 		active = False
# 		print('The pizza will be ready in thirty minutes.')
# 	else:
# 		print(f'I will add {topping} to your pizza.')

# 7.3 Multiples of Ten
# number = input('Please provide a number: ')
# if int(number) % 10 == 0:
# 	print('Your number is divisible by 10.')
# else:
# 	print('Your number is not divisible by ten.')

# 7.2 Restaurant Seating
# guests = input('How many people are in your party? ')
# if int(guests) > 8:
# 	print('You will have to wait.')
# else:
# 	print('Your table is ready.')

# 7.1 Rental Car
# car = input('What kind of rental car would you like?')
# print(f'Let me see if I can find you a {car}.')

# 6.11 Cities
# cities = {
#     'santiago': {
#         'country': 'chile',
#         'population': 6158080,
#         'nearby mountains': 'andes',
#         },
#     'talkeetna': {
#         'country': 'alaska',
#         'population': 876,
#         'nearby mountains': 'alaska range',
#         },
#     'kathmandu': {
#         'country': 'nepal',
#         'population': 1003285,
#         'nearby mountains': 'himilaya',
#         }
#     }

# for city, city_info in cities.items():
#     country = city_info['country'].title()
#     population = city_info['population']
#     mountains = city_info['nearby mountains'].title()

#     print("\n" + city.title() + " is in " + country + ".")
#     print("  It has a population of about " + str(population) + ".")
#     print("  The " + mountains + " mountains are nearby.")


# 6.10 Favorite Numbers
# fav_numbers = {
# 	'Justin': [41,24],
# 	'Beth': [35,21],
# 	'Richard': [33,2]
# }

# for key, values in fav_numbers.items():
# 	print(f"{key}'s favorite numbers are:")
# 	for value in values:
# 		print(value)

# 6.9 Favorite Places
# favorite_places = {
# 	'Justin': ['Munich', 'Paris', 'Salzburg'],
# 	'Beth': ['Lisbon','London','Corviero']
# }

# for key, values in favorite_places.items():
# 	print(f"{key}'s favorite places are:")
# 	for value in values:
# 		print('\t' + value)

# 6.8 Pets
# pets = [
# {
# 	'pet_name': 'Stevie',
# 	'owner': 'Justin'
# },
# {
# 	'pet_name': 'Shirley',
# 	'owner': 'Beth'
# }
# ]

# for pet in pets:
# 	name = pet['pet_name']
# 	owner = pet['owner']

# 	print(f'{name} is owned by {owner}')


# 6.7 People
# people = [{
# 	'first_name': 'Justin',
# 	'last_name': 'Shotwell',
# 	'age': '41',
# 	'city': 'Oak Park'
# },
# {
# 	'first_name': 'Elizabeth',
# 	'last_name': 'Priddy',
# 	'age': '35',
# 	'city': 'Oak Park'
# },
# {
# 	'first_name': 'Richard',
# 	'last_name': 'Voss',
# 	'age': '33',
# 	'city': 'San Diego'
# }]

# for person in people:
#     name = person['first_name'].title() + " " + person['last_name'].title()
#     age = str(person['age'])
#     city = person['city'].title()
    
#     print(name + ", of " + city + ", is " + age + " years old.")

# 6.6 Polling
# teams = {
# 	'Cubs': 'Chicago',
# 	'Braves': '',
# 	'Tigers': 'Detroit'
# }

# for k,v in teams.items():
# 	if v == '':
# 		print(f'Hey {k}, what town are you from?')
# 	else:
# 		print(f'The {k} are located in {v}.')

# 6.5 Rivers
# rivers = {
# 	'Nile': 'Egypt',
# 	'Thames': 'England'
# }

# for k,v in rivers.items():
# 	print(f'The {k} runs through {v}.')

# for k in rivers.keys():
# 	print(k)

# for v in rivers.values():
# 	print(v)

# 6.4 Glossary 2
# teams = {
# 	'Cubs': 'Chicago',
# 	'Braves': 'Atlanta',
# 	'Tigers': 'Detroit',
# 	'Twins': 'Minnesota',
# 	'Royals': 'Kansas City'
# }

# for k, v in teams.items():
# 	print(f'The {k} are located in {v}.')

# 6.3 Glossary
# teams = {
# 	'Cubs': 'Chicago',
# 	'Braves': 'Atlanta',
# 	'Tigers': 'Detroit'
# }

# for k, v in teams.items():
# 	print(f'The {k} are located in {v}.')


# 6.2 Favorite Numbers
# fav_numbers = {
# 	'Justin': 41,
# 	'Beth': 35,
# 	'Richard': 33
# }

# for key in fav_numbers:
# 	print(key, 'is', fav_numbers[key], 'years old.')


# 6.1 Person
# person = {
# 	'first_name': 'Justin',
# 	'last_name': 'Shotwell',
# 	'age': '41',
# 	'city': 'Oak Park'
# }

# for value in person:
# 	temp = person[value]
# 	print(temp)


# 5.11 Ordinal Numbers
# numbers = list(range(1,10))

# for number in numbers:
#     if number == 1:
#         print("1st")
#     elif number == 2:
#         print("2nd")
#     elif number == 3:
#         print("3rd")
#     else:
#         print(str(number) + "th")


# 5.10 Checking Usernames
# current_users = ["Adam", "Richard", "Justin", "Beth", "Tommy", "John"]
# new_users = ["Kathryn", "James", "Justin", "Ella", "Claire", "JOHN"]
# current_users_lower = [x.lower() for x in current_users]

# for user in new_users:
# 	if user.lower() in current_users_lower:
# 		print("You will need to enter a new username.")
# 	else:
# 		print("The username is available.")

# 5.9 No Users
# users = []
# if users:
# 	print("Something")
# else:
# 	print("We need to find some users!")

# 5.8 Hello, admin
# users = ["admin", "Justin", "Beth"]
# for user in users:
# 	if user == "admin":
# 		print("Hello Admin, would you like a status report?")
# 	else:
# 		print(f"Hello {user}, thank you for loggin in again.")

# 4.9 Cube Comprehension
# cubes = [cube**3 for cube in range(1,11)]
# print(cubes)

# 4.8 Cubes
# cubes = list(range(1,11))
# for cube in cubes:
# 	print(cube**3)

# 4.7 Threes
# threes = list(range(3,31,3))
# for three in threes:
# 	print(three)

# 4.6 Odd Numbers
# odd = list(range(1,20,2))
# for value in odd:
# 	print(value)

# 4.5 Summing a Million
# million = list(range(1,1000001))
# print(min(million))
# print(max(million))
# print(sum(million))

# 4.4 One Million
# million = list(range(1,1000001))
# for value in million:
	 # print(value)

# 4.3 Counting to Twenty
# print(list(range(1,21)))
