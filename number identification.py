import re

def mobile_in_input(input):
    input = input.replace(" ","")
    if '+' in input:#If country code is included in input
        if '+91' in input:#If the entered country code is Indian
            input = input.replace("+91","")
        else:#If the entered country code is not Indian
            print("Please Enter Valid Mobile Number")
            return

    zero_start = re.search(".*0((9|8|7|6)\d{9}).*", input)#If number starts with 0
    indian_start = re.search(".*91((9|8|7|6)\d{9}).*", input)#If number starts with Indian country code
    standard = re.search(".*((9|8|7|6)\d{9}).*", input)#Standard number as input

    if standard:
        number = standard.group(1)
        print(number)
    elif zero_start:
        number = zero_start.group(1)
        print(number)
    elif indian_start:
        number = indian_start.group(1)
        print(number)
    elif re.search(".*(1|2|3|4|5)\d{9}.*", input):#If number starts with 1/2/3/4/5, incorrect input
        print("Enter Valid Mobile Number")

input = input("")
mobile_in_input(input)
#Run and enter user text and press enter