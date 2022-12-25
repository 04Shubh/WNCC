import random

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"



class Bus(Vehicle):
    name = 'bus_1'
    mileage = '10'
    max_speed = '60'
    sit_cap = 25
    stand_cap = 15
    is_stand = False
    is_sit = False
    stand_count = 0
    sit_count = 0

class Car(Vehicle):
    name = 'car_name'
    max_speed = 80
    mileage = 15
    sit_cap = 5
    sit_count = 0
    ID = ['a','b','c','d','e']

Car1 = Car('BMW',80,15)
#Car1.name = 'car_a'

Car2 = Car('AUDI',80,15)
#Car2.name = 'car_b'
Car2.ID = ['A','B','C','D','E']

Bus1 = Bus('bus_1',60,10)

user_in = input('what you want to ride on?')

if(user_in =='A'):
    if(Car1.sit_count<5):
        print('Alloted seat in', Car1.name,' and your id is: ',Car1.ID[Car1.sit_count])
        Car1.sit_count += 1
    elif(Car2.sit_count<5):
          print('Alloted seat in', Car2.name,' and your id is: ',Car2.ID[Car2.sit_count])
          Car2.sit_count += 1
    else:
        print('seats not available in cars.')

if(user_in == 'B'):
    if(Bus1.sit_count<25):
        print('Alloted a sitting ticket in ',Bus1.name)
        Bus1.sit_count += 1
    elif(Bus1.stand_count<15):
          print('Alloted a standing ticket in ',Bus1.name)
          Bus1.stand_count += 1
    else:
        print('No seats available in bus.')

if(user_in == 'C'):
    remov_prob = random.random()
    if(remov_prob<0.6):
        if(Bus1.stand_count>0):
            print('person removed from bus.')
            Bus1.stand_count = Bus1.stand_count - 1
        elif(Bus1.sit_count>0):
            print('person removed from bus.')
            Bus1.sit_count = Bus1.sit_count - 1
        else:
            print('No person was removed.')
    
    elif(remov_prob<0.8):
        if(Car1.sit_count>0):
            print('person removed from ',Car1.name,'with ID ',Car1.ID[Car1.sit_count])
            Car1.sit_count = Car1.sit_count - 1
        else:
            print('No person removed from',Car1.name)

    else:
        if(Car2.sit_count>0):
            print('person removed from ',Car2.name,'with ID ',Car2.ID[Car2.sit_count])
            Car2.sit_count = Car2.sit_count - 1
        else:
            print('No person removed from',Car2.name)
            
  



