// The below will solve the puzzle for Javascript:

function inspectHospital(x){
  var flatten_x = [].concat.apply([], x);
  var count     = 0;
  flatten_x.forEach(function(e){
    if (typeof e === 'string' && e.toLowerCase() === "breach") { count += 1 } 
  });
  
  if (count > 2) {
    return 'Urgent Inspection!'
  } else if (count == 0) {
    return 'Safe'
  } else {
    return 'Trouble!'
  }
}

// level 1 - simple tests
var array1 = ['safe', 'breach', 'safe', 'safe', 'breach', 'safe', 'breach', 'breach']; // should equal 'Urgent inspection'
var array2 = ['safe', 'safe', 'safe', 'safe', 'breach', 'safe', 'safe', 'breach']; // should equal 'Trouble'
var array3 = ['safe', 'safe', 'safe', 'safe', 'safe', 'safe', 'safe', 'safe']; // should equal 'Safe'
var array4 = ['breach', 'breach', 'breach', 'breach', 'breach', 'breach', 'breach', 'breach']; // should equal 'Urgent inspection'
var array5 = ['safe', 'safe', 'safe', 'safe', 'safe', 'safe', 'safe', 'breach']; // should equal 'Trouble'

console.log(inspectHospital(array1));
console.log(inspectHospital(array2));
console.log(inspectHospital(array3));
console.log(inspectHospital(array4));
console.log(inspectHospital(array5));

// level 2 - case tests

var array6 = ['safE', 'brEach', 'safe', 'Safe', 'breach', 'SAFE', 'breach', 'BREach']; // should equal 'Urgent inspection'
var array7 = ['safe', 'safe', 'safe', 'safe', 'breach', 'sAfe', 'safe', 'brEAch']; // should equal 'Trouble'
var array8 = ['safe', 'saFE', 'safe', 'safe', 'safe', 'safe', 'safe', 'SAFE']; // should equal 'Safe'
var array9 = ['breach', 'breach', 'breach', 'BREACH', 'breach', 'breach', 'breach', 'breach']; // should equal 'Urgent inspection'
var array10 = ['safe', 'safe', 'SAFE', 'safe', 'safe', 'sAfe', 'safe', 'breach']; // should equal 'Trouble'

console.log(inspectHospital(array6));
console.log(inspectHospital(array7));
console.log(inspectHospital(array8));
console.log(inspectHospital(array9));
console.log(inspectHospital(array10));

// level 3 - nested tests

var array11 = [['safE', 'brEach', 'safe'], ['Safe', 'breach', 'SAFE'], ['breach', 'BREach']]; // should equal 'Urgent inspection'
var array12 = [['safe', 'safe', 'safe', 'safe', 'breach'], ['sAfe'], ['safe', 'brEAch']]; // should equal 'Trouble'
var array13 = [['safe', 'saFE'], ['safe', 'safe', 'safe', 'safe', 'safe', 'SAFE']]; // should equal 'Safe'
var array14 = ['breach', ['breach'], ['breach'], ['BREACH', 'breach'], 'breach', ['breach', 'breach']]; // should equal 'Urgent inspection'
var array15 = [['safe', 'safe'], 'SAFE', 'safe', ['safe'], ['sAfe'], ['safe'], 'breach']; // should equal 'Trouble'

console.log(inspectHospital(array11));
console.log(inspectHospital(array12));
console.log(inspectHospital(array13));
console.log(inspectHospital(array14));
console.log(inspectHospital(array15));

// level 4 - really nasted nested messy array provided by Peter ;-)

var array16 = ['safe', [[['SAFE', 'breach'], 'SAFE', 'breach'], 'SAFE', 'breach'], ['safE', 'breach', 'SafE', 'BREAch'], 'breach', 'safe', 'safe', 'breach', 'BreACH', 'BREach', 'SafE', [[['SAFE', 'breach'], 'SAFE', 'breach'], 'SAFE', ['SAFE', ['SAFE', 'breach'], 'breach'], 'breach', ['SAFE', ['SAFE', ['SAFE', 'breach'], 'breach'], 'breach']]]; // definitely an Urgent inspection here

console.log(inspectHospital(array16));

// # nice
