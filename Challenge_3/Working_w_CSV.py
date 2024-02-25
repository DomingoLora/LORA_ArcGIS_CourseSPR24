#PART 3: Working with CSV

import csv
from collections import defaultdict

def calculate_seasonal_average(months):
    seasonal_list = []
    with open("co2-ppm-daily.csv") as CO2:
        csv_reader = csv.reader(CO2, delimiter=',')
        header_skip = next(CO2)

        for row in csv_reader:
            year, month, day = row[0].split("-")
            if row[0].split("-")[1] in months:
                seasonal_list.append(float(row[1]))

    return round(sum(seasonal_list) / len(seasonal_list), 3)

years_dict = defaultdict(list)
CO2_values = []

with open("co2-ppm-daily.csv") as CO2:
    csv_reader = csv.reader(CO2, delimiter=',')
    header_skip = next(CO2)

    for row in csv_reader:
        year, month, day = row[0].split("-")
        CO2_values.append(float(row[1]))
        years_dict[year].append(float(row[1]))

print("The maximum CO2 value from the list is", max(CO2_values))
print("The minimum CO2 value from the list is", min(CO2_values))
print("The average of all CO2 values from the list is", round(sum(CO2_values) / len(CO2_values), 2))

print("\nThe following are average annual CO2 values from 1958-2017:")
for year, values in years_dict.items():
    print(f"{year}: {round(sum(values) / len(values), 2)}")

spring_avg = calculate_seasonal_average(['03', '04', '05'])
summer_avg = calculate_seasonal_average(['06', '07', '08'])
autumn_avg = calculate_seasonal_average(['09', '10', '11'])
winter_avg = calculate_seasonal_average(['12', '01', '02'])

print("\nThe average CO2 value throughout Spring months in this dataset =", spring_avg)
print("The average CO2 value throughout Summer months in this dataset =", summer_avg)
print("The average CO2 value throughout Autumn months in this dataset =", autumn_avg)
print("The average CO2 value throughout Winter months in this dataset =", winter_avg)
