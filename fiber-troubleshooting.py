#This script helps to identify issues with fiber runs based off of readings taken from a certified light measuring device.

#Step 1: Gathers user input for light power readings and stores them as variables.
hosttx = input("Enter the dBm reading of the SFP on the HOST side [ex. -2.8]")
hostrx = input("Enter the dBm reading of the CABLE on the HOST side [ex. -2.8]")
switchtx = input("Enter the dBm reading of the Switch SFP/Panel? [ex. -2.8]")
switchrx = input("Enter the dBm reading of the CABLE at the Switch SFP/Panel? [ex. -2.8]")
matching = input("Do these readings closely match the SFP/Switch output readings(+ or - 0.1 dB)? (0 = No, 1 = Yes, 2 = Unknown)")

#Step 2: Performs loss calculations and declaring variables used later.
hostloss = hosttx - switchrx
switchloss = switchtx - hostrx
cablepass = 0
txpass = 0
rxpass = 0

#Step 3: Running tests based on user inputs and saving to the variables from step 2.
#Step 3.1: Tests if the cable passed
if hostloss > -1.5 and switchloss > -1.5:
        cablepass = True
else:
        cablepass = False

#Step 3.2: Tests if the Tx was passing.
if hosttx > -4.5 and switchtx > -4.5:
        txpass = True
else:
        txpass = False

#Step 3.3: Tests if the Rx was passing.
if matching == 1:
        rxpass = True
elif matching == 2:
        rxpass = "Unknown"
elif matching == 0:
        rxpass = False
else:
        print "You did not choose a supported answer when asked if the readings match support outputs."

#Step 4: Begins the output sequence.
print "\nThe following is the prefab to send Support...\n\n"
#Prints the user inputted variables.
print "Hello,\n\nFiber and SFPs have been tested as follows:\n\nHost Tx: ",hosttx," dBm\nHost Rx: ",hostrx," dBm\nSwitch Tx: ",switchtx," dBm\nSwitch Rx: ",switchrx," dBm\ndB Loss from Host to Switch: ",hostloss," dB\ndB Loss from Switch to Host: ",switchloss," dB\n"
#Prints test results.
print "Cabling passed test: ",cablepass,"\nSFP transmitters are healthy: ",txpass,"\nSFP receivers are healthy: ",rxpass,"\n"

#Selects action plan based on Step 3 results.
if cablepass == True and txpass == True and matching == True:
        print "No Layer 1 issues -> HBA is likely the culprit but doesn't rule out SFPs. Swap SFPs and monitor for additional issues, if issue persists schedule HBA replacement."
elif cablepass == True and txpass == True and matching == False:
        print "Faulty SFP RX module, whichever SFP shows a discrepancy between meter readings and OS/Switch readings needs replaced."
elif cablepass == True and txpass == False and matching == True:
        print "Any SFP that doesn't match reported Rx from OS/Switch and actual Meter readings or has Tx lower than -5.2dBm needs replaced."
elif cablepass == False and txpass == False and matching == False:
        print "All layer 1 components need replaced or further investigation is required."
elif cablepass == False and txpass == True and matching == False:
        print "Cabling and any SFPs with Rx discrepancy needs replaced."
elif cablepass == False and txpass == False and matching == True:
        print "Cabling and any SFPs with low Tx need replaced."
elif cablepass == False and txpass == True and matching == True:
        print "Cabling is faulty or connections are loose and need fixed."
elif matching == 2:
        print "\n\nIf the 3rd answer is unknown, a support tech will need to check those readings at the OS/Switch level with the cable plugged in. This testing only works if the SFPs are broadcasting. This likely is not required if an obvious cabling issue is identified but is worth review."
else:
        print "There was a mistake that put you here. Please review your inputs."


#Deprecated sections:
#Prints an extra statement if no readings from support.
#if matching == 2:
#       print "\n\nIf the 3rd answer is unknown, a support tech will need to check those readings at the OS/Switch level with the cable plugged in. This testing only works if the SFPs are broadcasting. This likely is not required if an obvious cabling issue is identified but is worth review."

#Prints ALL action plan options
#print "\n\nTrue,True,True = No Layer 1 issues -> HBA is likely the culprit but doesn't rule out SFPs. Swap SFPs and monitor for additional issues, if issue persists schedule HBA replacement.\nTrue,True,False = Faulty SFP RX module, whichever SFP shows a discrepancy between meter readings and OS/Switch readings needs replaced.\nTrue,False,True = SFPs with low TX need replaced\nTrue,False,False = Any SFP that doesn't match reported RX from OS/Switch and actual Meter readings or has TX lower than -5.2dBm needs replaced\nFalse,False,False = All layer 1 components need replaced or further investigation is required.\nFalse,True,False = Cabling and any SFPs with RX discrepancy needs replaced\nFalse,False,True = Cabling and any SFPs with low TX need replaced\nFalse,True,True = Cabling is faulty or connections are loose and need fixed"