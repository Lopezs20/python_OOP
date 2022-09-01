import random
class person(object):
    idty = random.randint(1, 100)
    def __init__(self, name, age, sex="n/a", occupant="n/a", id=idty):
        self.name = name
        self.age = age
        self.sex = sex
        self.occupant = occupant
        self.idty = id
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGender(self):
        return self.sex
    def getOccupant(self):
        return self.occupant
    def setName(self, newName):
        self.name = newName
    def setAge(self, newAge):
        self.age = newAge
    def setGender(self, gender):
        self.gender = gender
    def setOccupant(self, occupant):
        self.occupant = occupant
    @staticmethod
    def isAdult(age):
        return age >= 18
    def printPerson(self):
        print("%s is %d years old, identifies as %s, and does %s for a living."% (self.name, self.age, self.sex, self.occupant))
    @classmethod
    def getId(cls):
        return cls.idty
    def getId(self):
        return self.idty
    
mike = person("Mike", 57, "male", "postguard")
print("This is Mike's ID: %d" % (mike.getId()))
mike.printPerson()
