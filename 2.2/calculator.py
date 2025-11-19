"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""

# Final Exam Calculator
# Sept 22
# Steven Zhang

# Calculates what grade you must get on the final to get your desired grade

desired = int(input("What is your desired grade? (Percent)\n").strip(" .%!?"))
current = int(input("What is your current grade? (Percent)\n").strip(" .%!?"))
finalWeight = int(input("What is the weight of your final exam? (out of 100)\n").strip(" .%!?"))

required = (100*desired-current*(100-finalWeight))/finalWeight
print("You will need to score a "+str(required)+"%.")