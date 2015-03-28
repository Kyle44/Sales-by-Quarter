# File:        hw3.py
# Written by:  Kyle Fritz
# Date:        9/25/2013
# Lab Section: 10
# UMBC email:  fritzk1@umbc.edu
# Description: This program will add up two divisions' quarters for a total 
#    value, then find the average amount for each quarter.
############### USE WITH PYTHON 3 ###########
# scl enable python33 bash


print("This program will calculate various sales data.")
def main():
    d1q1 = input("Enter Division 1's sales for quarter 1: ")
    d1q2 = input("Enter Division 1's sales for quarter 2: ")
    d1q3 = input("Enter Division 1's sales for quarter 3: ")
    d1q4 = input("Enter Division 1's sales for quarter 4: ")
    d2q1 = input("Enter Division 2's sales for quarter 1: ")
    d2q2 = input("Enter Division 2's sales for quarter 2: ") 
    d2q3 = input("Enter Division 2's sales for quarter 3: ") 
    d2q4 = input("Enter Division 2's sales for quarter 4: ")  
 # This will ask for the sales for each division for each quarter.
    list1 = []
    list2 = []   # This creates two different lists.
    list1.append(int(d1q1))
    list1.append(int(d1q2))
    list1.append(int(d1q3))
    list1.append(int(d1q4))
    list2.append(int(d2q1))
    list2.append(int(d2q2))
    list2.append(int(d2q3))
    list2.append(int(d2q4))    
# This adds the sales numbers to each corresponding list
    print("Division 1 sales by quarter: ")
    for element in list1:
       print("%s, "%(element), end = " ")
    print("\nDivision 2 sales by quarter: ")
    for element in list2:
        print("%s, "%(element), end = " ")  # This prints what information was
# inputed by the user.
    list3 = [x + y for x,y in zip(list1, list2)] # This adds each corresponding
# value in each list together.
    print("\nTotal sales by quarter: ")
    for element in list3:
        print("%s, "%(element), end = " ")
    list4 = [(x + y)/2 for x,y in zip(list1, list2)] # This finds the average
# of each corresponding value in each list.
    print("\nAverage sales by quarter: ")
    for element in list4:
        print("%s, "%(element), end = " ")
    print("\n")  # This makes sure that the program isn't on the same line
# as the prompt.   
main()
