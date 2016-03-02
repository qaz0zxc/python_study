##Animal is a object(yes,sort of confusing) look ai the extra credit
class Animal(object):
    pass

##??
class Dog(Animal):
    def __init__(self,name):
        ## ??
        self.name = name

## ??
class Cat(Animal):
    def __init__(self,name):
        ## ??
        self.name = name

## ??
class Person(object):
    def __init__(self,name):
        ## ??
        self.name = name
        ## Person has a pet of some kind
        self.pet = None

    def say(self,name):
        print name

class My(Person):
    def __init__(self,name):
        self.name = name

## ??
class Employee(Person):
    def __init__(self,name,salary):
        ## ?? hmm what is this strange maigc?
        super(Employee,self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass

## rover is a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = My("Mary")
mary.say("Hello")
