// level 1 - simple tests
var array1 = ['safe', 'breach', 'safe', 'safe', 'breach', 'safe', 'breach', 'breach']; // should equal 'Urgent inspection'
var array2 = ['safe', 'safe', 'safe', 'safe', 'breach', 'safe', 'safe', 'breach']; // should equal 'Trouble'
var array3 = ['safe', 'safe', 'safe', 'safe', 'safe', 'safe', 'safe', 'safe']; // should equal 'Safe'
var array4 = ['breach', 'breach', 'breach', 'breach', 'breach', 'breach', 'breach', 'breach']; // should equal 'Urgent inspection'
var array5 = ['safe', 'safe', 'safe', 'safe', 'safe', 'safe', 'safe', 'breach']; // should equal 'Trouble'

console.log(test(array1));
console.log(test(array2));
console.log(test(array3));
console.log(test(array4));
console.log(test(array5));

// level 2 - case tests

var array6 = ['safE', 'brEach', 'safe', 'Safe', 'breach', 'SAFE', 'breach', 'BREach']; // should equal 'Urgent inspection'
var array7 = ['safe', 'safe', 'safe', 'safe', 'breach', 'sAfe', 'safe', 'brEAch']; // should equal 'Trouble'
var array8 = ['safe', 'saFE', 'safe', 'safe', 'safe', 'safe', 'safe', 'SAFE']; // should equal 'Safe'
var array9 = ['breach', 'breach', 'breach', 'BREACH', 'breach', 'breach', 'breach', 'breach']; // should equal 'Urgent inspection'
var array10 = ['safe', 'safe', 'SAFE', 'safe', 'safe', 'sAfe', 'safe', 'breach']; // should equal 'Trouble'

console.log(test(array6));
console.log(test(array7));
console.log(test(array8));
console.log(test(array9));
console.log(test(array10));

// level 3 - nested tests

var array11 = [['safE', 'brEach', 'safe'], ['Safe', 'breach', 'SAFE'], ['breach', 'BREach']]; // should equal 'Urgent inspection'
var array12 = [['safe', 'safe', 'safe', 'safe', 'breach'], ['sAfe'], ['safe', 'brEAch']]; // should equal 'Trouble'
var array13 = [['safe', 'saFE'], ['safe', 'safe', 'safe', 'safe', 'safe', 'SAFE']]; // should equal 'Safe'
var array14 = ['breach', ['breach'], ['breach'], ['BREACH', 'breach'], 'breach', ['breach', 'breach']]; // should equal 'Urgent inspection'
var array15 = [['safe', 'safe'], 'SAFE', 'safe', ['safe'], ['sAfe'], ['safe'], 'breach']; // should equal 'Trouble'

console.log(test(array11));
console.log(test(array12));
console.log(test(array13));
console.log(test(array14));
console.log(test(array15));
