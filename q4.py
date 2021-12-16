        
n = int(input("Enter an integer:"))

divisor = []


for i in range(1,n+1):
    if(n%i==0):
        divisor.append(i)

print('The divisors of {} : '.format(n) , divisor)
    
        

 






