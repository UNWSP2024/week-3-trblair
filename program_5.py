# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
def hotdogpurchase():
    subtotal = 0
    hotdog=input("What type of hotdog would you like?\n\t1.Hot Dog $3.50\n\t2.Chili Dog $4.50\n").lower
    if hotdog == "1" or "hot dog" or "hotdog":
        subtotal=3.5
    elif hotdog == "2" or "chili dog" or "chilidog":
        subtotal=4.5
    toppingz=input("Would you like toppings? y/n\n")
    if toppingz == "y":
        question=input("Please select a topping from the list:\n\t1.Grilled Onions $1\n\t2.Peppers $0.75\n\t3.Cheese $0.50\n").lower
        if question == "1" or "grilled onions" or "grilledonions":
            subtotal = subtotal+1
            print("Your subtotal is ",subtotal)
            print("Your taxes are equal to ",subtotal*0.07)
            print("Your total is ",subtotal+subtotal*0.07)
        elif question == "2" or "peppers":
            subtotal = subtotal+0.75
            print("Your subtotal is ",subtotal)
            print("Your taxes are equal to ",subtotal*0.07)
            print("Your total is ",subtotal+subtotal*0.07)
        elif question == "3" or "cheese":
            subtotal = subtotal+0.5
            print("Your subtotal is ",subtotal)
            print("Your taxes are equal to ",subtotal*0.07)
            print("Your total is ",subtotal+subtotal*0.07)
        else:
            print("Invalid Input, please try again")
    elif toppingz == "n":
        print("Your subtotal is ",subtotal)
        print("Your taxes are equal to ",subtotal*0.07)
        print("Your total is ",subtotal+subtotal*0.07)
    else:
        print("Invalid Input, please try again")
hotdogpurchase()
