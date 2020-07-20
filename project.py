with open("currency.txt") as f:
    lines = f.readlines()

currencydict = {}
for line in lines:
    parsed = line.split("\t")
    currencydict[parsed[0]] = parsed[1]

amount = int(input("Enter amount:\n"))
print("Enter the name of the currency you want to convert  this amount to:\n Available options\n")
[print(item) for item in currencydict.keys()]
currency = input("Enter one of these currencies:\n")
print(f"{amount} INR  is equal to {amount * float(currencydict[currency])} {currency}") 