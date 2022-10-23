# 26.	The payment card is secured with a four-digit PIN code (0805). Write a 
# program that checks if the PIN code entered in the payment terminal is correct. 
# The user has up to three possibilities for entering a PIN code. In case of 
# three unsuccessful attempts, the card is blocked.

code = "0805"
attemps = 0
while attemps != 3:
    pin = input("Enter the PIN code: ")
    if pin == code:
        print("PIN correct")
        break
    else:
        print("Incorrect")
        attemps += 1
    
    if attemps == 3:
        print("Sorry, your payment card has been blocked.")