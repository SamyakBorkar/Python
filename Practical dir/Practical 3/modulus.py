'''
THIS CODE IS MADE BY SAMYAK BORKAR 
THIS IS A CUSTOM MODULO FUNCTION CODE WHICH HANDELS CASESLIKE:
1.WHEN DENOMINATOR IS EQUL TO NUMERATOR
2.WHEN DENOMINATOR IS EQUAL TO ZERO AND NUMERATOR IS INTEGER
3.WHEN DENOMINATOR IS EQUAL TO ZERO AND NUMERATOR IS FLOAT
4.WHEN DENOMINATOR IS GREATOR THAN NUMERATOR
5.AND THEN LAST IS FOR HANDELING MODULO FOR ALL NUMBERS IN WHICH I HAVE IMPLEMENTED THE LOGIC OF :
QUOTIENTT * DENOMINATOR + REMAINDER = NUMERATOR 
'''

def moduloFunc(numerator, denominator):
    if numerator == denominator:
        return 0
    elif denominator == 0 and isinstance(numerator, int):
        return "ZeroDivisionError: integer modulo by zero"
    elif denominator == 0 and isinstance(numerator, float):
        return "ZeroDivisionError: float modulo"
    elif numerator < denominator:
        return numerator
    elif isinstance(numerator, int) and isinstance(denominator, int):
        quotient = numerator // denominator
        remainder = numerator - (denominator * quotient)
        return remainder
    elif not (isinstance(numerator, int) and isinstance(denominator, int)):
        quotient = numerator / denominator 
        remainder = numerator - (denominator * int(quotient))
        return remainder
    else:
        return "ERROR 404"

print(moduloFunc(7.4, 5.0))  #for float value
print(moduloFunc(7,5))       #for integer values 
print(moduloFunc(7,7))      #when numerator and denominator are same 
print(moduloFunc(3,7))      #when numerator is less than denominator  
print(moduloFunc(5,0))	    #when denominator==0 and numerator==any number

