# gas_payment.py

def gas_payment(car_mpg, miles_to_drive, gas_price_per_gallon):

    gallons_required = (miles_to_drive/car_mpg)
    total_price = gallons_required * gas_price_per_gallon


    print(f"""
For a car trip where:
	- Miles = {miles_to_drive},
	- Car miles per gallon = {car_mpg} MPG
        - Gas price = ${gas_price_per_gallon:.2f}/gal,

You would owe your driver:
    ${total_price:.2f} (total gallons of gas required = {gallons_required:.2f})
""")


if __name__ == "__main__":
    car_mpg = int(input("Car MPG: "))
    miles_to_drive = float(input("Miles to drive: "))
    gas_price_per_gallon = float(input("Gas price per gallon: "))

    gas_payment(car_mpg, miles_to_drive, gas_price_per_gallon)


