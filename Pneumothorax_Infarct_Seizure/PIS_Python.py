'''
New doctors working in a particular ED department are struggling to prioritise the management of 3 different common emergency problems if they coexist in the same patient at presentation. They are: 1) Massive Pneumothorax, 2) Ischemic shock and 3) Seizures.
stay with me on this one.
The rules are the following:
- Massive pneumothorax trumps ischaemic shock in priority because it requires a chest drain to be inserted prior to anticoagulants. 
- Uncontrolled Seizures trump pneumothorax as you need to control the seizures before the chest drain can be physically inserted. 
- Ischemic shock trumps seizures because it is probably the cause of the fits and needs to be treated as a priority.
The code should return both the priority to be treated and a single line treatment plan ;)
You can write the code however you want in whatever language you want.
Obviously this is a medical variation on rock, paper, scissors and the extremely new ED docs at this highly undersupported ED department will thank you for helping them with these highly difficult (and rare) possible clinical scenarios ;)
'''

def in_extremis_decision_aid(PC1, PC2): #For use when confronted with the classic dual pathology of 'popped_lung' and ischaemic injury or fits ;)
    if PC1 == 'Massive Pneumothorax' and PC2 == 'Uncontrolled Seizures':
        return 'Treat the Seizures First with Diazepam & a 18mg/Kg Leviceractam loading dose'
    elif PC1 == 'Uncontrolled Seizures' and PC2 == 'Ischaemic Shock':
        return 'Treat the Ischaemia First with Antiplatelet/Heparin/Thrombolysis - call cardiologist/respiratory consultant'
    elif PC1 == 'Ischaemic Shock' and PC2 == 'Massive Pneumothorax':
        return 'Treat the Pneumothorax First with Emergency needle aspiration followed by chest drain insertion'
    elif PC1 == 'Uncontrolled Seizures' and PC2 == 'Massive Pneumothorax':
        return 'Treat the Seizures First with Diazepam & a 18mg/Kg Leviceractam loading dose'
    elif PC1 == 'Ischaemic Shock' and PC2 == 'Uncontrolled Seizures':
        return 'Treat the Ischaemia First with Antiplatelet/Heparin/Thrombolysis - call cardiologist/respiratory consultant'
    elif PC1 == 'Massive Pneumothorax' and PC2 == 'Ischaemic Shock':
        return 'Treat the Pneumothorax First with Emergency needle aspiration followed by chest drain insertion'
    elif PC1 == 'Uncontrolled Seizures' and PC2 == 'Uncontrolled Seizures':
        return 'Treat the Seizures with Diazepam & a 18mg/Kg Leviceractam loading dose'        
    elif PC1 == 'Massive Pneumothorax' and PC2 == 'Massive Pneumothorax':
        return 'Treat the Pneumothorax with Emergency needle aspiration followed by chest drain insertion' 
    elif PC1 == 'Ischaemic Shock' and PC2 == 'Ischaemic Shock':
        return 'Treat the Ischaemia with Antiplatelet/Heparin/Thrombolysis - call cardiologist/respiratory consultant'        
    else:
        return 'Apologies, These conditions are not extreme enough for the in_extremis decision aid, please pick up your Cheese and Onion'

in_extremis_decision_aid('Massive Pneumothorax', 'Ischaemic Shock')
in_extremis_decision_aid('Uncontrolled Seizures', 'Uncontrolled Seizures')

# see it in action at: https://goo.gl/r3QrFZ


"""
Medical Rock Paper Sissors.

Quick and dirty task from
https://www.facebook.com/groups/257859457974818/

Done by Stefan Mitrasinovic in the CDC
"""
print "What conditions do your patients have?"
cond1 = "Massive Pneumothorax"
cond2 = "Uncontrolled Seizure"
cond3 = "Ischemic Shock"
print """
1) %s
2) %s
3) %s
""" % (cond1, cond2, cond3)


def conditionSaver(num):
    """Return condition number."""
    while True:
        try:
            temp = abs(int(input("Patient %d: " % num)))
            if temp > 3 or temp == 0:
                raise ValueError
            return temp
        except ValueError:
            print "Please input a number (1-3) for the condition."


patient1 = conditionSaver(1)
patient2 = conditionSaver(2)


def printChoice(condition):
    """Print the correct condition to treat first."""
    print "You should treat the patient with the %s first" % condition


condCode = patient1 + patient2
if condCode == 3:
    printChoice(cond2)
elif condCode == 4:
    printChoice(cond1)
elif condCode == 5:
    printChoice(cond3)
else:
    print "Something went wrong"

