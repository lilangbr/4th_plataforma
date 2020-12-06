#This program returns the count of times that values in a vector, in order, 
#appear in a given bitmap image.
#The values in the vector are between 0 and 15.
#The bitmap image and vector are JSON files in the ./src folder.
#
#Author: Eliane Bresser Lang
#python v3.6.9
#Date: dec/06/2020

import json
import sys
from modules.get_object import get_json
from modules.search import search_element
from modules.requirements import vector_requirements
from modules.requirements import matrix_requirements

matrixMN = get_json('./src/image.json')
vectorAn = get_json('./src/vector.json')


if (not vector_requirements(vectorAn)):
    sys.exit()
if (not matrix_requirements(matrixMN)):
    sys.exit()

print('\n-----------------Statistics in a bitmap-------------------\n')
print('Values:                  ', vectorAn)



m = len(matrixMN)
n = len(matrixMN[0])

events = 0
s = ''
for element in vectorAn:
    event = search_element(element, matrixMN, m, n)
    events = events + event
    if events < ( m * n):
        if s != '':
            s = s + ' - ' + str(event)
        else:
            s = s + str(event)
    else:
        s = s + ' - ' + '0'
print('\nStatistics in a bitmap: ', s)
print('\n*********************End of Program************************\n')
