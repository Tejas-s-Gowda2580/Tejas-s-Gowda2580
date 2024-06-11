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