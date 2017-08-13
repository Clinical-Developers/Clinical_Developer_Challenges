# version by Adam Morley

var priority, plan, mp, is, us; 

mp = true;
is = false;
us = true;

if (mp && is){
	priority = 'massive pneumothorax';
	plan = 'Insert chest drain.';
}else if (us && mp){
	priority = 'uncontrolled seizures';
	plan = 'Control seizures';
}else if (is && us){
	priority = 'ischaemic shock';
	plan = 'Treat shock.';
}

console.log ('Priority - the '+priority+'. Treatment plan: '+plan); 
