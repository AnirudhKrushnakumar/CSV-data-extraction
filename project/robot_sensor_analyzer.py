import csv

readings = []
unusual_readings = 0
below_20 = 0
above_60 = 0

def avg_val(readings):
    if len(readings) == 0:
        return 0
    return sum(readings) / len(readings)

def unusual_percent(readings):
    if len(readings) == 0:
        return 0
    return (100 * (unusual_readings / len(readings)))

with open('Robot_Sensor_Readings_1000.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        readings.append(float(row["distance_cm"]))
        if readings[-1] < 20 or readings[-1] > 60:
            unusual_readings += 1
        if readings[-1] < 20:
            below_20 += 1
        if readings[-1] > 60:
                    above_60 += 1

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