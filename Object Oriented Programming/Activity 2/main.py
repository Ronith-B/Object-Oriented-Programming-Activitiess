class Vehicle:
    def __init__(self,max_speed,mileage):

        self.max_speed = max_speed
        self.mileage = mileage

modelY = Vehicle(195,250)

print('Model Max Speed:', modelY.max_speed)
print('Model Mileage:' , modelY.mileage )