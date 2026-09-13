import csv

# Initial variables and empty list
readings = []
unusual_readings_ids = []
unusual_readings = 0
below_20 = 0
above_60 = 0

# Calculates the average of the values in the dataset
def avg_val(readings):
    if len(readings) == 0:
        return 0
    return sum(readings) / len(readings)

# Calculates the unusual readings of the values in the dataset
def unusual_percent(readings):
    if len(readings) == 0:
        return 0
    return (100 * (unusual_readings / len(readings)))

# Opens the .csv file and stores it within the empty list
with open('project/Robot_Sensor_Readings_1000.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        readings.append(float(row["distance_cm"]))
        if readings[-1] < 20 or readings[-1] > 60:
            # Adds to the unusual readings count
            unusual_readings += 1
            # Saves the reading_id of the unusual reading
            unusual_readings_ids.append(row["reading_id"])
        if readings[-1] < 20:
            # Adds to the below 20 count
            below_20 += 1
        if readings[-1] > 60:
            # Adds to the above 60 count
            above_60 += 1

# Prints all information
print("Import Report:")
print("----------")
print(f"# of Readings: {len(readings)}")
print(f"First Reading: {readings[0]}")
print(f"Last Reading: {readings[-1]}")
print(f"Minimum: {min(readings)}")
print(f"Maximum: {max(readings)}")
print(f"Average: {avg_val(readings)}")
print(f"Below 20: {below_20}")
print(f"Above 60: {above_60}")
print(f"Unusual Readings: {unusual_readings}")
print(f"Unusual Reading %: {unusual_percent(readings)}")
print(f"Unusual Reading IDs: {unusual_readings_ids}")

# Debugging Challenge 1
# print(type(row["distance_cm"]))
# print(type(float(row["distance_cm"])))

# Groups of 100 Analyzing
for start in range(0, len(readings), 100):
    group = readings[start:start + 100]
    print("Group:", start + 1, "to", start + len(group))
    print("Average:", sum(group) / len(group))
