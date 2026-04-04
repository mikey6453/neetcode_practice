"""
Factory Method Pattern
Implement the Factory Method design pattern.

The Factory Method is a creational design pattern that provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.

You are given code that includes a few vehicles types and their respective factories. Complete the factory method implementation such that each factory returns the correct vehicle.

"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

class Car(Vehicle):
    def getType(self) -> str:
        print("Car")

class Bike(Vehicle):
    def getType(self) -> str:
        print("Bike")

class Truck(Vehicle):
    def getType(self) -> str:
        print("Truck")

class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
        pass

class CarFactory(VehicleFactory):
    # Write your code here
    def createVehicle(self) -> Vehicle:
        return Car()

class BikeFactory(VehicleFactory):
    # Write your code here
    def createVehicle(self) -> Vehicle:
        return Bike()

class TruckFactory(VehicleFactory):
    # Write your code here
    def createVehicle(self) -> Vehicle:
        return Truck()
    

carFactory = CarFactory()
bikeFactory = BikeFactory()
truckFactory = TruckFactory()

myCar = carFactory.createVehicle()
myBike = bikeFactory.createVehicle()
myTruck = truckFactory.createVehicle()

myCar.getType()
myBike.getType()
myTruck.getType()
