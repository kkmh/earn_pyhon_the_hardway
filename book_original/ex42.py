# Animal is-a object (yes sort of confusing) look at the extra credit
class Animal(object):
    pass


# Dog is-a animal
class Dog(Animal):
    def __init__(self, name):
        # Dog has-a name
        self.name = name


# Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        # Cat has-a name
        self.name = name


# Person is-a Object
class Person(object):
    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None


# Employee is-a Object
class Employee(Person):
    def __init__(self, name, salary):
        # hmm what is this strange magic?
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary


# Fish is-a object
class Fish(object):
    pass


# Salmon is-a Fish
class Salmon(Fish):
    pass


# Halibut is-a Fish
class Halibut(Fish):
    pass

# Rover is-a Dog
rover = Dog("Rover")

# satan is-a cat
satan = Cat("Satan")

# mary is-aperson
mary = Person("Mary")

# Mary has-a pet called satan, which is-a cat
mary.pet = satan

# Frank is-a employee, which is-a person and has-a salary
frank = Employee("Frank", 12000)
print "This is %s. He earns %d" % (frank.name, frank.salary)
# frank has-a pet called rover
frank.pet = rover

# flipper is-a fish
flipper = Fish()

# crouse is-a salmon
crouse = Salmon()

# harry is-a wizard (jokes) Halibut
harry = Halibut()