# Adam Morley's Version

var arr = [
    {Day: 1, patients: 240},
    {Day: 2, patients: 143},
    {Day: 3, patients: 490},
    {Day: 4, patients: 136},
    {Day: 5, patients: 59},
    {Day: 6, patients: 90},
    {Day: 7, patients: 20},
    {Day: 8, patients: 137},
    {Day: 13, patients: 70},
    {Day: 15, patients: 36},
    {Day: 25, patients: 26}
  ];


var calc = function(arr){
  var total = 0;
  for(var item of arr){
    if(item.Day <3){
      total = total + item.patients;
    }else if(item.Day <7){
      total = total + (2 * item.patients); 
    }else{
      total = total + (3 * item.patients);
    }
  }
  return total;
}


alert("Total number of bed days will be " +calc(arr));
