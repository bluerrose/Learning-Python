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

print(f'Thank you for choosing Wicked Arcade Michael! You have purchased {number_of_passes} passes for a total of {total_tokens} tokens. Your total number of playable games are {games_available} and your total cost is ${total_cost:.2f}. Thank you!')
