import json
import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

filePath = os.path.join(__location__, 'bdayMeal.csv')
fields = []
foodChoices = {}

starters = ['Soup','Salad','Salmon','Small Chicken Strips','Salad']
mains = ['Turkey','Sea Bass','Cauliflower','Big Beef Burger','Pizza','Penne']
deserts = ['Xmas Pudding','Cheesecake','Pavlova','Ice Cream','Chocolatey', 'Lava cake']

with open(filePath, newline='\n') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for index, row in enumerate(reader):
        if index == 0:
            fields = row
        else:
            name = row[0]
            foodChoices[name] = {'starter': [], 'main': [], 'desert': [], 'notes': []}
            for i, value in enumerate(row):
                choices = {}
                if value.lower() == 'y':
                    choice = fields[i]
                    if choice in starters:
                        foodChoices[name]['starter'].append(choice)
                    elif choice in mains:
                        foodChoices[name]['main'].append(choice)
                    elif choice in deserts:
                        foodChoices[name]['desert'].append(choice)
                    else:
                        foodChoices[name]['notes'].append(choice)

outputFile = os.path.join(__location__, 'bdayMeal.js')
with open(outputFile, 'w') as fp:
    fp.write("window.bdayMeal = ' ")
    json.dump(foodChoices, fp)
    fp.write("';")