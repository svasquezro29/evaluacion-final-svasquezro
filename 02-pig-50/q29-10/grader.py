
##! /usr/local/bin/python3
r"""Test cases
>>> run_answer() # doctest: +NORMALIZE_WHITESPACE
1971-07-08,jul,07,7
1974-05-23,may,05,5
1973-04-22,abr,04,4
1975-01-29,ene,01,1
1974-07-03,jul,07,7
1974-10-18,oct,10,10
1970-10-05,oct,10,10
1969-02-24,feb,02,2
1974-10-17,oct,10,10
1975-02-28,feb,02,2
1969-12-07,dic,12,12
1973-12-24,dic,12,12
1970-08-27,ago,08,8
1972-12-12,dic,12,12
1970-07-01,jul,07,7
1974-02-11,feb,02,2
1973-04-01,abr,04,4
1973-04-29,abr,04,4
<BLANKLINE>

"""
import doctest
import subprocess
import os

def run_answer():
    '''Codigo especifico para ejecutar la respuesta'''
    #----------------------------------------------------------------------------------------------
    # Ejecuta el código del estudiante
    #----------------------------------------------------------------------------------------------
    result = os.popen("pig -execute 'run question.pig'").read()
    result = os.popen("cat output/*").read()
    print(result)

#--------------------------------------------------------------------------------------------------
# Grader (generic)
#--------------------------------------------------------------------------------------------------
subprocess.run(['rm', '-f', '_SUCCESS']) # borra el flag de exito de la corrida
RESULT = doctest.testmod()               # ejecuta el doctest
FAIL, _ = RESULT                         # fail, total
if FAIL == 0:                            # grading
    open('_SUCCESS', 'a').close()        #
else:
    print('\n')
#--------------------------------------------------------------------------------------------------
