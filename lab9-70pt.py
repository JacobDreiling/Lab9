############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer

print 'Enter an Temperature value in Celcius to be converted to Fahrenheit.'

userTemp = int(raw_input())

fahrenTemp = userTemp * 9 / 5

fahrenTemp = fahrenTemp + 32

print 'That temperature in Fahrenheit is ' + str(fahrenTemp) + '.'