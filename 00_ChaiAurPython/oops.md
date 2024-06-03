# class
class name are usualyy in caps
class Car:
    #self is like a context like which object called it
    def __init__(self,brand,model): # init is constructor 
        self.brand=brand # the right one is from object and left one is the class variable
        self.model=model
    
    def full_name(self):
        return f"{self.brand} and {self.model}"


my_car=Car("mercedes","suv") ->object
print(my_car.brand)
print(my_car.full_name())
my_new_car=Car("tata","roll")

now here we have two object mycar and mynewcar so to know which one is calling the class we have the self statement or the context


# inheritance

class Car:
    def __init__(self,brand,model): 
        self.brand=brand
        self.model=model
    
    def full_name(self):
        return f"{self.brand} and {self.model}"
class ElectricCar(Car): -> way to write inheritance
    def __init__(self,brand,model,batterysize):
        super().__init__(brand,model) ->here super mean go to up class init to access it and pass the brand and model
        self.batterysize=batterysize

mytesla=ElectricCar("tesla","models","84kmph")
print(mytesla.full_name()) ->yes it has the access of fullname from the parent class

# Encapsulation
like in above if we want to access the brand we can directly do it . but what we want is not to have direct access to it

class Car:
    def __init__(self,brand,model): 
        self.__brand=brand
        self.model=model
    def get_brand(self):
        return self.__brand

myob=Car("tenzin","delek")
print(myob.get_brand())->we have the access of brand here

print(myob.__brand)->here now we dont have direct access to it

- the __ is used for making the vairble private (so it can be access inside the class but not outside of it)

so to get access to it we write method 
thats concept of enacpsulate

# polymorphism
- like the operator + is a example of it as it add number and also for string it act like a concatenate method

class Car:
    def __init__(self,brand,model): 
        self.brand=brand
        self.model=model

    def fuel_type(self):
        return "Petrol or diesel"
    
class EelctricCar:
    def fuel_type(self):
        return "electric charges"

tesla= ElectricCar()
print(tesla.feul_type())

mercede=Car("tata","w12")
print(mercede.feul_type())

same fucnction name but dif work

# static method - method that are accessable to the class but not to the object
class Car:
    @staticmethod ->to make the functionstatic
    def description(): -> we remove self as object shoudnt access it
        print("yoo")

tesla= Car()
print(Car.description()) ->only class can access it

# so these @staticmethod are call decorators
- enhance method functionality


# property decorators

class Car:
    def __init__(self,brand,model): 
        self.__brand=brand
        self.__model=model # __ makes private
    @property ->datamember accessable through function and also it cant be overwrite
    def model(self):
        return self.__model
mycar=Car("tata","safari")
mycar.model="city"
print(mycar.model)
it changes to city but we want to make model read only
so we make the data member private and make it accesable only through function

# multiple inheritance

class Battery:
    def battryinfo(self):
        return "yoo"
class Engine:
    def engineinfo(self):
        return "yoo1"
class ElectricCar(Battery,Engine):
    pass

myob=ElectricCar() 
print(myob.engineinfo()) -> it hass access to it
print(myob.battryinfo())
