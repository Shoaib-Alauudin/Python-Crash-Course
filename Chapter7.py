# user_input = ""
# while user_input != 'quit':
#     user_input = input("Please enter what ever you like : ")
#     if user_input != 'quit':
#         print((user_input))
#
#
# unconfirmed_users = ['alice','brain','candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     confirmed_users.append(current_user)
#
# for confirmed_user in confirmed_users:
#     print("Verifying user: "+confirmed_user.title())
#
#
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)
#
# responses = {}
# polling_active = True
# while polling_active:
#     name = input("Please Enter Your Name : ")
#     response = input("Which mountain would you like to climb someday? ")
#
#     # Store the response in the dictionary
#     responses[name] = response
#
#     # Find out if anyone else is going to take the poll.
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#
#     if repeat == ('no' or 'No' or 'NO' or 'nO'):
#         polling_active = False
#
#
#
# # Polling is complete. Show the results.
# print("\n ---Poll Results--- ")
# for Name, Response in responses.items():
#     print(Name+" Would like to climb "+Response+".")
#
# # 7-8. Deli:
# Sandwich_orders = ['Grilled Cheese sandwich','Turkey sandwich','Egg Sandwich','Beef sandwich','Tuna sandwich','Butter Sandwich','Steak Sandwich','Cumcumber Sandwich','Vegatable Sandwich','Buffalo Sandwich','Fish Sandwich','Pastrami Sandwich','Pastrami Sandwich','Pastrami Sandwich']
# finished_sandwichs = []
# while Sandwich_orders:
#     current_order = Sandwich_orders.pop()
#     finished_sandwichs.append(current_order)
# print(finished_sandwichs)
#
#
# # 7-9. No Pastrami:
# while 'Pastrami Sandwich' in finished_sandwichs:
#     finished_sandwichs.remove('Pastrami Sandwich')
# print(finished_sandwichs)

# 7-10. Dream Vacation:
poll_results = []
user_input = ""
while user_input != 'No':
    place = input("If you could visit one place in the world, Where would you go? ")
    user_input = input("Do you want to poll again? (Yes/No) ")
    poll_results.append(place)
print(poll_results)