import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
totalswaps=0
for i in range(0,n):
    swaps=0
    for j in range (0,n-1):
        if a[j]>a[j+1]:
            swaps+=1
            a[j],a[j+1]=a[j+1],a[j]

    if swaps==0:
        break
    else:
        totalswaps+=swaps

print("Array is sorted in",totalswaps,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])
