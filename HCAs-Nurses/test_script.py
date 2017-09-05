import unittest
from random import randint

def solution(staff_units, patients):
    try:
        return max(((i, staff_units-i) for i in range(staff_units+1) if 2*i+4*(staff_units-i) == patients))
    except ValueError:
        return "This hospital is in trouble!"

def staffing(staff_units, patients):
    HCA, nurse = 2*staff_units-patients/2, patients/2-staff_units
    if HCA < 0 or nurse < 0 or not HCA == int(HCA) or not nurse == int(nurse):
        return "This hospital is in trouble!"
    return HCA, nurse

class TestStaffingSimple(unittest.TestCase):

    def test_staffing(self):
        print('Testing Definite Success Cases')
        self.assertEqual(staffing(72, 200), (44, 28)),
        self.assertEqual(staffing(72, 200), (44, 28)),
        self.assertEqual(staffing(116, 282), (91, 25)),
        self.assertEqual(staffing(12, 24), (12, 0)),
        self.assertEqual(staffing(6, 24), (0, 6)),
        self.assertEqual(staffing(344, 872), (252, 92)),
        self.assertEqual(staffing(158, 616), (8, 150)),
        print('Testing Failure Cases')
        self.assertEqual(staffing(25, 555), "This hospital is in trouble!"),
        self.assertEqual(staffing(12, 25), "This hospital is in trouble!"),
        self.assertEqual(staffing(54, 956), "This hospital is in trouble!")
        print('Testing Edge Cases')
        self.assertEqual(staffing(0, 0), (0, 0))
        self.assertEqual(staffing(-1, -1), "This hospital is in trouble!")
        self.assertEqual(staffing(500, 0), "This hospital is in trouble!")
        self.assertEqual(staffing(0, 500), "This hospital is in trouble!")
        self.assertEqual(staffing(-45, 5), "This hospital is in trouble!")
        self.assertEqual(staffing(5, -55), "This hospital is in trouble!")

class TestStaffingRandom(unittest.TestCase):
    def test_random_staffing(self):
        print('Testing Random Cases')
        for _ in range(20):
            i, j = randint(-100, 1000), randint(-100, 1000)
            print("Mixed testing for (%s, %s)" % (i, j))
            self.assertEqual(staffing(i, j), solution(i, j),"It should work for random inputs too")
        s = 0
        while s!= 30:
          i, j = randint(0, 1000), randint(0, 1000)
          if solution(i, j) != "This hospital is in trouble!":
            print("Valid testing for (%s, %s)" % (i, j))
            self.assertEqual(staffing(i, j), solution(i, j),"It should work for random inputs too")
            s+=1
        s = 0
        while s!= 10:
          i, j = randint(0, 1000), randint(0, 1000)
          sol = solution(i, j)
          if sol != "This hospital is in trouble!":
            print("Invalid testing for (%s, %s)" % (-i, -j))
            self.assertEqual(staffing(-i, -j), "This hospital is in trouble!","It should work for random inputs too")
            s+=1

if __name__ == '__main__':
    unittest.main()
