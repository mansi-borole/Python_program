unit=int(input("Enter the units :"))

if unit<=50:

    rs=unit*0.50

    g=(rs*20)/100+rs

    print("The gross value is ",g)

elif unit<=150:

    rs= 0.75 * (unit-50)+25

    g=(rs*20)/100+rs

    print("The gross value is ",g)

elif unit<=250:

    rs=1.20*(unit-150)+75+25

    g=(rs*20)/100+rs

    print("The gross value is ",g)

else:

    rs=1.50 * (unit-250) +180 +75 + 25

    g=(rs*20)/100+rs

    print("The gross value is ",g)



'''a=int(input("Enter the units :"))

b=int(input("Enter the units :"))

c=int(input("Enter the units :"))

if a>b and a>c:

    if b>c:

        print(a,b,c)

    elif c>b:

        print(a,c,b)

elif b>c and b>a:

    if c>a:

        print(b,c,a)

    elif a>c:

        print(b,a,c)

else:

    print(c,a,b)'''

'''a=int(input("Enter the units :"))

b=int(input("Enter the units :"))

sum = 0

for c in range(a,b+1):

    sum=c+sum



print(sum)'''

'''for c in range(1 0,0,-1):

    print(c)'''

'''a=int(input("Enter the number :"))

b=int(input("Enter the number :"))

while (a<b+1):

    print(b)

    b=b-1'''

'''for i in range(1,11):

    if i==5:

        break

    print(i)'''

'''b=int(input("Enter the numbe for range : "))

sum = 0

for a in range(b+1):

    if a%2==0:

        sum = sum + a

print(sum)'''

a = int(input("Enter the numbe to print sum of even numbers : "))



