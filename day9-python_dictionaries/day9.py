#DICTIONARIES = OBJECT
#{key: value}

programming_dictionary = {
    "bug" :"an error", 
    "function" : "piece of code",
}

#find a key
# print(programming_dictionary["bug"])

#Adding a new entry
# programming_dictionary["loop"] = "doing something over and over"
# print(programming_dictionary)

#Create empty dictionary
#empty_dictionary = {}

#wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit item in dictionary
# programming_dictionary["bug"] = "an error in runtime"
# print(programming_dictionary["bug"])

#Loop through dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

#GRADING PROGRAM
# student_scores = {
#     "Harry" : 81,
#     "Ron" : 78,
#     "Hermione" : 99,
#     "Draco" : 74,
#     "Neville" : 62,
# }

# student_grades = {}

# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
# print(student_grades)



#NESTING
# capitals = {
#     "France" : "Paris",
#     "Germany" : "Berlin"
# }

# #Nesting list in a dictionary
# travel_log = {
#     "France": ["Toulouse", "Lille", "Saint-gaudens"]
# }

#Nesting dictionary in dictionary
# travel_log = {
#     "France": {"cities_visited" : ["Toulouse", "Lille", "Saint-gaudens"], 
#                "total_visits" : 24},
#     "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
#                 "total_visits" : 10}
# }

#Nesting Dictionary in list
# travel_log = [
#     {
#         "country" :"France",
#         "cities_visited" : ["Toulouse", "Lille", "Saint-gaudens"],
#         "total_visits" : 24
#     },
#     {
#         "country": "Germany",
#         "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits" : 10
#     }
# ]


#CHALLENGE DICTIONARY LIST
# travel_log = [
#     {
#         "country" :"France",
#         "cities_visited" : ["Toulouse", "Lille", "Saint-gaudens"],
#         "total_visits" : 24
#     },
#     {
#         "country": "Germany",
#         "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits" : 10
#     }
# ]

# country = input("Which country did you visit?")
# nbr_times = int(input("How many times did you go there"))
# city_list = ["Sao Paulo", "Rio de Janeiro"]

# def add_new_country(country, visits, cities):
#     new_city = {}
#     new_city["country"] = country
#     new_city["total_visits"] = visits
#     new_city["cities_visited"] = cities

#     travel_log.append(new_city)
#     print(f"I've been to {travel_log[2]["country"]} {travel_log[2]["total_visits"]} times. My favourite city was {travel_log[2]["cities_visited"][0]}")

# add_new_country(country, nbr_times, city_list)


#BLIND AUCTION PROGRAM
bidder_dictionary = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print (f"The winner is {winner} with a bid of {highest_bid} ")


while not bidding_finished:
    name = input("What is your name?\n")
    bid = int(input("How much do you want to bid?\n"))
    bidder_dictionary[name] = bid

    should_continue = input("Is there another bidder? type Yes or No\n").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bidder_dictionary)
