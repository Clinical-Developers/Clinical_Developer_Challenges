'''
Challenge for the weekend (for those not saving lives) is as follows:
A hospital secretary prints off hundreds of case notes for an audit you are doing but for some reason everything is wrongly capitalised. This is causing havoc with the regular expressions you already wrote to read lower case string values. In any language can you define a function to quickly revert the cases of the all the notes so that you can analyse them all at once with the program you already built.
(eg. If the note reads 'dIAGNOSIS: eMPHYSEMA AND pULMONARY oEDEMA' can you in just one or two lines of code revert it back to 'Diagnosis: Emphysema and Pulmonary Oedema'. Good luck.)
'''

def changeCase(str):
    try:
        output="".join(letter.lower() if letter.isupper() else letter.upper() for letter in str)
        print(output)
    except TypeError:
        #in case a string is not passed to the function
        print("Please enter a word!")

changeCase(1)
changeCase("dIAGNOSIS: eMPHYSEMA AND pULMONARY oEDEMA")

# can also just use changecase()
