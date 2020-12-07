# 4th_plataforma
This project is part of the Vivo challenge for new developers. It consists of 3 challenges, as follows:
Note: See ./subject for more details.

<h2><b>***** 1th *****</b></h2>
Given values from 0 to 15, generate a statistic of its occurrence in a bitmap image (which can be represented by an M x N matrix), as shown in the following figure:

![1th](images/1.png)

This challenge was developed in python.
Script: <b>prova_desenvolvedores_4p_1.py</b>
To run: $python3 prova_desenvolvedores_4p_1.py
Requirements: python v3.x instaled
  
To run unit tests:
- go to <b>./unit_tests</b> 
- run py.test to run all tests. 
  <b>(unit_tests)$ py.test</b>
  (Or py.test name_of_file.py to run a particular test.)
- Note: You must have pytest installed on your machine. See https://docs.pytest.org/en/stable/ for instructions.

<b>$ py.test</b>
![1th](images/2.png)

<h2><b>***** 2th *****</b></h2>

Transform the previous algorithm into a <b>Rest API</b>.
- Input parameter: list with the values
- Output: output of the algorithm in JSON format.

This API was developed on FLask Framework. 
Script: <b>prova_desenvolvedores_4p_2.py</b>
To run: $python3 prova_desenvolvedores_4p_2.py
In your browser, go to http://127.0.0.1/5000/ and follow the instructions. 
Or, for short, type the previous url followed by the space-separated values.

Note: 
- Values must be between <b>0 and 15</b>, 
- separated by <b>spaces</b>. 
- Other characters are not accepted, as well as values outside the range.

