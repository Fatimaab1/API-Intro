import requests

response = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews") # API call to BBC to get response
#print(response)

# if the web-page status code is live welcome the user with the status
#if response.status_code == 200: # if true execute the next line if false execute next block
   # print(f"The status code is {response.status_code} welcome to BBC")
   # print(type(response.content)) # get the content from the web-app/endpoint
# find a way to change this type to json or dict or list or any type which we could
# iterate through loops

#else:
    #print(f"OOPs something went wrong, the status code is {response.status_code} Please try later")




# or print a message OOPs something went wrong
# should give us the status code only - number 200 - 404 - 501 etc

# second iteration -
#if response: # what is it checking
   # print("success")
#elif response.status_code == 404: # what is it checking
   # print("unsuccessfull")

#else: # what is it checking
    #print(f"fOOps something went wrong please try later the status code is {response.status_code}")


# Third iteration
# create a function that returns the status code with appropriate message
# use control flow to make the right decision
# USE RETURN not print inside your function

def return_status_code ():
    if response.status_code == 200:
        return f"The status code is {response.status_code} welcome to BBC"
    elif response.status_code == 404:
        return f"OOPs something went wrong, the status code is {response.status_code} Please try later"
    else:
        return "There seems to be a problem"

print(return_status_code())