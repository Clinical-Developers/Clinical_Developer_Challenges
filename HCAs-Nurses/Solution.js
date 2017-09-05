function staffing(staff_units, patients) {
  const nurses = patients / 2 - staff_units;
  const hca = staff_units - nurses;
  if (patients & 1 || hca > staff_units || nurses > staff_units)
    return "This hospital is in Trouble";
  else
    return [hca, nurses];
}

console.log(staffing(72,200)); // should equal 44 and 28
console.log(staffing(116,282)); // should equal 91 and 25
console.log(staffing(12,24)); // should equal 12 and 0
console.log(staffing(6,24)); // should equal 0 and 6
console.log(staffing(25,555)); // should equal "This hospital is in trouble!"
console.log(staffing(12,25)); // should equal "This hospital is in trouble!"
