
##! /usr/local/bin/python3
r"""Test cases
>>> run_answer() # doctest: +NORMALIZE_WHITESPACE
1971-07-08,08,8,jue,jueves
1974-05-23,23,23,jue,jueves
1973-04-22,22,22,dom,domingo
1975-01-29,29,29,mie,miercoles
1974-07-03,03,3,mie,miercoles
1974-10-18,18,18,vie,viernes
1970-10-05,05,5,lun,lunes
1969-02-24,24,24,lun,lunes
1974-10-17,17,17,jue,jueves
1975-02-28,28,28,vie,viernes
1969-12-07,07,7,dom,domingo
1973-12-24,24,24,lun,lunes
1970-08-27,27,27,jue,jueves
1972-12-12,12,12,mar,martes
1970-07-01,01,1,mie,miercoles
1974-02-11,11,11,lun,lunes
1973-04-01,01,1,dom,domingo
1973-04-29,29,29,dom,domingo
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
