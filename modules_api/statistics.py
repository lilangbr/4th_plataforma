#This program returns the count of times that values in a vector, in order, 
#appear in a given bitmap image.
#The values in the vector are between 0 and 15.
#The bitmap image and vector are JSON files in the ./src folder.
#
#Author: Eliane Bresser Lang
#Date: dec/06/2020

import json
import sys
from modules.get_object import get_json
from modules.search import search_element
from modules.requirements import vector_requirements
from modules.requirements import matrix_requirements

matrixMN = get_json('./src/image.json')


def statistics(vectorAn):
    
    if (not matrix_requirements(matrixMN)):
        r = {
                'Error': 'Error Matrix - Matrix not satisfied the requirements. (See file image.json in folder src! It must be a not null matrix)'
        }
        return r

    if (not vector_requirements(vectorAn)):
        r = {
                'Error': 'Error Vector - Vector not satisfied the requirements. See http://127.0.0.1:5000/instructions'
        }
        return r



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
    r = {
            'numbers' : str(vectorAn),
            'occurrence': s
    }
    return r
