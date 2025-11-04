#hybied.py
#Jiawei Zhu
#
#Total cost of owning a hybrid car for five years and need to consider depreciation
#Input
The_cost_of_the_new_car = float(input("Cost of car:"))  
The_estimated_miles_driven_per_year = float(input("Miles driven per year:"))  
The_cost_of_gas = float(input("Cost of gas:"))  
The_fuel_efficiency_in_miles_per_gallon = float(input("Fuel efficiency (mpg):"))  
The_estimated_resale_value_after_five_years = float(input("Estimated resale value after 5 years:"))  
# Calculation of total_miles, total_gallons, and five_year_gas_cost
total_miles = The_estimated_miles_driven_per_year * 5
total_gallons = total_miles / The_fuel_efficiency_in_miles_per_gallon 
five_year_gas_cost = total_gallons * The_cost_of_gas
# five year car cost depreciation
five_year_car_cost = The_cost_of_the_new_car - The_estimated_resale_value_after_five_years
# Total cost over 5 years
five_year_total_cost = five_year_gas_cost + five_year_car_cost
print(f"Five year gas cost: {five_year_gas_cost:.1f}")
print(f"Five year car cost: {five_year_car_cost:.1f}")
print(f"Five year total cost: {five_year_total_cost:.1f}")
                                             

                                             
