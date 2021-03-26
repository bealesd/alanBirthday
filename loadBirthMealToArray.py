import json
import csv
import os

class CreateBirthdayMeal:
    def __init__(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        self.inputFile = os.path.join(__location__, 'bdayMeal.csv')
        self.outputFile = os.path.join(__location__, 'bdayMeal.js')

        self.starters = ['Soup','Salad','Salmon','Small Chicken Strips','Salad']
        self.mains = ['Turkey','Sea Bass','Cauliflower','Big Beef Burger','Pizza','Penne']
        self.deserts = ['Christmas Pudding','Cheesecake','Pavlova','Ice Cream','Chocolatey', 'Lava cake']

        self.fields = []

    def main(self):
        try:
            foodChoices = self.getMenuChoices()
            self.setMenuChoices(foodChoices)
        except Exception as e:
            print('Failed to create file: {0}. \nException: {1}'.format(self.outputFile, e))
        else:
            print('Created file: {0}'.format(self.outputFile))

    def getMenuChoices(self):
        foodChoices = {}

        with open(self.inputFile, newline='\n') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for index, row in enumerate(reader):
                if index == 0:
                    self.fields = row
                else:
                    name = row[0]
                    foodChoices[name] = {'starter': [], 'main': [], 'desert': [], 'notes': []}
                    for i, value in enumerate(row):
                        # choices = {}
                        if value.lower() == 'y':
                            choice = self.fields[i]
                            if choice in self.starters:
                                foodChoices[name]['starter'].append(choice)
                            elif choice in self.mains:
                                foodChoices[name]['main'].append(choice)
                            elif choice in self.deserts:
                                foodChoices[name]['desert'].append(choice)
                            else:
                                foodChoices[name]['notes'].append(choice)    

        return foodChoices

    def setMenuChoices(self, foodChoices):
        with open(self.outputFile, 'w') as fp:
            fp.write("window.bdayMeal = ' ")
            json.dump(foodChoices, fp)
            fp.write("';")


if __name__ == "__main__":
    # execute only if run as a script
    createBirthdayMeal = CreateBirthdayMeal()
    createBirthdayMeal.main()
