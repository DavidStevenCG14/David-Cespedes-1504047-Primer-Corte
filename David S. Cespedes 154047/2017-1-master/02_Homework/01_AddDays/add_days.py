#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: add_days.py
# Description: This module calculates the result of a date plus some days
# Author: Diego Fernando Marin

def add_days(date, days):
    """ (date, number) -> date
    return the final date after adding some days to the initial date
    """
    # TODO: calculate and return the correct date
    from datetime import datetime, timedelta

    initial_date=("")

    formato1 = "%Y-%m-%d"
    date = datetime.strptime(date, formato1)

    days = timedelta(days=days)
    final_date = date + days

    return final_date.strftime(formato1)

def main():
    """ Main Program """
    initial_date = input("initial date (yyyy-mm-dd): ")
    # TODO: convert the string "yyyy-mm-dd" to your date structure "initial_date"
    days = int(input("days: "))
    final_date = add_days(initial_date, days)
    print("{} + {} days = {}".format(initial_date, days, final_date))

if __name__ == "__main__":
    main()
