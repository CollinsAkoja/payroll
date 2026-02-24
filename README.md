Payroll System with Inheritance and Polymorphism (Python)
Project Overview

This project is a simple Python-based payroll system designed to demonstrate key Object-Oriented Programming (OOP) concepts:

Classes and Objects

Inheritance

Method Overriding

Polymorphism

Modular system design

The system models employees in an organization and processes their salaries using different payment methods.

Features
Employee Management

The program defines a base Employee class containing:

Employee name

Salary

Bonus calculation method

Two subclasses extend the base class:

Manager

Receives a higher bonus percentage.

Developer

Receives a moderate bonus percentage.

Each subclass overrides the bonus calculation to demonstrate polymorphism.

Payment Processing System

A base Payment class defines a common method:

process_payment()

Three subclasses simulate different payment methods:

CreditCardPayment

PayPalPayment

BankTransferPayment

Each subclass overrides the payment method to demonstrate different processing behaviors.

Payroll Integration

The PayrollSystem class connects employees with their payment methods.

The system:

Stores employee-payment pairs

Calculates salary + bonus

Processes payments using polymorphism

Project Structure
payroll_project/
│
├── payroll.py        # Main payroll program
└── README.md      # Project documentation
Example Workflow

Create employee objects:

Manager

Developer

Regular Employee

Assign payment methods:

Credit Card

PayPal

Bank Transfer

Run payroll:

Bonuses are calculated

Payments are processed using the assigned method

Sample Output
Paying Collins:
Processing credit card payment for Collins. Amount: $108000.00

Paying Israel:
Processing PayPal payment for Israel. Amount: $80500.00

Paying Odiase:
Processing bank transfer for Odiase. Amount: $55000.00
OOP Concepts Demonstrated
Inheritance

Manager and Developer inherit from the Employee base class.

Method Overriding

Each subclass defines its own bonus calculation.

Polymorphism

The same method:

process_payment()

behaves differently depending on the payment type.

Requirements

Python 3.x

No external libraries required

How to Run
python payroll.py
Possible Improvements (Future Work)

Connect to a real database (SQLite or MySQL)

Add employee IDs and departments

Build a GUI using Tkinter or a web dashboard using Flask

Export payroll reports to Excel or CSV

Add real payment API integration (Stripe, PayPal API)

Author
Collins Akoja Nathaniels

Payroll System Demo Project for learning Python OOP and Polymorphism.
