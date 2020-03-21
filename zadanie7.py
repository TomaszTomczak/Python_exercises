class IllegalCarError(Exception):
   """Base class for other exceptions"""
   pass

class Car:
    def __init__(self, pax_count, car_mass, gear_count):
        if (pax_count <1 or pax_count > 5) or car_mass > 2000:
            raise IllegalCarError
        self._pax_count = pax_count
        self._car_mass = car_mass
        self._gear_count = gear_count
        print("ctor")

    @property
    def total_mass(self):
        return self._pax_count*70.0

    @property
    def pax_count(self):
        print("getter")
        return self._pax_count

    @pax_count.setter
    def pax_count(self, count):
        print ("setter")
        c = int(count)
        if c > 5 or c < 1:
            print("raise an error")
            raise IllegalCarError
        self._pax_count = c
        

if __name__ == "__main__":
    try:
        car1 = Car(5,2000,4)
        car1.pax_count = 123123
        print (car1.total_mass)
        print (car1.pax_count)
    except IllegalCarError:
       print("wrong value")
    



    