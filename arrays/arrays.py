# # merge intervals
# a = [[1,3],[2,6],[8,10],[15,18]]
# print(a)
# i=0
# while i<len(a)-1:
#     if a[i][1]>=a[i+1][0]:
#         a[i][1] = a[i+1][1]
#         a.remove(a[i+1])
#     elif a[i][1]<a[i+1][0]:
#         i = i+1
# print(a)


# longest substring

s = "abcabcbb"
# maxi = 0
# for i in range(0,len(s)):
#     mp={}
#     s1=""
#     for j in range(i,len(s)):
#         s1+=s[j]
#         if s[j] in mp:
#             break
#         else:
#             mp[s[j]] = 1
#         maxi = max(maxi,j-i+1)
# print(maxi)
        

left=0
right=0
d={}
maxi=0
while right<len(s):
    if s[right] not in d:
        d[s[right]] = right
        maxi = max(maxi,right-left+1)
         
    else:
        left = d[s[right]]+1
        d[s[left]]-=1
        left+=1
        continue
    if d[s[right-1]]<=1:
        maxi = max(maxi,right-left+1)
print(maxi) 

    
    
