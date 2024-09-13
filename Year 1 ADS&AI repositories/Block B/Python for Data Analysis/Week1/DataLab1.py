# Week 1, DataLab 1

# Q.1 Write a Python function to return "Hello World!"

def hello_world():
    #print("Hello World!")
    return("Hello World!")

##########################################################################################################

# Q.2 Write a Python function which:
#accepts a given number as a function parameter.
#checks if the given number is even or odd.
#prints "even" if the number is even.
#prints "odd" if the number is odd.
#has a default value of 7 if no number if supplied.

def even_or_odd(number = 7):
    if number %2 == 0:
        return 'even'
    return "odd"

##########################################################################################################

# Q.3 Write a python function to classify people as either 
#adults (greater than or equal to 18 years old) or 
#children (less than 18 years old)

def adult_or_child(age):
    if age >= 18:
        return 'adult'
    return 'child'


##########################################################################################################

# Q.4 RIVM Vaccine Registration
## Write a Python function which prints out the vaccine registration date, vaccine and location for a user supplied year of birth.

def rivm(dob):
    location = {
        '1931 or earlier' : 'Groningen',
        '1932 - 1936' : 'Arnhem',
        '1937 - 1941' : 'Breda',
        '1942 - 1946' : 'Harlingen',
        '1947 - 1951' : 'Edam',
        '1952 - 1955' : 'Amsterdam',
        '1956 - 1957' : 'Sittard',
        '1958 - 1960' : 'Rotterdam',
        '1961 - 1971' : 'Groningen',
        '1972 - 1981' : 'Arnhem',
        '1982 - 1991' : 'Breda',
        '1992 or later' : 'Maastricht'
    }
    return location[dob]