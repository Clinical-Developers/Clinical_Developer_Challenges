# Challenge as before

# Simon Rodney's Solution:

import numpy as np
inputArray=np.array([1,5,7,81,1,4,7,8,-34,96,2,5,8,1,-124,753,9,5,4,3,13,7,90,5,1,4,8,3,6,7,7,8,500,-100,2,6,7,2,9,1,8,9,3,6])
sanitised = inputArray[np.where(np.logical_and(inputArray>=1,inputArray<=10))]
print("Sum of input quizz results between 1 and 10:",np.sum(sanitised))
print("Average score of sanitised quizz results: ",round((np.sum(sanitised)/np.size(sanitised)),2))

"""
Stefan Mitrosinovic's Python Version

Survey Filter Challenge.
Build a function to check an array for true values
then find the mean over the results.
"""

results = [1,5,7,81,1,4,7,8,-34,96,2,5,8,1,-124,753,9,5,4,3,13,7,90,5,1,4,8,3,6,7,7,8,500,-100,2,6,7,2,9,1,8,9,3,6]


def survey_filter(survey):
  "Filter results and calculate mean."
  print("There are %d survey scores" % len(survey))
  filtered = list()
  for score in survey:
    temp = int(abs(score))
    if temp >= 1 and temp <= 10:
      filtered.append(temp)
  print("There were %d invalid survey results" % (len(survey) - len(filtered)))
  print("There is a total score of %d" % sum(filtered))
  print("Which results in a mean of %.2f" % (sum(filtered) / len(filtered)))
  

survey_filter(results)
