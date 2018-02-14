import os
import osa
import requests
import re
from datetime import datetime

client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')

def temp_converter():
    file = open('temps.txt', 'r')
    # print(file)
    temps = []
    for line in file:
        # print(line)
        result = re.match('\d+', line)
        print(result.group(0))
        temps.append(int(result.group(0)))
    average_temp = sum(temps)/len(temps)
    print(average_temp)

    result = client.service.ConvertTemp(average_temp, 'degreeFahrenheit', 'degreeCelsius')
    print(result)

temp_converter()

client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')

def currency_converter():
    file = open('currencies.txt', 'r')
    cost = 0.0
    for line in file:
        result = re.findall('\S+', line)
        date = datetime.now().date()
        print(result)
        resultat = client.service.ConvertToNum('', result[2], 'RUB', result[1], True, '', '')
        # print(resultat)
        cost += round(resultat)
        print(cost)

currency_converter()

client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')

def miles_converter():
    file = open('travel.txt', 'r')
    miles_distance = 0.00
    kilometres_distance = 0.00
    distances = []
    for line in file:
        line = line.replace(',', '')
        # print(line)
        result = re.findall('\d*\.\d*', line)
        # print(result)
        miles_distance = int(result[0])
        kilometres_distance = client.service.ChangeLengthUnit(miles_distance, '', 'Miles', 'Kilometres')
        print(kilometres_distance)

miles_converter()