# write your code here
import random

print("Enter the number of friends joining (including you):")
friends_num = int(input())

if friends_num <= 0:
    print("No one is joining for the party")

else:

    print("Enter the name of every friend (including you), each on a new line:")
    friends_names = {}
    for i in range(friends_num):
        friends_names[input()] = 0

    # input the total bill value
    print("Enter the total bill value:")
    bill_value = float(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_feature=input()

    if lucky_feature == "No":
        print("No one is going to be lucky")
        try:
            individual_bill_value = round(bill_value / friends_num, 2)
        except Exception:
            print("No one is joining for the party")
        else:
            for item in friends_names:
                friends_names[item] = individual_bill_value
            print(friends_names)

    if lucky_feature == "Yes":
        lucky_guy = random.choice(list(friends_names.keys()))
        print(f"{lucky_guy} is the lucky one!")
        try:
            individual_bill_value = round(bill_value / (friends_num-1), 2)
        except Exception:
            print("No one is joining for the party")
        else:
            for item in friends_names:
                friends_names[item] = individual_bill_value
            # bill for the lucky one
            friends_names[lucky_guy] = 0
            print(friends_names)
