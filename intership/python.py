################################## swapping
# swap with 3rd varibale

a = input("enter the number")
b = input("enter the another number")
temp=a
a=b
b=temp
print(a,b)

######################## without 3rd variable
a=3
b=8
print(a,b,"original")
a,b=b,a
print(a,b,"swapped")


############################################################ palindrome
num=int(input("Enter a number"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(rev==temp):
    print("Palindrome")
else:
    print("Not a palindrome")


################################################### prime or not
def prime(num):
    if num<=1:
        print(num,"is not a prime number")
    if num>=1:
        for i in range(3,num//2+1):
            if num%i==0:
                print(num,"is not a prime")
                break
        else:
            print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
num=int(input("enter a number"))
print(prime(num))


###########################################################5*5 rows colums pattern
for i in range(5):
    for j in range(5):
        print("*",end="  ")
    print()



################################### for printing numbers in reverse triangle
for i in range(5):
    for j in range(5):
        if i==j:
            print("*",end=" ")
            # i=i+1
    print()

# ###########################for printing in X pattern
i=0
j=4
for row in range(5):
    for col in range(5):
        if row==i and col==j:
            print("*", end=" ")
            i=i+1
            j=j-1
        elif i==j:
            print("*",end=" ")
        else:
            print(" ")

    print()


################################# string examplesssssssss
a="thala,for,a,reason"
print(a.replace("thala","basava"))
print("thala"  not in a)
print(a.split(","))
a="my name is tejas"
print(slice(a[:-1]))

###################### highlighting the  character
txt="my name is \" tejas \" gowda"
print( txt)

#########################insert opertaion
a=["bas","manja","buddha"]
a.insert(1,"ravi")
print(a)

# ###################### extend opearation
a=["bas","manja","buddha","apple"]
b=["ninganna","juggad"]
a.extend(b)
print(a)
for i in a:
    print(i,end="\n")
a.sort(reverse=False)
print(a)

########################################## printing reverse of numbers pattern
for x in range(5,0,-1):
    for y in range(x,5):
        print(" ",end=" ")
    for z in range(x,0,-1):
        print(z+" ")
    print()

############################################## given sorted array count the numbers
#
arr=[1,2,2,4,5]
x=int(input("enter the no. to count in array"))
count=0
for i in range(len(arr)):
    if arr[i]==x:
        count=count+1
print("no. of occurences: ",count)

###########################################addition of 2 no.s without add symbol and arithmatic
a=int(input("enter the  value of a:"))
b=int(input("enter the  value of b:"))
sum=a-(-(b))
print("sum:",sum)

######################################### write prgm to find modulus without using modulus
a=int(input("enter the  value of a:"))
b=int(input("enter the  value of b:"))
q=a//b
# if part may not ne needed in many cases
if q<0:
    q+=1
m=a-b*q
print(m)

##################################### divide without using the divide symbol and modulus
a=float(input("enter the  value of a:"))
b=float(input("enter the  value of b:"))
count=0
while b!=0:
    if b<a:
        a=a-b
        count=count+1
    else:
        break
print(count)

#################################### finding the biggest prime factorial
import math
def maxPrimeFactor(n):
    max_Prime = 1
    while n % 2 == 0:
        max_Prime = 2
        n /= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_Prime = i
            n = n / i
    if n > 2:
        max_Prime = n
    return int(max_Prime)

n = 25
print(maxPrimeFactor(n))

############################### finding the missing values
n=7
arr=[7,5,3,2,1]
for i in range(1,n+1):
    if i not in arr:
        print("missing number",i)
#
#
################################## another method for finding missing values(by taking input from user)
from array import array

n = int(input('Enter the number: '))

if not (1 <= n <= 106):
    print("Invalid input. Please enter a number within the range [1, 10^6].")
else:
    arr = array('i', [])
    print("Enter the array elements separated by spaces:")
    arr.extend(map(int, input().split()))

    for i in range(1, n + 1):
        if i not in arr:
            print("Missing number:", i)

# ####################################### finding the second largest element
def second_largest(arr):
    arr=list(set(arr))
    arr.sort()
    return arr[-2]

array = [14, 67, 8, 89]
print(list(array))
print("Second largest number is ",second_largest(array))


# ######################################## finding the maximum difference
def maximum_diff(arr):
    arr=list(set(arr))
    arr.sort()
    return (arr[-1]-arr[0])

array=[3,4,1,9,56,7,9,12]
print(list(array))
print("largest difference is ",maximum_diff(array))
