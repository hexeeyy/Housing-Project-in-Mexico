""" This is my online course in Worldquant University that is all about Data Science"""
# Project 01: Housing Project in Mexico

# Declare variable `house_0_list`
house_0_list = [115910.26, 128, 4]

# Print object type of `house_0_list`
# (We'll learn more about object types in later projects 😉)
print("house_0_list type:", type(house_0_list))

# Print length of `house_0_list`
print("house_0_list length:", len(house_0_list))

# Get output of `house_0_list`
print(house_0_list)

# Task 1.1.1: One metric that people in the real estate industry look at 
# is price per square meter because it allows them to compare houses of different sizes. 
# Can you use the information in this list to calculate the price per square meter for house_0?

house_0_price_m2 = house_0_list[0]/house_0_list[1]
print(house_0_price_m2)

#Task 1.1.2: Next, use the append method to add the price per square meter to the end of the end of house_0.
house_0_list.append(house_0_price_m2)
print(house_0_list)

# Nested List
# Declare variable `houses_nested_list`
houses_nested_list = [
    [115910.26, 128.0, 4.0],
    [48718.17, 210.0, 3.0],
    [28977.56, 58.0, 2.0],
    [36932.27, 79.0, 3.0],
    [83903.51, 111.0, 3.0],
]

# Print `houses_nested_list` type
print("houses_nested_list type:", type(houses_nested_list))

# Print `houses_nested_list` length
print("houses_nested_list length:", len(houses_nested_list))

# Get output of `houses_nested_list`
print(houses_nested_list)

#**Task 1.1.3:** Append the price per square meter to each 
# observation in `houses_nested_list` using a `for` loop.

for house in houses_nested_list:
    price_m2 = house[0]/house[1]
    house.append(price_m2)
print(houses_nested_list)

# Dictionary
# Declare variable `house_0_dict`
house_0_dict = {
    "price_approx_usd": 115910.26,
    "surface_covered_in_m2": 128,
    "rooms": 4,
}

#Task 1.1.4: Calculate the price per square meter for 
# house_0 and add it to the dictionary under the key "price_per_m2".

house_0_dict["price_per_m2"]=house_0_dict["price_approx_usd"]/house_0_dict["surface_covered_in_m2"]
print(house_0_dict)

#JSON
# Declare variable `houses_rowwise`
houses_rowwise = [
    {
        "price_approx_usd": 115910.26,
        "surface_covered_in_m2": 128,
        "rooms": 4,
    },
    {
        "price_approx_usd": 48718.17,
        "surface_covered_in_m2": 210,
        "rooms": 3,
    },
    {
        "price_approx_usd": 28977.56,
        "surface_covered_in_m2": 58,
        "rooms": 2,
    },
    {
        "price_approx_usd": 36932.27,
        "surface_covered_in_m2": 79,
        "rooms": 3,
    },
    {
        "price_approx_usd": 83903.51,
        "surface_covered_in_m2": 111,
        "rooms": 3,
    },
]

#Task 1.1.5: Using a for loop, calculate the price per square meter and store the result under a 
# "price_per_m2" key for each observation in houses_rowwise.

for house in houses_rowwise:
    house["price_per_m2"]=house["price_approx_usd"]/house["surface_covered_in_m2"]
    print(house)

#Task 1.1.6: To calculate the mean price for houses_rowwise by 
# completing the code below.
# Declare `house_prices` as empty list
house_prices = []

# Iterate through `houses_rowwise`
for house in houses_rowwise:
    house_prices.append(house["price_approx_usd"])

    # For each house, append "price_approx_usd" to `house_prices`


# Calculate `mean_house_price` using `house_prices`
mean_house_price = sum(house_prices) / len(house_prices)

# Print `mean_house_price` object type
print("mean_house_price type:", type(mean_house_price))

# Get output of `mean_house_price`
print(mean_house_price)

# Declare variable `houses_columnwise`
houses_columnwise = {
    "price_approx_usd": [115910.26, 48718.17, 28977.56, 36932.27, 83903.51],
    "surface_covered_in_m2": [128.0, 210.0, 58.0, 79.0, 111.0],
    "rooms": [4.0, 3.0, 2.0, 3.0, 3.0],
}

# Print `houses_columnwise` object type
print("houses_columnwise type:", type(houses_columnwise))

# Get output of `houses_columnwise`
print(houses_columnwise)

#Task 1.1.7: Calculate the mean house price in houses_columnwise
# Calculate `mean_house_price` using `houses_columnwise`
mean_house_price = sum(houses_columnwise["price_approx_usd"]) / len(houses_columnwise["price_approx_usd"])
print(mean_house_price)

#Task 1.1.8: Create a "price_per_m2" column in houses_columnwise?

# Add "price_per_m2" key-value pair for `houses_columnwise`
houses_columnwise["price_per_m2"] = [price/surface for price, surface in zip(houses_columnwise["price_approx_usd"], houses_columnwise["surface_covered_in_m2"])]
print(houses_columnwise)

# Import pandas library, aliased as `pd`
import pandas as pd

# Declare variable `df_houses`
df_houses = pd.DataFrame(houses_columnwise)

# Get output of `df_houses`
print(df_houses)

#my own practice
#Create a dictionary
new_data = {
    "key": [203, 20, 223, 1212],
    "feature2": ["Codes", "Age", "Achievements", "Work"]
}
print("\nData", new_data, type(new_data))

datax = (list(zip(new_data["feature2"], new_data["key"] )))
print("\nThis is the datax: ", datax, type(datax))

#Declare a new variable and add it to the datax
Add = {
    "Math": 54,
    "Science": 32
}
print("\nThis is the New Data: ", Add, type(Add))

# From the Add dictionary, separate the key and the value.
add_items = list(Add.items())
print("\nThis is the add_items: ", add_items, type(add_items))

# Extend datax with add_items
datax.extend(add_items)
print("\nThis is the extended datax: ", datax, type(datax))

df_new_data = pd.DataFrame(datax, columns=['Feature', 'Grade'], index=[chr(97 + i) for i in range(len(datax))])
print(df_new_data)




