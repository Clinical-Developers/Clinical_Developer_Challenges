# Challenge: week beginning 27/8/17:

This is a clinical variation on a popular programming puzzle:

Anyonymous General has a problem. They know they need to staff their hospital with the appropriate number of nurses and HCA's.

Both Nurses and HCA's count as one staff-unit in the calculation: However, in this hospital:

A Nurse is always responsible for 4 patients.
Whilst an HCA is always responsible for 2 patients.
Given a number of staff-units and patients in the hospital can you calculate the number of nurses and HCA's there must be in that hospital. If any value/result is negative, there is no soution or the calculation returns a float then return: "Your hospital's got problems!". 0,0 however should return [0,0].

In Python the result should return a tuple - (Heads, Legs) or in any other language an array or list - [Heads, Legs]/{Heads, Legs}.

e.g

(Staff-Units, Patients) = (6, 24)

So - (6, 24) => should return (0 , 6) (HCA's, Nurses)

However - (6, 25) => "Your hospital's got problems!"

the function should be called staffing:

so in Python for instance it should begin: def staffing(staff-units, patients):

There are many ways to solve it, so just because someone else did it one way doesn't mean there are not good alternatives also available.

Happy clinician coding!
