'''
You are familiar with basics of input/output and many other useful things in Python. This module is all about conditional statements like if, elif, else; for, while, etc.

In Python, any conditional statement ends with ':' (proper indentation must be followed while working through loops).

There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.

Now, complete the function which returns true if you are in trouble, else return false
'''

def friends_in_trouble(j_angry, s_angry):
    if j_angry==True and s_angry==True :
        return True
    elif j_angry==False and s_angry==False:
        return True
    else:
        return False
    

#{ 
 # Driver Code Starts.

# Driver code    
def main():
    testcase = int(input())
    
    # loop for testcases
    while(testcase > 0):
        string = input().split()
        j_angry = string[0]
        s_angry = string[1]
        if(j_angry == 'True'):
            j_angry = True
        else:
            j_angry = False
        
        if(s_angry == 'True'):
            s_angry = True
        else:
            s_angry = False
            
        print(friends_in_trouble(j_angry, s_angry))
        
        testcase -= 1
    
if __name__ == '__main__':
    main()
# } Driver Code Ends