
class car(object):
    def __init__(self, year=0, make='', condition="n/a", pricing=5000.00):
        self.make = make
        self.year = year
        self.condition = condition
        self.pricing = pricing
    
    def printOut(self, printYear, printMake, printCondition, printPricing):
        if printYear == self.year:
            print("Car was made in %d\n" % (self.year))
        else:
            print("incorrect value")
        if printMake == self.make:
            print("Car is a %s\n" % (self.make))
        else:
            print("incorrect value")
        if printCondition == self.condition:
            print("Car is in %s condition.\n" % (self.condition))
        else:
            print("incorrect value")
        if printPricing == self.pricing:
            print("Car is worth $%d dollars\n" % (self.pricing))
        else:
            print("incorrect value")
    
    def printOutYear(self):
        print("Car attribute %d\n" % (self.year))
           
whip = car(2022, "example", "example_condition", 10)
whip.printOutYear()
whip.printOut(2022, "example", "example_condition",10)



