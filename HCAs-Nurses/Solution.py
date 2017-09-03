# This is a maths problem not primarily a progamming one.
# As such the solution function call might look like this:

def staffing(staff_units, patients):
    HCA, nurse = 2*staff_units-patients/2, patients/2-staff_units
    if HCA < 0 or nurse < 0 or not HCA == int(HCA) or not nurse == int(nurse):
        return "No solutions"
    return HCA, nurse

'''   
So the equation is balanced as follows 

with HCAs/nurses expressed as x and y respectively and staff_units and patients expressed as s and p respectively:

x = s*2 - p/2
y = p/2-s

But, there is no need to work them both out. Once you have calculated HCA's for instance you can just do:

y = s-x

since you know that s-x must leave only remainder y. If it doesn't then you have a problem and the equation can't be solved!
'''

# Programmatically this can be more clearly be expressed as:

def staffing(staff_units, patients):
    HCA = 2*staff_units-patients/2
    nurse = staff-units-HCA
    if HCA < 0 or nurse < 0 or HCA != int(HCA):
        return "No solutions"
    return HCA, nurse
    
# if you still don't believe me check out this repl: https://repl.it/Kewn/2
