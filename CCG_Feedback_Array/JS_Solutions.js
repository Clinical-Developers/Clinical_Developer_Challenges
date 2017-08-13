/*

Challenge:

Challenge: The CCG has a problem. They have done a survey of all the primary care patients in their region. The survey had a score from 1 to 10 asking patients to rate their care. All this data has been uploaded to a central computer system. Unfortunately, some silly folk have decided to put some silly numbers like -100 or 50 in the box. Can you write a simple function that will exclude all these outliers and sum up the totals that fit within the instructions of the survey?
The CCG were going to ask PWC to sort this out for them at a cost of £20,000 but you have offered to do faster and better for consulting fees of just £4,000; Meanwhile offering to throw in a little analysis of your own 😉
A sample of the CCG's array is given below:
([1,5,7,81,1,4,7,8,-34,96,2,5,8,1,-124,753,9,5,4,3,13,7,90,5,1,4,8,3,6,7,7,8,500,-100,2,6,7,2,9,1,8,9,3,6])
Your code function should come up with an answer to this array, and then the CCG will be happy to commission you. If you get the answer right you will get a shoutout next time as long as your solution is at least an improvement on / variation of someone else's. Bonus credit will be given for extra miles travelled 

# Versions Below:

Stefan Mitrosinovic

Survey Filter Challenge.
Build a function to check an array for true values
then find the mean over the results.
*/

const votes = [1,5,7,81,1,4,7,8,-34,96,2,5,8,1,-124,753,9,5,4,3,13,7,90,5,1,4,8,3,6,7,7,8,500,-100,2,6,7,2,9,1,8,9,3,6];

const surveyCalculator = (arr) => {
  // Filter results and calculate mean.
  console.log(`There are ${votes.length} survey scores`);
  const filtered = arr.filter(x => x >= 1 && x <= 10);
  console.log(`There were ${votes.length - filtered.length} invalid survey results`);
  const sum = filtered.reduce((a,b) => a+b, 0);
  console.log(`There is a total score of ${sum}`);
  const mean = sum / filtered.length;
  console.log(`Which results in a mean of ${mean.toFixed(2)}`);
}

# Adam Morleys Version

surveyCalculator(votes);

var votes = ([1,5,7,81,1,4,7,8,-34,96,2,5,8,1,-124,753,9,5,4,3,13,7,90,5,1,4,8,3,6,7,7,8,500,-100,2,6,7,2,9,1,8,9,3,6]);
var x = 0;
var y = 0;

function antiScam(arr){
  for(var i of arr){
    i>=1 && i<=10 ? x = x + i : y++;  
  }
  console.log('Total:' + x);
  console.log('Average:' + x/(votes.length-y));
  console.log('Number of scam attempts:' + y);
}

antiScam(votes);

# David Anderson's version:

console.log(
  [1,5,7,81,1,4,7,8,-34,96,2,5,8,1,-124,753,9,5,4,3,13,7,90,5,1,4,8,3,6,7,7,8,500,-100,2,6,7,2,9,1,8,9,3,6].reduce((carry,vote) => {
      return carry + (vote <= 10 && vote >= 1 ? vote : 0)
    })
);
