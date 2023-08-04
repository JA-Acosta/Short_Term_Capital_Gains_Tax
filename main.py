'''
JAAR
08/03/2023
Short Term Gain Tax
Version 2
'''

import re

'''
Generates a program that calculates the short-term capital gains tax based on an initial amount, terms in days, and a daily interest rate.
'''

def get_tax_rates()->dict :
    '''
    >>> Extracts the current tax rates from a file for the user.

    >>> Return: (dict) tax_rates
    '''
    tax_rates = []
    # % : upper_range
    with open('Tax_Rates.txt', 'r') as tr :
        for line in tr.readlines() :
            bracket = list(map(float, line.split()))
            tax_rates.append(tuple(bracket))
    return tax_rates

def stock_data()->dict:
    '''
    >>> Takes a file containing a list of transactions and gets each stocks ticker, purchase amount and sell price.

    >>> Returns {dict} stock_information
    '''
    with open('stock_transactions.txt', 'r') as st :
        data = {}
        st.readline()
        for line in st.readlines() :
            ticker, i, j = list(filter(None, re.split(r'[\s]+', line)))
            data.update({ticker : float(j) - float(i)})
        return data

def calculate_taxes(earnings : float) :
    '''
    >>> Uses the current tax rates to calculate the total taxes for user earnings.

    >>> Return (float) taxes
    '''
    taxes = 0
    print(earnings)
    for bracket in get_tax_rates() :
        rate, minimum, maximum = bracket
        if maximum <= earnings :
            taxes += rate * (maximum - minimum) / 100
            print(taxes)
        else :
            if earnings < minimum :
                break
            taxes += (earnings - minimum) * rate / 100
            print(taxes)
    return taxes

def main() :
    print(calculate_taxes(sum(value for value in stock_data().values())))

if __name__ == '__main__' :
    main()