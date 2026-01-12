# Conditional Statements
from pyscript import display, document

def checker_converter(e):
    check = int(document.getElementById('temp').value)

    convert = (check-32) * 5/9
    
    if convert >= 37.8: 
        display(f'You have an abnormal temperature, get well soon!', target='output')
    else:
        display(f'You have a normal temperature, have a good day!', target='output')
    