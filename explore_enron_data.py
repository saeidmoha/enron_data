#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print(len(enron_data)) # number of keys
print(len(enron_data[((list(enron_data))[0])])) # len of first key values.

print((list(enron_data))[0]) # first key (any key)
print(enron_data[((list(enron_data))[0])]) # print first value, which is also a dictionary

#print(enron_data.keys()) # all keys

nbofpoi = 0
for key in enron_data.keys():
    if (enron_data[key]['poi'] == 1):
        nbofpoi += 1
        
print("nb of POI = ", nbofpoi)

num_lines = sum(1 for line in open('/home/saeid/ud120-projects/final_project/poi_names.txt'))
print(num_lines - 2) 

print(enron_data["PRENTICE JAMES"]['total_stock_value'])
print(enron_data["COLWELL WESLEY"]['from_this_person_to_poi'])
print(enron_data["SKILLING JEFFREY K"]['exercised_stock_options'])

print("total_payments: ", enron_data["LAY KENNETH L"]['total_payments'])
print(enron_data["SKILLING JEFFREY K"]['total_payments'])
print(enron_data["FASTOW ANDREW S"]['total_payments'])

nbofpoi = 0
for key in enron_data.keys():
    if (enron_data[key]['salary'] != 'NaN'):
        nbofpoi += 1
        
print(nbofpoi)

nbofpoi = 0
for key in enron_data.keys():
    if (enron_data[key]['email_address'] != 'NaN'):
        nbofpoi += 1
        
print(nbofpoi)


nbofpoi = 0
nbtot = 0
for key in enron_data.keys():
    if (enron_data[key]['total_payments'] == 'NaN'):
        nbofpoi += 1
    else: nbtot += 1
        
print("total_payments NaN = and nbtot", nbofpoi, nbtot)
print("pourcent = ", 100 * (nbofpoi/(nbofpoi + nbtot)) )


nbofpoi = 0
for key in enron_data.keys():
    if (enron_data[key]['poi'] == 1 and enron_data[key]['total_payments'] == 'NaN'):
        nbofpoi += 1
        
print("nb of POI with total_payments=Nan is:  ", nbofpoi)

