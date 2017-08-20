![no expect](https://cldup.com/_J15R6UgNI.png)

# Phone Call Challenge #

Another challenge brought to you by the Clinical Developer's Club [Facebook Page](https://www.facebook.com/groups/257859457974818/) - This one by our esteemed member Jeremy Thornton also known as @ifknot - https://github.com/ifknot

### Introduction ###

The NHS faces huge and worsening patient access challenges in Accident & Emergency, Hospital clinics and, of course, General Practice. This challenge is designed to explore one fictional part of the patient access problem and allow you to experiment with some real NHS data in a fictional context. All of this data is historic and otherwise redundant. This data has been released to Clinical Developers Club for research purposes as open source data under the  Creative Commons Licence: Attribution Non-Commercial No Derivatives (CC BY-NC-ND) [Summary Link](https://creativecommons.org/licenses/by-nc-nd/4.0/)

### The Scenario

Fictional Group Practice (FGP) is a busy inner city practice of 8000+ patients. They have discovered that their call handling system keeps statistics on the phone calls that they receive - there is no patient identifiable information nor phone numbers stored - and they would like to put all this data to good use, can you help them?

### The Challenge ###

Using any software or programming language that you prefer can you...

- #### Level 1 ####

  - [ ] Analyse one day's worth of data from the group statistics and agents statistics for the Tuesday after Easter Monday? 


  - [ ] What can you tell the practice to help FGP improve patient access and advise on staffing levels for days after bank holidays?

- #### Level 2 ####

  - [ ] Analyse and visualize *all* of the data that FGP has available to them? 


  - [ ] What can you tell the practice and how do your visualisation(s) help them understand what you have discovered in order to help them improve the patient access challenges that they face?

- #### Level 3 ####

  - [ ] Model all of the data that FGP has available to them?


  - [ ] Use the model to create a predictive dashboard to visualize past and future call data that can predict the impact of, for example, staffing levels on patient access?

### How The Practice Works

To help you with this challenge and understand the data files here is how the FGP reception and staffing works...

Every morning at 0800h the surgery opens and phones switch over from the Out of Hours service and patients start arriving for booked appointments, to make appointments and make general queries. 

Under full staffing there will be 2 receptionists manning the front 'Reception' desk taking phone calls and handling face to face encounters - there is also 1 or 2 members of the reception team working in the 'Back Office'.

There is one number to call FGP, so the call first goes to the agent 'Reception L1', if that line is busy it is automatically transferred to agent 'Reception Desk', and so on to 'Back Office1' and finally, if it is staffed, to the 'Back Office3' agent.

### Data Structures

There are 2 file types:

1. Agent Statistics - Describe the performance of individual call handling 'agents' and consists of: 
   - agent name
   - number of calls handled 
   - number of calls unanswered (remember these will be bounced on to the next agent)
   - average call time
   - total talk time
   - total staffed time.
2. Group Statistics - Describe the performance of the whole 'group' of all of the call handling 'agents' and consists of:
   - timestamp
   - number of busy overflows
   - number of calls answered
   - number of calls abandoned 
   - number of calls transferred
   - number of calls timed out 
   - average number of agents talking 
   - average number of agents staffed 
   - average wait time 
   - average abandonment time

### Licence 

Released under Creative Commons Licence: Attribution Non-Commercial No Derivatives (CC BY-NC-ND [Licence Link](https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode)

#### You are free to:

**Share** � copy and redistribute the material in any medium or format.

The licensor cannot revoke these freedoms as long as you follow the license terms.

#### Under the following terms:

- **Attribution** � You must give [appropriate credit](https://creativecommons.org/licenses/by-nc-nd/4.0/#), provide a link to the license, and [indicate if changes were made](https://creativecommons.org/licenses/by-nc-nd/4.0/#). You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **NonCommercial** � You may not use the material for [commercial purposes](https://creativecommons.org/licenses/by-nc-nd/4.0/#).
- **NoDerivatives** � If you [remix, transform, or build upon](https://creativecommons.org/licenses/by-nc-nd/4.0/#) the material, you may not distribute the modified material.





