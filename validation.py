#!/usr/bin/env python3

def get_float_monthly():
    while True:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment > 0 and monthly_investment <= 1000:
            return monthly_investment
            break
        else:
            print("Monthly Investment must be greater than 0 and less than 1000")

def get_float_rate():
    while True:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            return yearly_interest_rate
            break
        else:
            print("Interest rate must be greater than 0 and less than 15")
          
def get_int():
    while True:
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 1000:
            return years
            break
        else:
            print("Years must be greater than 0 and less than 1000")
                  
def main():
    choice = "y"
    while choice.lower() == "y":
        get_float_monthly()
        get_float_rate()
        get_int()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
