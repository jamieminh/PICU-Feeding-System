# PICU-Feeding-System
## Coursework for Design and Analysis of Data Structures and Algorithm module

### Feeding young patients in a Pediatric Intensive Care Unit
  - The attached flowchart shows the decision making process for feeding patients in paediatric intensive care units (PICU) in a hospital.
  - Patients, depending on their condition, are classed as High Risk or Low Risk as shown in attached feeding decision making chart. Any other category is to be ignored. Patients are assessed by specialist nurses every few hours and their feeding maybe adjusted based on
the various data that are recorded.
  - The hospital is looking to create a decision support system for the nurses to allow for speed, accuracy and consistency of the process. You are required to produce the core of the system that processes the data and allows the nurse to make an informed decision, quickly and
consistently

![PICU deccision making flowchart](https://i.imgur.com/KNGCtaK.jpg)

### Task 1
 - Given the attached flowchart, design suitable data structure(s) to employ and develop the
algorithm to support this decision making process. Produce detailed pseudocode and / or
relevant design diagrams - UML or any other equivalent.

### Task 2
 - Save new data per patient as it is created in the cycle of evaluation indicated in the
flowchart. Utilise the new data together with the data provided in each file to complete 5
day cycle of evaluation and feeding.
 - At the end of a 24 hour period, print on screen an update showing each patient’s
progress as they are fed and assessed through each day over a period of five days.
 - At the end of the 5 day cycle, rank the list of patients at the rate improvement
they’ve shown and identify those who show lack of progress and they need to be referred to
dieticians and specialist clinicians. At the top of a list you should show the patients that have
been progressing their feeding regularly. These should be followed by patients that have
had their feeding by one or more stoppages. Finally at the bottom of the list you should
show the patients that have had to be evaluated by a dietician as their feeding had to be
stopped for more than 8 hours.

 - Notes. A normal GRV should below 5ml x Patient weight in Kgs, or less than 250ml for
children heavier than 40kgs. q2h – stands for every 2 hours.

### Task 3
 - Evaluate your design & implementation as to the effectiveness of the solution and
the efficiency of the tools (data structures & algorithms) employed.
 - Discuss the concept of security of the data used here and the legal concerns. What
should the hospital be doing to secure the data to be compliant with GDPR and other
legislation in the UK?
