# import the required package
import requests

# valid post-code of invalid - url of the API address
url = "http://api.postcodes.io/postcodes/"

# store the data

postcode = "e147le"
url_arg = url + postcode # ("http://api.postcodes.io/postcodes/e147le")

# display the outcome
response = requests.get(url_arg)
#print(response.status_code)
response_dict = response.json()
result_dict = response_dict['result']

for key in result_dict.keys():
    if key == 'postcode':
        print(f'please confirm this is your postcode {result_dict["postcode"]}')# enter value/key that would print postcode (index number)
    elif key == 'longitude':
        print(result_dict["longitude"])
    elif key == 'latitude':
        print(result_dict["latitude"])

result_dict.keys()

    #print(key) # this prints all keys in dict
#print(result_dict)
# print the post code from the data received from the API call
print(result_dict["postcode"])

# print longitude - and latitude
print(result_dict["longitude"])
print(result_dict["latitude"])

# display url together with given postcode
print(url_arg + postcode)

# check the type of data scrapped from the web - response
print(type(postcode))
print(type(result_dict["latitude"]))
print(type(result_dict["longitude"]))

# convert data type if needed to iterate through the data and print required information

# display longitude - latitude - postcode - etc

# once completed - create a function to do return the required value - 1 function MUST only RETURN 1 value
# create a function that checks if the post code is valid - prompt the user to input the postcode

def valid_postcode():
    users_input = input("please enter postcode: ")
    if users_input != postcode:
        print("postcode entered is invalid")
    else:
        print("postcode is valid")
valid_postcode()

# create a class with all of these functions
# create a file called postcode_checker.py
# import this file and class
# call these functions in postcode_checker.py #inherticance

# create a skeleton e.g.
# def postcode_validation():
    #pass
# check the post code if it's valid or not
