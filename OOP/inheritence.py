class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

class BMW(Car):
    def __init__(self, model, year, price):
        super().__init__(model, year,)
        self.price = price
    
    def result(self):
        print(f"Car name is {self.model} publish in{self.year} & the price is{self.price}")
        
b1 = Car("Bmw12", 2012, 20000)
b1.result()
            