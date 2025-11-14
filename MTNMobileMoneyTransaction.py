Transactional_amount = int(input("How much do you wish to transact?: "))
amount = Transactional_amount
if amount <= 100:
     charge = 2
elif amount >100 and amount <= 500:
    charge = 5
elif amount >500 :
    charge = 10
print (f'i believe the amount you want to transact is GHS{Transactional_amount}\n'
       ,"Also the charge for that amount is: GHS",charge)