
# def chai(n):
#     print(n)

# chai("bodja")

# chai_one="masala tea"
# chai_two="butter tea"

class Battery:
    def battryinfo(self):
        return "yoo"
class Engine:
    def engineinfo(self):
        return "yoo1"
class ElectricCar(Battery,Engine):
    pass

myob=ElectricCar() 
print(myob.engineinfo())
print(myob.battryinfo())