# Author(s):	Eden Jack
# Date Created: 07/03/2024
# Date Edited:	07/03/2024
# Description:  This module hosts some basic functions that allow us to solve how each logic gate impacts a given equation.

##Expected "Inputs" tables
#TestInput = {
#    "A": True,
#    "B": False,
#    "C": False,
#    "D": True
#}

## AND_Gate - AND, if both are true
def AND_Gate(Inputs):
    # Iterate through each input, track if they are all true. 
    # If any result is False, it trips the "TrueResults" variable to False.
    TrueResults = True
    for Key in Inputs:
        Value = Inputs[Key]
        if Value == False:
            TrueResults = False

    # Return results
    if TrueResults:     # If the result is true
        return True     # Return true
    else:               # If the statement isn't true
        return False    # return false
    
## NAND_Gate - Not AND, inverts the given result of an AND gate.
def NAND_Gate(Inputs):
    F = not AND_Gate(Inputs) # Call the AND_Gate, and invert!
    return F

## OR_Gate - OR, either or both
def OR_Gate(Inputs):
    # Iterate through each input, track if they are all true.
    # If any result is true, then we have a successful "OR", set the TrueResult to True
    TrueResults = False
    for Key in Inputs:
        Value = Inputs[Key]
        print(Key, Value)
        if Value == True:
            TrueResults = True

    # Return results
    if TrueResults:     # If the result is true
        return True     # Return true
    else:               # If the statement isn't true
        return False    # return false
    

## XOR_Gate - Exclusive Or gate, only if 1 result is true.
def XOR_Gate(Inputs):
    # Iterate through each input, track if they are all true.
    # If a given result is true, and a the current TrueResult is false, then consider us to be true
    # If then *another* result is true, we are false.
    TrueResults = False
    for Key in Inputs:
        Value = Inputs[Key]
        if Value == True and TrueResults == False:
            TrueResults = True
        elif Value == True and TrueResults == True:
            TrueResults = False
            break # Exit the loop early, no need to continue if we are going to be false

    # Return results
    if TrueResults:     # If the result is true
        return True     # Return true
    else:               # If the statement isn't true
        return False    # return false
    

## NOR_Gate - Invert of an OR gate
def NOR_Gate(Inputs):
    F = not OR_Gate(Inputs) # Call the OR_Gate, and invert!
    return F

###Run a quick test
TestInput = {
    "A": True,
    "B": False,
    "C": False,
    "D": True
}

print(OR_Gate(TestInput))