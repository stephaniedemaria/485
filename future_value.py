#!/usr/bin/env python3

import validation 

def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

#def get_float_monthly():
    #while True:
        #monthly_investment = float(input("Enter monthly investment:\t"))
        #if monthly_investment > 0 and monthly_investment <= 1000:
            #return monthly_investment
            #break
        #else:
            #print("Monthly Investment must be greater than 0 and less than 1000")

#def get_float_rate():
    #while True:
        #yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        #if yearly_interest_rate > 0 and yearly_interest_rate <= 15:
            #return yearly_interest_rate
            #break
        #else:
            #print("Interest rate must be greater than 0 and less than 15")
          
#def get_int():
    #while True:
        #years = int(input("Enter number of years:\t\t"))
        #if years > 0 and years <= 1000:
            #return years
            #break
        #else:
            #print("Years must be greater than 0 and less than 1000")
                  
def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = validation.get_float_monthly()
        yearly_interest_rate = validation.get_float_rate()
        years = validation.get_int()

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
