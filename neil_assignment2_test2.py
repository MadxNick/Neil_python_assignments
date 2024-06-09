# a cashier has a currency note of denomination 10,50,100. if the amount to be withdrawn is the input through keyboard (in multiple of ten and maximum 990) find the total no of currency notes of each denomination the cashier will have to be given to the withdrawer
amount = int(input("Enter the amount to be withdrawn (in multiples of 10 and maximum 990): "))
def notes(amount):
    count = {'100': 0, '50': 0, '10': 0}
    if amount % 10 != 0 or amount > 990:
        return "Invalid amount"
    count['100'] = int(amount/100)
    amount %= 100
    count['50'] = int(amount/50)
    amount %= 50
    count['10'] = int(amount/10)
    return count
print("Total number of currency notes:")
print(notes(amount))



