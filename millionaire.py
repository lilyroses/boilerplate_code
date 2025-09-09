sec_per_min = 60
min_per_hr = 60
hr_per_day = 24
min_per_day = hr_per_day * min_per_hr

def spend_it_fast(days, dollar_amount):
  dollars_per_day = dollar_amount / days
  dollars_per_hour = dollars_per_day / hr_per_day
  dollars_per_min = dollars_per_hour / min_per_hr
  print(f"""
To spend ${dollar_amount:,} in {days} days, you would need to spend:
  - ${dollars_per_day:,.2f} / day
  - ${dollars_per_hour:,.2f} / hr
  or
  - ${dollars_per_min} / min
""")


if __name__ == "__main__":
  print("\nInput a dollar amount and X days to find out how fast you'd have to spend to spend that much money in X days.")
  days = int(input("Days: "))
  dollar_amount = int(input("Dollar amount: "))
  spend_it_fast(days, dollar_amount)
