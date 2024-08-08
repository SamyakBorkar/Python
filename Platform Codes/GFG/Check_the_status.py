'''
Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.
Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return false.
'''



def check_status(a, b, flag):
    if (a <0) and (b<0) and (flag == True) :
       return True
    elif (a*b < 0) and (flag== False):
        return True
    else:
        return False
    
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        a = int(input())
        b = int(input())
        flag = input()
        
        if(flag == "True"):
            flag = True
        else:
            flag = False
        
        if(check_status(a, b, flag) is True):
            print ("True")
        else:
            print ("False")
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
