# sum of all numbers in a list
l1= [1,2,3,4,50]

def mySum(l1):
    sum=0

    for i in l1:
        sum+=i
    return sum

# print(mySum(l1))

def myProd(l1):
    mul=1

    for i in l1:
        mul*=i
    return mul

# print(myProd(l1))

def largest(l1):
    max=l1[0]
    for i in l1:
        if i>max:
            max=i
    return max

# print(largest(l1))

def largest02(l1):
    return max(l1)

# print(largest02(l1))

def smallest(l1):
    return min(l1)

# print(smallest(l1))

s1 = ['abc', 'xyz', 'aba', '1221']

def custom(s1):
    count = 0
    for i in s1:
        if len(i)>=2 and i[0]==i[-1]:
            count+=1
    return count

# print(custom(s1))

l2 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last(n):
    return n[-1]

def customSort(l2):
    l3 = sorted(l2,key=last,reverse=True)
    return l3

# print(customSort(l2))

# ####################

# remove duplicates from a list
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

def removeDuplicates(a):
    return set(a)

# print(removeDuplicates(a))

# ################################

# Find the list of words that are longer than n from a given list of words

s3 = "The quick brown fox jumps over the lazy dog"

def strOp(n,s3):
    l3= []
    l2 = s3.split(" ")
    for i in l2:
        if len(i)>n:
            l3.append(i)
    return l3

# print(strOp(3,s3))

# ###################################

def commonData(l1,l2):
    l3=[]
    for i in l1:
        for j in l2:
            if i==j:
                l3.append(i)
    return l3
                

# print(commonData([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))

# #########################################

# program to print a specified list after removing the 0th, 4th and 5th elements.

s7 =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

def removeItems(s1):
    color = [x for i,x in enumerate(s1) if i not in (0,4,5)]
    return color

# print(removeItems(s7))


# ##########################

# print not even numbers

def notEven(l1):
    x = [j for j in l1 if (j%2)!=0]
    return x

# print(notEven([7, 8, 120, 25, 44, 20, 27]))

# ########################

# join strings

s = ['a', 'b', 'c', 'd']

print("".join(s))


# #######################################33





