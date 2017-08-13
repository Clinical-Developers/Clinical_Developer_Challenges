'''

So a large district general hospital is trying to work predict how many bed days their patients will require, thus they can calculate capacity. The CQC have threatened to take them over if they don't improve.
You are the only person in the hospital who can actually code (they use contractors to do any needed maintainence/dev) They have one piece of knowledge which they can use to make predictions and that is the following:
- if a patient has stayed in hospital less than two days they are likely to stay only one more day (ie. n+1 days). 
- if they have stayed 2-7 days they are likely to stay twice that time. 
- if they have already been in hospital over a week they will normally stay 3 times that number of days on average.
Given a snapshot of the hospital at the present time, can you build a function/algorithm that can be fed all this numeric data and return the number of bed days required?
If you can solve it, you can be sure the hospital administrators will look favourably upon you when you submit that big grant proposal next month...

Date: Tuesday 27th June 2017. 
Day 1 patients: 240
Day 2 patients: 143
Day 3 patients: 490
Day 4 patients: 136
Day 5 patients: 59
Day 6 patients: 90
Day 7 patients: 20
Day 8 patients: 137
Day 13 patients: 70
Day 15 patients: 36
Day 25 patients: 26

'''


# My Version
def bed_day_calculator(n, x):
	"""Function will Calculate Bed Days."""
	if n == 0:
	    return 0
	elif n < 3:
	    return n * x + (x * 1)
	elif n < 8:
	    return (n * x) * 2
	else:
	    return (n * x) * 3
	
Total = bed_day_calculator(1, 240) + bed_day_calculator(2, 143) + bed_day_calculator(3, 490) + bed_day_calculator(4, 136) + bed_day_calculator(5, 59) + bed_day_calculator(6, 90) + bed_day_calculator(7, 20) + bed_day_calculator(8, 137) + bed_day_calculator(13, 70) + bed_day_calculator(15, 36) + bed_day_calculator(25, 26)
print(Total)

# Stefan Mitrosinovic's Version
"""
Calculating bed days.

Calculate the number of bed days depending on how
long patients have already been in the hospital.
"""


def bedDaysCalc(d):
    """Calculator for how many bed days the patient is expected to stay."""
    if d == 0:
        return 0
    elif d < 3:
        return d + 1
    elif d < 8:
        return d * 2
    else:
        return d * 3


print "Bed days calculator."
print "Please follow the instructions and only input numbers."

bedDays = 0
while True:
    try:
        print "Please input the number of days the patients have been in the hospital:"
        day = input(">")
        dayNum = abs(int(day))
        print "How many patients have been in the hospital for %d %s?" % (dayNum, "days" if dayNum > 1 else "day")
        num = input(">")
        patientNum = abs(int(num))
        bedDays = bedDays + bedDaysCalc(dayNum) * patientNum
        print "Given this snapshot, we expect %d bed days to be required" % bedDays
    except ValueError:
        print "Please type a number"
