import csv

# with open("226 weather-data.csv") as data_list:
#     data = csv.reader(data_list)
#     temperatures = []
#     for row in data:
#         temperature = row[1]
#         if temperature != "temp":
#             temperature_int = int(temperature)
#             temperatures.append(temperature_int)
#
# print (temperatures)

import pandas

#data = pandas.read_csv("226 weather-data.csv")
#list_max = data["temp"].max()
#highest_temp_row = data[data.temp == list_max]
#print(highest_temp_row.day)
#print(highest_temp_row.condition )

data = pandas.read_csv("Squirrel_Data.csv")

# counting squirrels
squirrel_colors = data["Primary Fur Color"]
print(squirrel_colors)
red_count = 0
gray_count = 0
black_count = 0
x= 0

while x < len(squirrel_colors) -1:
    if squirrel_colors[x] == "Gray":
        gray_count += 1
    elif squirrel_colors[x] == "Black":
        black_count +=1
    elif squirrel_colors[x] =="Cinnamon":
        red_count += 1
    x += 1

squirrel_counts = {
    "Fur Color": ["Red", "Gray", "Black"],
    "Number of Squirrels": [[gray_count], [black_count], [red_count]]}

df = pandas.DataFrame.from_dict(squirrel_counts)
print(df)