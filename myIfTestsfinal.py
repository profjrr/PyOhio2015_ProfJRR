
# coding: utf-8

# # Making the "Best Decisions" in Python from the Very Beginning
# 
# # By Professor Reed -- PyOhio 2015 Conference -- 02-AUG-2015
# 
# # Begin with "Simple IF Tests"

# # myIfTestsfinal -- Modified 30-JUL-2015 -- all!

# In[41]:

# # Simple IF Tests - Part 1

# Making the "Best Decisions" in Python From the Very Beginning by ProfJRR (02-AUG-2015)
## Demo 1 - Simple IF Tests
##
# # Copy 9 - myfirstIFtests

### Begin Ifs in Python:
##
### Python ifs presented by Professor Reed
### last updated (11-DEC-2014)
### for Python 3.4+
### Lighting Talks -- Python User Group -- Feb. 2015 Meeting
##
## ID: lightIFdemos.py -- demo
## Included for further exploration of "data types" and if testing!
##
## Modified: 23-JUL-2015
## Demo -- Simple If Tests!
##
##import string

def simpleIf1(x):
    print("Trial01 -- Simple If test:")
    if x < 0:
        print("==> simple if test ran:", x)
    print("end of Trial01: ")
    print()
    return

def simpleIf2(x):
    print("Trial02 -- Simple If test: ")
    if x > 0:
        print("==> simple if test ran:", x)
    print("end of Trial02: ")
    print()
    return
    
def simpleIf3(x):
    print("Trial03 -- Simple If test: ")
    if x == 0:
        print("==> 3rd simple if test ran:", x)
    print("end of Trial03: ")
    print()
    return
       
##        
##       
### --- Professor Reed's test driver area --- ###
##        

def testMyIfs():
##    
    print ("*** Demonstration 1 - Simple IF Tests ***")
    x = 0    ## demo 1 
##    x = -1   ## demo 2
  
##   x = 1    ## demo 3
##    print()
##    print("x is: ", x)
##        
    print()
    print("Initial value of x is: ", x)
    print()
    ##
    simpleIf1(x)
    simpleIf2(x)
    simpleIf3(x)
    return

##    

### note: the test driver area above is a replacement for main()
##    
### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()
##
testMyIfs()
### end of demonstration 1 -- simple if tests ###


# In[42]:

### Demonstration 2 -- simple if tests begins ###
def simpleIf1(x):
    print("Trial01 -- Simple If test: ")
    if x < 0:
        print("==> simple if test ran:", x)
    print("end of Trial01: ")
    print()
    return

def simpleIf2(x):
    print("Trial02 -- Simple If test: ")
    if x > 0:
        print("==> simple if test ran:", x)
    print("end of Trial02: ")
    print()
    return
    
def simpleIf3(x):
    print("Trial03 -- Simple If test: ")
    if x == 0:
        print("==> simple if test ran:", x)
    print("end of Trial03: ")
    print()
    return
       
##        
##       
### --- Professor Reed's test driver area --- ###
##        

def testMyIfs():
##    
    print ("*** Demonstration 2 - Simple IF Tests ***")
##    x = 0    ## demo 1 

    x = -1   ## demo 2
    
##   x = 1    ## demo 3
##    print()
##    print("x is: ", x)
##        
    print()
    print("Initial value of x is: ", x)
    print()
    ##
    simpleIf1(x)
    simpleIf2(x)
    simpleIf3(x)
    return

##    

### note: the test driver area above is a replacement for main()
##    
### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()
##
testMyIfs()
### end of Demonstration 2 -- simple if tests ###


# In[43]:

### Begin Demonstration 3 -- simple if tests ###
## Modified: 23-JUL-2015
## Demo -- Simple If Tests!
##
##import string

def simpleIf1(x):
    print("Trial01 -- Simple If test: ")
    if x < 0:
        print("==> simple if test ran:", x)
    print("end of Trial01: ")
    print()
    return

def simpleIf2(x):
    print("Trial02 -- Simple If test: ")
    if x > 0:
        print("==> simple if test ran:", x)
    print("end of Trial02: ")
    print()
    return
    
def simpleIf3(x):
    print("Trial03 -- Simple If test: ")
    if x == 0:
        print("==> simple if test ran:", x)
    print("end of Trial03: ")
    print()
    return
       
##        
##       
### --- Professor Reed's test driver area --- ###
##        

def testMyIfs():
##    
    print ("*** Demonstration 3 - Simple IF Tests ***")
##    x = 0    ## demo 1 

##    x = -1   ## demo 2
    
    x = 1    ## demo 3
##    print()
##    print("x is: ", x)
##        
    print()
    print("Initial value of x is: ", x)
    print()
    ##
    simpleIf1(x)
    simpleIf2(x)
    simpleIf3(x)
    return

##    

### note: the test driver area above is a replacement for main()
##    
### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()
##
testMyIfs()


# # Results of Simple IF Tests above!


# In[44]:

# # Begin elseIF Tests


# # Begin elseIF Tests
##
## Modified: 23-JUL-2015
## Demo -- Simple If Tests!
##
##import string

def ifWithElse1(x):
    print("Trial 01: ")
    if (x < 0):
        print("with else test ran(x < 0):", x)
    else:
        print("else guesses x is either zero or something? x is==>", x)
    print("end of Trial 01: ")
    print()
    return

def ifWithElse2(x):
    print("Trial 02: ")
    if (x > 0):
        print("with else test ran(x > 0):", x)
    else:
           print("else guesses x is either zero or something? x is==>", x)
    print("end of Trial 02: ")
    print()
    return
    
def ifWithElse3(x):
    print("Trial 03: ")
    if (x == 0):
        print("with else test ran for zero value:", x)
    else:
           print("else guesses x is either zero or something? x is==>", x)
    print("end of Trial 03: ")
    print()
    return
##        
##       
### --- Professor Reed's test driver area --- ###
##        

def testMyIfs():
##
    print ("******************************************")
    print ("*** Demonstration 1 - ifWithelse Tests ***")
    print ("******************************************")
    x = 0    ## demo 1 

##    x = -1   ## demo 2
    
## x = 1    ## demo 3
##    print()
##    print("x is: ", x)
##        
    print()
    print("Initial value of x is: ", x)
    print()
    ##
    ifWithElse1(x)
    ifWithElse2(x)
    ifWithElse3(x)
    return

### note: the test driver area above is a replacement for main()
##    
### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()
##
testMyIfs()    


# In[45]:

##
## Modified: 23-JUL-2015
## Demonstration 2 -- ifWithElse Tests!
##
##import string

def ifWithElse1(x):
    print("Trial 01: ")
    if (x < 0):
        print("with else test ran(x < 0):", x)
    else:
        print("else guesses x is either zero or something? x is==>", x)
    print("end of Trial 01: ")
    print()
    return

def ifWithElse2(x):
    print("Trial 02: ")
    if (x > 0):
        print("with else test ran(x > 0):", x)
    else:
        print("else guesses x is either zero or something? x is==>", x)
    print("end of Trial 02: ")
    print()
    return
    
def ifWithElse3(x):
    print("Trial 03: ")
    if (x == 0):
        print("with else test ran for zero value:", x)
    else:
        print("else guesses x is either zero or something? x is==>", x)
    print("end of Trial 03: ")
    print()
    return
##        
##       
### --- Professor Reed's test driver area --- ###
##        
def testMyIfs():
##
    print ("******************************************")
    print ("*** Demonstration 2 - ifWithelse Tests ***")
    print ("******************************************")
##    x = 0    ## demo 1 

    x = -1   ## demo 2
    
## x = 1    ## demo 3
##    print()
##    print("x is: ", x)
##        
    print()
    print("Initial value of x is: ", x)
    print()
    ##
    ifWithElse1(x)
    ifWithElse2(x)
    ifWithElse3(x)
    return

### note: the test driver area above is a replacement for main()
##    
### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()
##
testMyIfs()    


# In[46]:

# In[ ]:

##
## Modified: 23-JUL-2015
## Demonstration 2 -- ifWithElse Tests!
##
##import string

def ifWithElse1(x):
    print("Trial 01: ")
    if (x < 0):
        print("with else test ran(x < 0):", x)
    else:
        print("else guesses x is either zero or something? x is==>", x)
    print("end of Trial 01: ")
    print()
    return

def ifWithElse2(x):
    print("Trial 02: ")
    if (x > 0):
        print("with else test ran(x > 0):", x)
    else:
        print("else guesses x is either zero or something? x is==>", x)
    print("end of Trial 02: ")
    print()
    return
    
def ifWithElse3(x):
    print("Trial 03: ")
    if (x == 0):
        print("with else test ran for zero value:", x)
    else:
        print("else guesses x is either zero or something? x is==>", x)
    print("end of Trial 03: ")
    print()
    return
##        
##       
### --- Professor Reed's test driver area --- ###
##        

def testMyIfs():
##
    print ("******************************************")
    print ("*** Demonstration 3 - ifWithelse Tests ***")
    print ("******************************************")
##    x = 0    ## demo 1 

##   x = -1   ## demo 2
    
    x = 1    ## demo 3
##    print()
##    print("x is: ", x)
##        
    print()
    print("Initial value of x is: ", x)
    print()
    ##
    ifWithElse1(x)
    ifWithElse2(x)
    ifWithElse3(x)
    return

### note: the test driver area above is a replacement for main()
##    
### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()
##
testMyIfs()


# In[47]:

# In[ ]:

def elseElseIf(x):
    print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print ("$$$ Special Demonstration  - elseElseIfTests $$$")
    print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
##
    print()
    print("Test Special Trial01: ")
    if x == 0:
        print()
        print("elseElseIf--initial if decision--> x equals zero: --> ", x)
        print()
    elif x == -1.0:
        print("elseElseif--first elif decision--> x is a neg: ", x)
        print()
    elif x == +1.0:
        print("elseElseif--second elif decision--> x is a plus: ", x)
        print() 
    else:
        print("elseElseif--final else or otherwise--> x is an unexpected value of: ", x)
        print()
        
    print("### end of Test Special Trial01 ###")
    print()
    return

def testMyIfs():
##
##    
## Testing new ifs ##
## x = -1.0 ## neg 1 -- test1
##    x = 0.0 ## value of zero! -- test2 ???
## x = -1.0 ## value of neg one -- test3
## x = +1.0 ## value of pos one -- test4
## x = +0.9 ## unexpected fractional value postive
    x = -0.9 ## unexpected fractional value negative 
## x = 9.9 ## value is high unexpected positive value???
   
    print()
    print("the supplied value of x for Special Demonstration is: ", x)
    print()
    elseElseIf(x)
    print()
    return

### note: the test driver area above is a replacement for main()
##    
### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()
testMyIfs()
    


# # 
# # Begin Participant's Experiment Section!!!
# 
# # 

# In[48]:

#############################################
### Experiments Follow:

def simpleIf(x):
    print("Experiment 01: ")
    if x < 0:
        print("simple if test ran:", x)
    print("end of Experiment 01: ")
    print()
    return

def ifWithElse(x):
    print("Experiment 02: ")
    if x < 0:
        print("with else test ran:", x)
    else:
        print("else x determines x is greater than a negative value")
    print("end of Experiment 02: ")
    print()
    return
    
def elseIf(x):
    print("Experiment 03: ")
    if x < 0:
        print("with else elseif:", x)
    elif x == 0:
        print("elseif x is equal to zero")
    else:
        print("elseif final else x is greater than a negative value")
    print("end of Experiment 03: ")
    print()
    return

def simpleifalpha(x):
    print("Experiment 04: ")
    if str.isalpha(x):
        print("simple if alpha test ran:", x)    
    print("end of Experiment 04: ")
    print()
    return
    
def simpleifnumeric(x):
    print("Experiment 05: ")
    if str.isnumeric(x):
        print("simple if numeric test ran: ", x)
    print("end of Experiment 05: ")
    print()
    return
       
def lowercasecheck(x):
    print("Experiment 06: ")
    if str.islower(x):
        print("if lowercase found: ", x)
    else:
        print("x is not lowercase: ", x)
    print("end of Experiment 06: ")
    print()
    return
    
def caseChkelif(x):
    print("Experiment 07: ")
    if str.islower(x):
        print("if case chk found lowercase: ", x)
    elif str.isupper(x):
        print("x is UPPERCASE by case chk: ", x)
    else:
        print("x is something other: ", x)
    print("end of Experiment 07: ")
    print()
    return
##        
##       
### --- Professor Reed's test driver area --- ###
##        
def elseElseIf(x):
    print("Experiment 03b: ")
    if x > 9.9:
        print("with else elseif:", x)
    elif x == -9.9:
        print("elseElseif x is a neg", x)
    elif x == +9.9:
         print("elseElseif x is a plus", x)
    else:
        print("elseif final else x is greater than a negative value")
    print("end of Experiment 03b: ")
    print()
    return

def testMyIfs():
##    
### Part I ###
    ### comment out the current demo ###
    ### un-comment the next demo ###
###    
    x = 'c' ## x is assigned lower case 'c' value -- demo 1
##    x = 'C' ## x is assigned upper case 'C' value -- demo 2
##    x = '22' ## x is assigned a value of 22 -- demo 3
##    
## end of demos from Feb. 23rd meeting 2015    
##    
### Part II ### -- future demos
##    x =  22 ## x is assigned a numeric value of 22 -- demo 4
##    x = -22 ## neg x is assigned value of -22 -- demo 5
##    
##    x = -1   ## demo 6
##    x = 0    ## demo 7 
##    x = 1    ## demo 8
##    print()
##    print("x is: ", x)
##        
    print()
    print("Initial value of x is: ", x)
    print()
    ##
##    simpleIf(x)
##    ifWithElse(x)
    simpleifalpha(x)
    simpleifnumeric(x)
    lowercasecheck(x)
    caseChkelif(x)
    return
##    

### note: the test driver area above is a replacement for main()
##    
### Professor Reed uses test cases instead of main()!
##if __name__ == '__main__':
##    main()
testMyIfs()

### end of experimental Python Laboratory ###
    


# # End of Experiment Area:

# In[ ]:


# In[ ]:



