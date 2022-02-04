def saving_rate(expense, income):
    deposit = expense - income 
    result = ((deposit*100)/expense)
    print("Your Monthly Saving Rate {:.2f}%".format(result))

    if result >= 25:
        print("Good")
    elif result >= 20 and result <= 24:
        print("Better")
    elif result >=15 and result <= 19:
        print("Not Bad")
    elif result >=10 and result <= 14:
        print("Satisfactory")
    elif result < 10:
        print("Not Satisfactory")



saving_rate(11,15)