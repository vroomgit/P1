#
def karatsuba_product(n1,n2):
    """
    

    Parameters
    ----------
    n1 : int
        FIRST NUMBER TO BE MULTIPLIED.
    n2 : int
        SECOND NUMBER TO BE MULTIPLIED.

    Returns
    -------
    INT
        PRODUCT OF TWO NUMBERS n1 and n2.

    """
    
    sn1 = str(n1)
    sn2 = str(n2)
    
    
    if (len(sn1)<4 and len(sn2)<4):
        return n1*n2
    
    
    mid = max(len(sn1),len(sn2)) // 2

    '''
    Slicing two numbers into a,b,c,d.
    '''
    
    a = n1 // pow(10,mid)
    b = n1 % pow(10,mid) 
    c = n2 // pow(10,mid)
    d = n2 % pow(10,mid)

    
    '''
    Calculating step one which is a*c
    '''
    step1 = karatsuba_product(a,c)

    
    '''
    Calculating step two which is b*d
    '''
    step2 = karatsuba_product(b,d)

    
    '''
    Calculating step three which is ((a+b)*(c+d))
    '''
    step3 = karatsuba_product((a+b),(c+d))

    
    '''
    Calculating step four which is Step 3 - Step 2 - Step 1
    '''
    step4 = step3 - step2 - step1

    
    '''
    Calculating step five, the result of Karatsuba Multiplication
     which is: step2 + (10^n * Step 1) + (10^n/2 * Step 4) 
    '''
    step5 = step2 + ((pow(10,mid*2))*step1) + ((pow(10,mid))*step4) 
    # print("Step1",step1,"\n")
    # print("Step2",step2,"\n")
    # print("Step3",step3,"\n")
    # print("Step4",step4,"\n")
    # #print("Step5",step5,"\n")
    
    return step5



# n1=4567894574531357963242652159753455452179345214621415975345545217934521462144567894574531357963242652
# n2=1597534554521793452146214456789457453135796324265245678945745313579632426521597534554521793452146214

# import time
# t = time.time()
# conv_prod = n1*n2
# print("\nConventional product of the two numbers =",conv_prod, "\nTime taken for conventional product",time.time()-t)

# '''
# Calculates and prints the difference between the results of
# Karatsuba multiplication and conventional multiplication. If
# this error is zero, the Karatsuba product is calculated correctly
# '''
# t = time.time()
# k = karatsuba_product(n1,n2)
# print("K",k,"\nTime taken for Karatsuba product",time.time()-t)
# print("Error = ",k-conv_prod)
# print(len(str(n1)))

