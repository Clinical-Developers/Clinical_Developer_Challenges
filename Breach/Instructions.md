# Breach - 05/09/2017

<h3> Welcome to Breach </h3>
<p>
This may seem like a game, but in reality it is a fight for survival. You are given the unenviable task of assessing ED performance across the country.

You are working from home as this is where you have your system set up, and the national body has charged you to solve this problem for them.
</p>
<h4><em> You will be fed 'arrays' that central healthcare control has designed for you to assess so they can work out which hospitals to inspect!</em></h4>
<p>
Within these arrays are contained the stats on the performance of each emergency department each day of the week. A 'Breach' in this case, is when a patient had to wait over 12 hours to be assessed in ED.

They will be in the form of an array or list as below in the Python example:
</p>
<b> ['safe', 'breach', 'safe', 'safe', 'breach'] </b>

<h2> The Rules </h2>
<ol>
  <li>If a hospital has no breaches at all it is to be labelled as: <b> 'Safe' </b></li>
  <li>If a hospital has 1 to 3 they are to be labelled as: <b> 'Trouble' </b></li>
  <li>If a hospital has over 3 breaches they are to be labelled as: <b> 'Urgent Inspection' </b></li>
</ol>

<h3> Challenge Levels </h3>

<h5> Level One </h5>
To complete this level your function just has to take in clean arrays: <b> ['safe', 'breach', 'safe', 'safe', 'breach'] </b> and return the answer - job done.

<h5> Level Two </h5>
To complete this level your function has to take in messy arrays, clean them and return a result: <b> ['sAfe', 'BreaCh', 'SAFE', 'sAfe', 'bReach'] </b> # For the sake of simplicity the words will always be 'safe' or 'BREACH'.

<h5> Level Three </h5>
To complete Level Three, your function needs to handle two-dimensional or 'nested' arrays as well: <b> [['sAfe', 'BreaCh', ['SAFE', 'sAfe'], ['bReach']] </b>
<br></br>

<p>
I could take this further but I'll leave it there for now (if someone is a real smartypants and solves it in a day I might give them a level 4 mwahahaha.)
</p>

<h3> You can do it Clinician Programmer! </h3>
Here are your test cases: (Note your programs will be tested against a lot more hidden ones, but this will get you started.):
<ul>
  
  <li>['safe', 'safe, 'safe', 'safe', 'safe', 'safe', 'safe'] </li>- Should return 'Safe'
  <li>['safe', 'breach', 'safe', 'safe', 'breach'] </li>- Should return 'Trouble'
  <li>['safe', 'breach', 'safe', 'safe', 'breach', 'safe', 'safe', 'breach'] </li>- Should return 'Urgent Inspection'
  
</ul>
