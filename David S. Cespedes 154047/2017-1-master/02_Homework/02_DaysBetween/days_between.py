#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: days_between.py
# Description: This module calculates the difference in days between two dates
# Author: Diego Fernando Marin

def days_between(initial_date, final_date):
    """ (date, date) -> number
    return the days between two dates
    """
    # TODO: calculate and return the days between two dates
    from datetime import datetime, timedelta
    ini_date = ("")
    fin_date = ("")
    formato1 = "%Y-%m-%d"
    while True:
        try:
            if initial_date == "":
                break
            if final_date == "":
                break
            initial_date = datetime.strptime(initial_date, formato1)

            final_date = datetime.strptime(final_date, formato1)

            if final_date >= initial_date:
                days = final_date - initial_date
                return days.days
            else:
                return print("ingrese una fecha final mayor o igual a la inicial")
        except: 
            print ("error") 
        return 0           
def main():
    """ Main Program """
    ini_date = input("initial date (yyyy-mm-dd): ")
    fin_date = input("final date (yyyy-mm-dd): ")
    # TODO: convert the strings dates ("yyyy-mm-dd") to your date structure
    days = days_between(ini_date, fin_date)
    print("there are {} days between {} and {}".format(days, ini_date, fin_date))

if __name__ == "__main__":
    main()

