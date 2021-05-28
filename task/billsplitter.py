# write your code here
import random

guests_dict = {}
print("Enter the number of friends joining (including you):")
guests = int(input())

if guests < 1:
    print("No one is joining for the party")
else:

    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(guests):
        guest = input()
        guests_dict[guest] = 0

    print("Enter the total bill value:")
    bill = int(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky = input()

    if lucky == 'Yes':
        names = list(guests_dict.keys())
        random_int = random.randint(0, len(names) - 1)
        print(f"{names[random_int]} is the lucky one!")
        bill_individual = round(bill / (guests - 1), 2)
        for key, value in guests_dict.items():
            guests_dict[key] = bill_individual
        # update for lucky
        guests_dict[names[random_int]] = 0
    else:
        print("No one is going to be lucky")
        bill_individual = round(bill / guests, 2)
        for key, value in guests_dict.items():
            guests_dict[key] = bill_individual

    print('\n' + str(guests_dict))
