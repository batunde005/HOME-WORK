
card_user = input(" Select card type 1.Regular, 2.Silver, 3.Gold, 4.Platinum")
user_card1 = "R"
user_card2 = "S"
user_card3 = "G"
user_card4 = "p"
total_cost = int(input(" Enter the cost of the Product: "))
discount = 0
if card_user == "R":
    if total_cost > 2000:
        discount = 10
    elif total_cost > 1000:
        discount = 5
    else:
        discount = discount

elif card_user == "S":
    discount = 5
    if total_cost > 2000:
        discount = discount + 10
        
    elif total_cost > 1000:
            discount = discount + 5
    else:
            discount = discount

    if card_user == "G":
        if total_cost > 2000:
            discount = discount + 10
        elif total_cost > 1000:
            discount = discount + 5
        else:
            discount = discount
          
    if card_user == "P":
        if total_cost > 2000:
            discount = discount + 10
        elif total_cost > 1000:
            discount = discount + 5
        else:
            discount = discount
    amount_user_will_pay = total_cost - (discout/100)
    print(amount_user_will_pay)




