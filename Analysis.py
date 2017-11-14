from __future__ import division
import csv
import os
import sys
import math
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def data_retrieve(information_file):
	with open(information_file) as information:
		data = csv.reader(information)
		temp = list()
		for row in data:
			temp.append(row)
		all_data = map(list, zip(*temp))
		latitude = all_data[0]
		length = len(latitude)
		longtitude = all_data[1]
		price = all_data[2]
		weekly_price = all_data[3]
		monthly_price = all_data[4]
		#reviews per month
		reviews = all_data[8]
		number_of_owners=0
		total_price = 0
		return(latitude, longtitude, price, weekly_price, monthly_price, reviews)
def price_estimation(lat, longit, information_file):
	(latitude, longtitude, price, weekly_price, monthly_price, 
	reviews) = data_retrieve(information_file)
	length = len(latitude)
	number_of_owners=0
	total_price = 0
	for i in range(1, length):
		if(latitude[i]==str(lat) and longtitude[i]==str(longit)):
			denom = 3
			if(float(weekly_price[i])==0):
				temp_wp = 0
				denom-=1
			else:
				temp_wp = float(weekly_price[i])
			if(float(monthly_price[i])==0):
				temp_mp = 0
				denom-=1
			else:
				temp_mp = float(monthly_price[i])
			temp_p = float(price[i])

			weekly_income = (temp_p*7 + temp_wp + temp_mp/4)/denom
			print(temp_wp)
			total_price+=weekly_income
			number_of_owners+=1

	if(number_of_owners==0):
		return "No airbnb present in the area"
	else:
		return total_price/number_of_owners

def booking_optimization(lat, longit, information_file):
	(latitude, longtitude, price, weekly_price, monthly_price, 
	reviews) = data_retrieve(information_file)
	max_revenue = -1
	length = len(latitude)
	for i in range(length):
		if(latitude[i]==str(lat) and longtitude[i]==str(longit)):
			temp_p = float(price[i])
			weekly_income = temp_p*7
			if(weekly_income>max_revenue):
				max_revenue = weekly_income
	if(max_revenue==-1):
		return "No airbnb present in the area"
	else:
		return max_revenue

print(price_estimation(37.75418395, -122.4065138, "useful_information.csv"))
print(booking_optimization(37.75418395, -122.4065138, "useful_information.csv"))
