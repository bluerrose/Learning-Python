#Arcade Day Pass Tracker Challenge
#1)Create variables to store:
# customer name
#number of passes
#tokens per pass
#price per pass
#tokens requiured per game

#2)calculate total tokens
#total tokens
#total cost
#games available (use floor division to get a whole number)

#3)Print a summary with 
#customer name
#passes bought
#total tokens
#total cost
#games available

customer_name = 'Michael'
number_of_passes = 10
tokens_per_pass = 20
price_per_pass = 5.00
tokens_per_game = 4

total_tokens = number_of_passes * tokens_per_pass
total_cost = number_of_passes * price_per_pass
games_available = total_tokens // tokens_per_game

#print('Thank you for choosing Wicked Arcade Michael! You have purchased ' + str(number_of_passes) + ' passes for a total of ' + str(total_tokens) + ' tokens. Your total number of playable games are ' + str(games_available) + ' and your total cost is $' + str(total_cost) +'. Thank you!')
#This was my original code but I was unsatisfed that the total cost returned as "$50.0" instead of "$50.00". I plugged it into an Ai and explained my issue.
#Using the Ai introduced me to f-string formatting. Although it is new to me I find the f-string formatting to be a lot cleaner and easier to read. It also makes more sense and I'm excited to learn more about them. 
#Thanks for reading my code and I hope you have a great day :).

print(f'Thank you for choosing Wicked Arcade Michael! You have purchased {number_of_passes} passes for a total of {total_tokens} tokens. Your total number of playable games are {games_available} and your total cost is ${total_cost:.2f}. Thank you!')
