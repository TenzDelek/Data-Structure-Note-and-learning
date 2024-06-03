# from tenzin import chai

# chai("butter milk") #when you run this the __pycache__ file is generated

# n=100
# func=int(f'{n}',2)
# print(func)

class Car:
    def __init__(self,brand,model): 
        self.brand=brand
        self.model=model

    def feul_type(self):
        return "Petrol or diesel"
    
class ElectricCar(Car):
    def feul_type(self):
        return "electric charges"

tesla= ElectricCar("tenzin","delek")
print(tesla.feul_type())
print(tesla.model)
mercede=Car("tata","w12")
print(mercede.feul_type())