'''

My rough and ready solution with minimal analysis - this will be fleshed out later

Challenge: The CCG has a problem. They have done a survey of all the primary care patients in their region. The survey had a score from 1 to 10 asking patients to rate their care. All this data has been uploaded to a central computer system. Unfortunately, some silly folk have decided to put some silly numbers like -100 or 50 in the box. Can you write a simple function that will exclude all these outliers and sum up the totals that fit within the instructions of the survey?
The CCG were going to ask PWC to sort this out for them at a cost of £20,000 but you have offered to do faster and better for consulting fees of just £4,000; Meanwhile offering to throw in a little analysis of your own 😉
A sample of the CCG's array is given below:
([1,5,7,81,1,4,7,8,-34,96,2,5,8,1,-124,753,9,5,4,3,13,7,90,5,1,4,8,3,6,7,7,8,500,-100,2,6,7,2,9,1,8,9,3,6])
Your code function should come up with an answer to this array, and then the CCG will be happy to commission you.

'''
4,3,13,7,90,5,1,4,8,3,6,7,7,8,500,-100,2,6,7,2,9,1,8,9,3,6]

CCG_raw_count = len(CCG_Array)
CCG_raw_sum = sum(CCG_Array)
print(CCG_raw_count)
print(CCG_raw_sum) # Wowswer this is a crazy number

# But this is useless given the outlying values

def CCG_feedback(arr):
    sum = 0
    for score in arr:
        sum += score if score>0 and score<11 else 0
    return sum
    
CCG_sum = CCG_feedback(CCG_Array)

# Now we need to know the valid count of which these feedback values are made up

def CCG_condition(score):
    return score>0 and score<11
    
def CCG_feedback_count(x):
    return sum(1 for x in CCG_Array if CCG_condition(x))
    
CCG_valid_count = CCG_feedback_count(CCG_Array)

print(CCG_sum)
print(CCG_valid_count)
CCG_mean = CCG_sum / CCG_valid_count
print(CCG_mean)


