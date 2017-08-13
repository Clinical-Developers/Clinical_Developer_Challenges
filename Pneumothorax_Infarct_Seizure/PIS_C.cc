/* */
New doctors working in a particular ED department are struggling to prioritise the management of 3 different common emergency problems if they coexist in the same patient at presentation. They are: 1) Massive Pneumothorax, 2) Ischemic shock and 3) Seizures.
stay with me on this one.
The rules are the following:
- Massive pneumothorax trumps ischaemic shock in priority because it requires a chest drain to be inserted prior to anticoagulants. 
- Uncontrolled Seizures trump pneumothorax as you need to control the seizures before the chest drain can be physically inserted. 
- Ischemic shock trumps seizures because it is probably the cause of the fits and needs to be treated as a priority.
The code should return both the priority to be treated and a single line treatment plan ;)
You can write the code however you want in whatever language you want.
Obviously this is a medical variation on rock, paper, scissors and the extremely new ED docs at this highly undersupported ED department will thank you for helping them with these highly difficult (and rare) possible clinical scenarios ;)
/* */
  
// Example program by Jeremy Thornton - CDC
  
#include <iostream>
#include <string>

int main() {
  std::cout << "What's up Doc?\n"
  << "1: pneumothorax\n"
  << "2: shock\n"
  << "3: seizures" << std::endl;
  int a, b;
  std::cin >> a >> b;
  std::cout << "First treat ";
  switch (a+b) {
    case 3:
        std::cout << "pneumothorax!";
        break;
    case 4:
        std::cout << "seizures!";
        break;
    case 5:
        std::cout << "shock!";
        break;
  }
  std::cout << std::endl;
}
