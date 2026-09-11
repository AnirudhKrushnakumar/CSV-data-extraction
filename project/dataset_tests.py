# Initial variables and test datasets
valid_option = False
test_a = [10, 20, 30, 40, 50]
test_b =[40, 41, 39, 42, 40, 38, 41, 43, 39, 40, 42, 41, 37, 40, 39, 42, 41, 38, 40, 43]
test_c = [40, 42, 39, 100, 41, 38, 43, 40, 42, 39, 41, 38, 40, 42, 39, 41, 100, 40, 38, 42, 41, 39, 40, 43, 38]
unusual_readings = 0
below_20 = 0
above_60 = 0

# Calculates the average of the values in the dataset
def avg_val(dataset):
    if len(dataset) == 0:
        return 0
    return sum(dataset) / len(dataset)

# Calculates the unusual readings of the values in the dataset
def unusual_percent(dataset):
    if len(dataset) == 0:
        return 0
    return (100 * (unusual_readings / len(dataset)))

# Loop which allows for re-entry of set choosing
while valid_option == False:
    # Asks the user which dataset they'd like to use
    set_option = input("Choose which dataset you want to use (a, b, or c): ")
    # Chooses the dataset based on user input
    if set_option == "a":
        dataset = test_a
        valid_option = True
    elif set_option == "b":
        dataset = test_b
        valid_option = True
    elif set_option == "c":
        dataset = test_c
        valid_option = True
    else:
        print("Please choose a valid option.")

# Prints all information
print("Import Report:")
print("----------")
print(f"# of Readings: {len(dataset)}")
print(f"First Reading: {dataset[0]}")
print(f"Last Reading: {dataset[-1]}")
print(f"Minimum: {min(dataset)}")
print(f"Maximum: {max(dataset)}")
print(f"Average: {avg_val(dataset)}")
print(f"Below 20: {below_20}")
print(f"Above 60: {above_60}")
print(f"Unusual Readings: {unusual_readings}")
print(f"Unusual Reading %: {unusual_percent(dataset)}")