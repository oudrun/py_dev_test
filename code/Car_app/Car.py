class Car:
    
    amount_cars = 0
    
    def __init__(self, manufacturer, model, hp):
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp
        Car.amount_cars += 1


    def __del__(self):
        print("Object gets deleted!")
    
    
    def print_car_amount(self):
        print("Amount: {}"
                .format(Car.amount_cars))

    
    def print_info(self):
        print("Manufacturer: {}, Model: {}, HP: {}"
            .format(self.manufacturer,
                    self.model,
                    self.hp))

myCar1 = Car("Tesla", "Model X", 525)

myCar1.print_info()
myCar1.print_car_amount()

#Directly access Car attributes
print(myCar1.manufacturer)
print(myCar1.model)
print(myCar1.hp)

myCar2 = Car("BMW", "X3", 200)
myCar3 = Car("VW", "Golf","100")
myCar4 = Car("Porche","911",520)

#Delete object manually
del myCar3





    
