#RULES 
#Camel case for ALL variables 
#Each individual process as it's own function
#all possible inputs accounted for



                    #INPUTS MESSAGE AND SHIFT 
def inputMessage(): 
    print("What is the message that you want to encrypt") 
    message = input("")
    return message 
def inputShift():
    x = 0
    while x != 1: 
        print("What is the shift for the message that you want (between 1 and 26) ")
        shift = int(input()) 
        if shift > 26 or shift < 1:
            continue 
        else: 
            x = x + 1 
    return shift 


def messageToAscii(): 
    #converts to ascii
    ascii_message = ascii(message)
    return ascii_message

def asciiShift():
    asciiShift = [''] 
    for c in messageToAscii(): 
        oldInt = ord(c.lower())
        newInt = ord(c.lower()) + shift
        if oldInt >= 97 and oldInt < 122:
            if newInt > 122:
                newNewInt = newInt - 26 
                asciiShift.append(chr(newNewInt))
            else: 
                asciiShift.append(chr(newInt))
        else: 
            asciiShift.append(c) 
    encryptedMessage = "".join(str(x) for x in asciiShift)

    return encryptedMessage


#variables returned 
message = inputMessage()
shift = inputShift()
ascii_message = messageToAscii()
encryptedMessage = asciiShift()
print("Orginial message = ", message.lower()) 
print("Encrypted message = ", encryptedMessage )
