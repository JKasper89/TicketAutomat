#!/usr/local/bin/python
# coding: utf-8


#program: ticket machine
#author: Jan Kasper


from decimal import *
import locale
import time
import math

#version info and greeting
__infoWidth__ = 80
__version__ = '0.1'
__author__ = 'Jan Kasper'

x = ''.center(80, '*') + "\n" + (' '*76).center(80, '*') + "\n" + \
    'Ticket Automat'.center(76, ' ').center(80, '*') \
    + "\n" + (__version__ + ' vom ' + (time.strftime("%d.%m.%y"))).center(76, ' ').center(80, '*') \
    + "\n" + 'Fehler bitte an jankasper@students.tbs1.de'.center(76, ' ').center(80, '*') \
    + "\n" + (' '*76).center(80, '*')+"\n"+''.center(80, '*')
print(x)

locale.setlocale(locale.LC_ALL, 'german')

#initialize machine
newTicket = True

#amount of money at start
contentMoney = {"ct2000" : 50, "ct1000" : 50, "ct500" : 50, "ct200" : 0, "ct100" : 50, "ct50" : 50, "ct20" : 50, "ct10" : 50 }

#main routine
while newTicket:
    #Ask User for Ticket Price
    while True:
        try:
            ticketPrice = input("Bitte geben Sie den Ticketpreis an:")
            ticketPrice = Decimal(ticketPrice)
            ticketPrice = ticketPrice*100
            if ticketPrice <= 0:
                raise ValueError
            break
        except InvalidOperation:
            print("Achtung! Bitte geben Sie eine Zahl ein!")
        except ValueError:
            print("Achtung! Bitte geben Sie eine Zahl grösser 0 ein !")

    print (ticketPrice)
    #User is paying now
    payAmount = 0
    while payAmount < ticketPrice:
        temp = 0
        temp = int(input("Bitte geben Sie einen Schein oder eine Münze ein: \n (1) := 20 Euro \n (2) := 10 Euro "
                     "\n (3) := 5 Euro \n (4) := 2 Euro \n (5) := 1 Euro \n (6) := 50 Cent \n (7) := 20 Cent \n (8) := 10 Cent"))
        if (temp == 1):
            contentMoney["ct2000"] += 1
            payAmount += 2000
        elif temp == 2:
            contentMoney["ct1000"] += 1
            payAmount += 1000
        elif temp == 3:
            contentMoney["ct500"] += 1
            payAmount += 500
        elif temp == 4:
            contentMoney["ct200"] += 1
            payAmount += 200
        elif temp == 5:
            contentMoney["ct100"] += 1
            payAmount += 100
        elif temp == 6:
            contentMoney["ct50"] += 1
            payAmount += 50
        elif temp == 7:
            contentMoney["ct20"] += 1
            payAmount += 20
        elif temp == 8:
            contentMoney["ct10"] += 1
            payAmount += 10
        else:
            print("Bitte geben Sie eine Zahl aus der obigen Auswahl an!")

#calculate return
    returnMoney = 0
    while  ticketPrice + returnMoney < payAmount:
        if contentMoney["ct2000"] > 0:
            if payAmount - ticketPrice - returnMoney >= 2000:
                contentMoney["ct2000"] -= 1
                returnMoney += 2000
        if contentMoney["ct1000"] > 0:
            if payAmount - ticketPrice - returnMoney >= 1000:
                contentMoney["ct1000"] -= 1
                returnMoney += 1000
        if contentMoney["ct500"] > 0:
            if payAmount - ticketPrice - returnMoney >= 500:
                contentMoney["ct500"] -= 1
                returnMoney += 500
        if contentMoney["ct200"] > 0:
            if payAmount - ticketPrice - returnMoney >= 200:
                contentMoney["ct200"] -= 1
                returnMoney += 200
        if contentMoney["ct100"] > 0:
            if payAmount - ticketPrice - returnMoney >= 100:
                contentMoney["ct100"] -= 1
                returnMoney += 100
        if contentMoney["ct50"] > 0:
            if payAmount - ticketPrice - returnMoney >= 50:
                contentMoney["ct50"] -= 1
                returnMoney += 50
        if contentMoney["ct20"] > 0:
            if payAmount - ticketPrice - returnMoney >= 20:
                contentMoney["ct20"] -= 1
                returnMoney += 20
        if contentMoney["ct10"] > 0:
            if payAmount - ticketPrice - returnMoney >= 10:
                contentMoney["ct10"] -= 1
                returnMoney += 10

#check
  #  if not payAmount -ticketPrice - returnMoney == 0:
   #     print("Es ist ein schwerwiegender Fehler aufgetreten! Das Programm wird beendet!")
    #    break

#Answer
    print("Sie erhalten ein Rückgeld in Höhe von " + str(returnMoney))
    print("Der Bestand des Geldautomaten beträgt:")
    for key in contentMoney:
        print(key + ": " + str(contentMoney[key]))

# new ticket?
    """     while true: 
            choose=str(input("Möchten Sie ein weiteres Ticket kaufen? (y,n)"))
            if choose == :
               repeat=True
            elif choose == n:
                repeat = False"""




