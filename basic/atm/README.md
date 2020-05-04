# ATM Exercise

## Goals

1. User input.
2. Dictionaries.
3. Functional programing.

## Introduction

Write a program that will simulate an ATM. When the program will initialize it will read a file containing all the customers of the bank. The file will specify for each customer its customer-ID, ATM password, and the consumer balance (that can't be negative).

The ATM will allow the following options to a using costumer:
1. Check the balance.
2. Cash withdrawal.
3. Cash deposit.
4. Change password.  

To turn off the ATM, enter `-1` as the customer ID. When the ATM will be turned off, it will save the current state of all the bank customers.

## Recommendations & Notes

* Use a simple file for the customers data. Each customer will be a single line and their information will come in a known order separated by a comma or a space.
* Use dictionaries to find the user data based on the customer-ID.






