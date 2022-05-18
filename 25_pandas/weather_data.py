# weather_data = []
# with open('weather_data.csv', 'r') as data:
#     data_file = data.readlines()
#     for i in data_file:
#         i = i.split(',')
#         weather_data.append(i)

# import csv
# with open('weather_data.csv', 'r') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for i in data:
#         try:
#             temperatures.append(int(i[1]))
#         except:
#             continue
#     print(temperatures)

import pandas
# read data from csv
data = pandas.read_csv("weather_data.csv")

# show temp column
temp = data["temp"]

# calculate average and maximum temp
avg_temp = temp.mean()
max_temp = temp.max()

# show row for Monday
monday = data[data.day == "Monday"]
print(monday.temp)

# convert temp from C to F
temp = monday.temp * 9 / 5 + 32
print(temp)

# show row with max temp
print(data[data.temp == max_temp])

# create dataframe from dict
data_dict = {
    "students": ['John', 'Joe', 'James'],
    "scores": [80, 70, 60]
}
data = pandas.DataFrame(data_dict)
print(data)
# save to file
data.to_csv('new_data.csv')