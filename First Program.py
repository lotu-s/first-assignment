# Jacky Le
# Computer Studies 10
# May 10 2021
# A chatbot that asks a question, reads your answer, and replies with a random response.

import random

#Question 1
myinput = input("What games do you enjoy playing?")
response_list = ["I've never tried that game before, you should show me it!", "I played that game before but didn't enjoy it personally.", "That game is really fun, I play it too!"]
print(random.choice(response_list))

#Question 2
#Added time delay due to responding too fast and messes up where the text is placed

import time

time.sleep(0.5)
myinput = input("What's your favourite hobby?")
response_list = ["That sounds pretty cool, I want to try that.", "That's my favourite too!", "Ahh, I don't really enjoy that but to each their own."]
print(random.choice(response_list))

#Question 3
time.sleep(0.5)
myinput = input("Who is your favourite legend in Apex Legends?")
response_list = ["Oh they're my favourite too!", "Eww, I hate that Legend", "They're cool, but I prefer someone else"]
print(random.choice(response_list))

#Question 4
time.sleep(0.5)
myinput = input("Do you want to do anything today with some friends?")
response_list = ["Sounds like a plan.", "Can we do something else?", "That's fine with me!"]
print(random.choice(response_list))

