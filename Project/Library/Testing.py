# Author(s):	Eden Jack
# Date Created: 07/03/2024
# Date Edited:	13/03/2024
# Description:  This module hosts the code used to help test, we can use this module to create different tests for the application


#==================================
#       TRUE/FALSE testing
#==================================
# Test functions from the testing.py module, provided in Week 17

# Standard True/False test response. Code works, but check it operates as expected.
def Test_Expected(Expected, Func, *Args):
    if Args == None:
        return Func() == Expected
    else:
        return Func(*Args) == Expected

# test_multiple() function accepts a list of calls to 
# the test() function and returns the percentage of successfully
# passed tests.
#
# The call to test_multiple() can look something like this:
# tests = [
#   test(5, add, [3, 2]),
#   test('Hannah', name),
#   test('Hello, James!', greet, ['James'])
# ]
# test_multiple(tests)

def Test_Multiple(tests):
   return sum(tests) / float( len(tests) ) * 100

#==================================
#       INPUT RESPONSE testing
#==================================
# Custom cross-module sequential input testing, requires all tested inputs to be changed to t_input.
# Useful if multiple pieces of code are expected to run in sequence of one another, affected by the user, but not directly interacting with one another.

# InputPopper; sets up a global variable for "InputList" with the given Input sequence.
    # Example: InputList = SetInputPopper(12, 3, 1234, "A")
    # This would then mimic a sequence of inputs as "12", then the next input() as 3, then 1234, then "A"
    # As this is a global variable stored within this module, it can be called across multiple modules.
def SetInputPopper(*Args):
    global InputList 
    InputList = [*Args]
    return InputList


# Test_input; useful for creating a "pseudo-input". If a user is expected to input something sequentially, this allows for that "expected" sequence to be tested.
    # Inputs happen linearly, and only handle the expected "input" calls. 
    # A global "InputList" is required, via SetInputPopper.
    # This will work across multiple calling modules, as well as releasing the program after use.
        # TakeInput is just a debounce checker
        # InputList check is a protected error case.
def t_input(Prompt):
  TakeInput = False
  try:
     ThisVal = InputList.pop(0)
  except:
    TakeInput = True
  finally:
    if TakeInput:
      ThisVal = input(Prompt)
    else:
      print(Prompt, ThisVal)
  return ThisVal
        