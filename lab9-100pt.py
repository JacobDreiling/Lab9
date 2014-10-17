############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.

patients = 12

while patients > 0:
    print 'Patient ' + str(patients) + ' , what is your temperature?'
    userTemp = int(raw_input())
    print 'Have you been sick in the last 24 hours? (Type "Yes" or "No")'
    userAns = raw_input()
    print 'Have you recently been to Weeeeeest Aaaaafricaa? (Type "Yes" or "No")'
    userEbola = raw_input()
    if userTemp > 105:
        print 'You must be admitted to da Krankenhaus.. dug.'
    elif userTemp > 102 and userAns == 'Yes':
        print 'You must be admitted to da Krankenhaus.. dug.'
    elif userTemp > 100 or userEbola == 'Yes':
        print 'You must be admitted to da Krankenhaus.. dug.'
    else:
        print "You haven't Elola.. dug."
    patients = patients - 1
        