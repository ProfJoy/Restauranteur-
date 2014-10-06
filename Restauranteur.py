#Developed by Abey Joy
#The following are a set of functions that solve many common issues that restaurant diners encounter.
#In no way am I to be held responsible for any damages caused by usage of these functions,

import random

#Purpose: calc_tip calculates the tip amount based on the users input, and outputs the amount to tip, as well as the new meal total.
#Parameters: calc_tip takes no paramteers.
#Returns: calc_tip returns a double, the tip amount.
def calc_tip():
    meal_total = float(input("What is the total cost of your meal?"))
    tip_perc = float(input("What percentage would you like to tip?"))
    if tip_perc < 1: #User entered the percentage as a decimal
       tip_amount = meal_total * (tip_perc)
    elif tip_perc >= 1: #User entered the percentage as an integer
        tip_amount = meal_total * (tip_perc / 100)
    print ("You should tip: ", tip_amount)
    print ("In total, your meal comes out to: " , tip_amount + meal_total)
    return tip_amount 

#Purpose: split_meal is a function which helps one figure out how much they need to pay based on what they ordered, the tax, and the tip.
#Parameters: split_meal takes no parameters.
#Returns: split_meal does not return anything, instead it prints diner's names and how much they should pay
def split_meal():
    print("Hello everyone, I will help you each and every one of you figure out just how much you need to pay!")
    meal_total = float(input("What is the total cost of everyone's meal, not including tax?"))
    tax = float(input("How much was the tax on the meal?"))
    tip_perc = float(input("What percentage would you like to tip?"))
    if tip_perc < 1: #User entered the percentage as a decimal
       tip_amount = meal_total * (tip_perc)
    elif tip_perc >= 1: #User entered the percentage as an integer
        tip_amount = meal_total * (tip_perc / 100)
    total_people = int(input("How many people are splitting the bill?"))
    
    #INITIALIZERS
    people_counter = 0
    orderers = []
    orders = []
    order_total = 0
    looper = "START"
    #INITIALIZERS
    
    while people_counter < total_people:
        name = input("What is your name?")
        orderers.append(name)
        print("Hello",name)
        while looper != 0:
            looper = float(input("Enter the cost of each dish you ordered individually, when you are finished enter '0':"))
            order_total += looper
            
        #REINITIALIZE
        orders.append(order_total)
        order_total = 0
        looper = "START"
        people_counter = people_counter + 1
        #REINITIALIZE
        
    while orderers != []:
        print(orderers.pop(), ", you should pay: ",orders.pop() + (tax/total_people) + (tip_amount/total_people))
        
#Purpose: who_pays is a function that takes no parameters, but takes in the names of everyone who is willing to pay and randomly selects one person to pay.
#Parameters: who_pays does not take any parameters
#Returns: who_pays does not return anything, instead it prints out the diner selected randomly to pay the bill
def who_pays():
    contenders = []
    entry = ''
    while entry != "Stop":
        entry = input("Enter the names of everyone who would like to pay, when you are finished, enter 'Stop'")
        contenders.append(entry)
    winner = random.randint(0,(len(contenders)-1))
    print("Congratulations, ", contenders[winner], ". You get to pay!")                         

