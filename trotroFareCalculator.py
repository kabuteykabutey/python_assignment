passenger_route= input("Enter the passenger route: ")
total_passengers= int(input("Enter the total number of passengers boarding the trotro: "))
Fare = 0
if passenger_route =="madina":
    Fare = 5
elif passenger_route =="kasoa":
    Fare = 10
elif passenger_route =="Tema":
    Fare = 8
    print(passenger_route, Fare)
total_fare_to_be_paid = total_passengers * Fare
print("The total fare to be paid by all the customers is:GHS ",total_fare_to_be_paid)

