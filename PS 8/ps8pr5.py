#
# ps8pr5.py (Problem Set 8, Problem 5)
#
# TT Securities
#
# Computer Science 111
#

import math

def display_menu():
    """ prints a menu of options
        """
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.

    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')
    print()

def get_new_prices():
    """ gets a new list of prices from the user and returns it
        """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
        """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
        """
    return prices[-1]

## Add your functions for options 3-7 below.

def avg_price(prices):
    """ returns the average price of a list of prices.
        input: prices is a list of 1 or more numbers.
        """
    total = 0
    for i in prices:
        total += i
        average = total / len(prices)
    return average

def std_dev(prices):
    """ returns the standard deviation of a list of prices
        input: prices is a list of 1 or more numbers.
        """
    total = 0
    for i in prices:
        total = total + ((i - avg_price(prices))**2)
        newtotal = total / len(prices)
        stddev = math.sqrt(newtotal)
    return stddev

def max_day(prices):
    """ returns the day of the maximum price.
        input: prices is a list of 1 or more numbers.
        """
    price = prices[0]
    pos = 0
    for i in range(len(prices)):
        if prices[i] > price:
            price = prices[i]
            pos = i
    return pos

def any_below(prices, num):
    """ returns True if there are any prices below threshold 'num'; False otherwise.
        input: prices is a list of 1 or more numbers.
        input: num is a single integer.
        """
    for x in prices:
        if x < num:
            return True
    return False

def find_plan(prices):
    """ returns a list containing three integers:
        [the buy day, the sell day, the resulting profit]
        input: prices is a list of 2 or more prices.
        idea: uses loops to find the best days on which to buy and sell the stock
        whose prices are given in the list of prices; the buy and sell days
        determined should maximize the profit earned, but the sell day must be
        greater than the buy day.
        """
    maxdiff = prices[1] - prices[0]
    buy = 0
    sell = 0
    for x in range(len(prices)):
        for y in range(x + 1, len(prices)):
            d = prices[y] - prices[x]
            if d > maxdiff:
                maxdiff = d
                buy = x
                sell = y
    return [buy, sell, maxdiff]

def tts():
    """ the main user-interaction loop
        """
    prices = []
    
    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()
        
        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here

        elif choice == 3:
            avgprice = avg_price(prices)
            print('The average price is', avgprice)
        elif choice == 4:
            standarddev = std_dev(prices)
            print('The standard deviation is', standarddev)
        elif choice == 5:
            maxday = max_day(prices)
            print('The max price is', prices[maxday], 'on day', maxday)
        elif choice == 6:
            inp = int(input('Enter the threshold: '))
            answer = any_below(prices, inp)
            if answer is True:
                print('There is at least one price below', inp)
            else:
                print('There are no prices below', inp)
        elif choice == 7:
            plan = find_plan(prices)
            buyday = plan[0]
            sellday = plan[1]
            profit = plan[2]
            print(' Buy on day', buyday, 'at price', prices[buyday])
            print('Sell on day', sellday, 'at price', prices[sellday])
            print('Total profit:', profit)
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
