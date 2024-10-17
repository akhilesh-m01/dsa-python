m1 = [[1,2,3],[4,5,6],[7,8,9]]

m = len(m1)
n = len(m1[0])

print(m,n)

def printMatrix(m1,m,n):
    for i in range(0,m):
        for j in range(0,n):
            print(m1[i][j], end=" ")
        print()

# sum of elements in matrix
sum=0
for i in range(0,m):
    for j in range(0,n):
        sum+= m1[i][j]
print(sum)

# sum of elements of upper triangle
uSum = 0
lSum = 0
for i in range(0,m):
    for j in range(0,n):
        if(j>=i):
            uSum +=m1[i][j]
        if(i>=j):
            lSum +=m1[i][j]
print(uSum)
print(lSum)


# snake pattern
for i in range(0,m):
    if(i%2==0):
        for j in range(0,n):
            print(m1[i][j],end=" ")
    else:
        for j in range(n-1,-1,-1):
            print(m1[i][j],end=" ")
    print()


# transpose of a matrix
def transpose(m1,m,n):
    for i in range(0,m):
        for j in range(0,n):
            if(i!=j) and j>i:
                m1[i][j],m1[j][i] = m1[j][i],m1[i][j]
    printMatrix(m1,m,n)


def swapRows(m1,m,n):
    for i in range(0,m//2):
        for j in range(0,n):
            m1[i][j], m1[m-1-i][j] = m1[m-1-i][j], m1[i][j]
    printMatrix(m1,m,n)


a = [[1,2,3],[4,5,6],[7,8,9]]
transpose(a,m,n)
print("90 degrees")
swapRows(a,m,n)

def matrixMul(a,b,m,n):
    ans = []
    for i in range(0,m):
        temp = []
        for j in range(0,n):
            sum=0
            for k in range(0,n):
                sum+=a[i][k]*b[k][j]
            temp.append(sum)
        ans.append(temp)
    printMatrix(ans,m,n)

matrixMul(m1,a,m,n)







