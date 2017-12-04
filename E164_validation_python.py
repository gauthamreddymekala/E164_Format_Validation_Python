#converts the number to E164 format
def E164(a):
    print("+1"+ a) 

phn = input("please enter the phone number")
#checks if number is valid
validate = phn.isnumeric()

if(validate and len(phn)== 10):
    E164(phn)
else:
    print("Phone number is not valid")
    
    