import pandas as pd
import numpy as np

missing_values = [np.NaN,"NaN", "N/A", "nan", " "]
df = pd.read_csv("airbnb_listings.csv", na_values= missing_values)
df['reviews_per_month'] = df['reviews_per_month'].fillna(0)
df.host_is_superhost = df.host_is_superhost.replace({"t":1, "f":0})
df["bathrooms"].fillna(0,inplace=True)
df.host_has_profile_pic = df.host_has_profile_pic.replace({"t":1, "f":0})
df.host_identity_verified = df.host_identity_verified.replace({"t": 1,"f":0})
df.instant_bookable= df.instant_bookable.replace({"t":1,"f":0})
df.has_availability = df.has_availability.replace({"t":1 , "f":0})
df['last_scraped'] = pd.to_datetime(df['last_scraped'])
df['price'] = df['price'].str.strip('$')
df['host_response_rate'] = df['host_response_rate'].str.strip('%')
df['host_acceptance_rate'] = df['host_acceptance_rate'].str.strip('%')
df['price'] = pd.to_numeric(df['price'], errors='coerce')

for i in df:
    for j in i:
        if j == missing_values:
            df['i'] = df['i'].dropna()

df['price'] = pd.to_numeric(df['price'], errors='coerce')

def the_cheapest_house():
    return df['price'].min()

def the_exp_house():
    return df['price'].max()

def price_of_rooms(n_beds):
    if n_beds in range(1, 18) and n_beds not in {11, 17}:
        condition = (df['beds'] == n_beds) & (df['has_availability'] == 1)
        filtered_df = df[condition]
        min_values = filtered_df[['id', 'beds', 'neighbourhood_cleansed', 'room_type', 'price']].min()
        return min_values
    else:
        print(f"Invalid number of beds: {n_beds}. Please provide a number between 1 and 18.")

def all_info_based_in_room(n_beds):
    if n_beds in range(1, 18) and n_beds not in {11, 17}:
        condition = (df['beds'] == n_beds) & (df['has_availability'] == 1)
        filtered_df = df[condition]
        return filtered_df
    else:
        print(f"Invalid number of beds: {n_beds}. Please provide a number between 1 and 18.")

def info_based_inprice(price_eu):
    if price_eu in df['price'].values:
        return df[df['price'] == price_eu]
    else:
        print("Your budget is not on the prices")
        unique_prices = set(df["price"])
        print("Prices list that you can choose:", unique_prices)

def main():
    print("Welcome to Airbnb info\n")
    a = input("The menu is the following: (Choose your number option) \n 1.-The cheapest price\n 2.- The most expensive house\n 3.- Price for bed(s)\n 4.- Bed according to the budget\n")
    options = {'1', '2', '3', '4'}
    
    if a in options:
        if a == '1':
            print(f"The cheapest price: {the_cheapest_house()}")
        elif a == '2':
            print(f"The most expensive house: {the_exp_house()}")
        elif a == '3':
            s_rooms = input("How many beds are you looking for (the cheapest price available):\n")
            print(price_of_rooms(int(s_rooms)))
        elif a == '4':
            budget_p = input("Budget:\n")
            print(info_based_inprice(float(budget_p)))
    else:
        print("Introduce a valid option")

main()