budget = int(input())
product = input()

while product != "End":

    product = int(product)
    budget -= product
    if budget < 0:
        print(f"You went in overdraft!")
        break
    product = input()

else:
    print("You bought everything needed.")
