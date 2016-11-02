from flask import request
import csv
import hashlib

def hesh(a):
    return(hashlib.md5(a).hexdigest())

def regi(a, b):
    c = csv.reader(open("name.csv"))
    for d in c:
        if a == d[0]:
            return "Name Taken!"
    with open('name.csv', 'a') as e:
        f = csv.writer(e)
        f.writerow([a, hesh(b)])
    return "Added"
             

def login(a, b):
    c = csv.reader(open("name.csv"))
    for d in c:
        if a == d[0]:
            if hesh(b)==d[1]:
                return "Welcome"
            return "Incorred Password"
    return "You need to register"





