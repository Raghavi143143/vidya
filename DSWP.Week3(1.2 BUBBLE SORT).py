print("*"*20,"Bubble sorting","*"*20,)
import time
start=time.time()
def bubblesort(a):
    n=len(a)
    for i in range(n-2):
        for j in range(n-2-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
alist=[34,46,43,27,57,41,45,21,70]
print("Before sorting:",alist)
bubblesort(alist)
print("After sorting:",alist)
end=time.time()
print(f"Runtime of the program is:{end-start}")
print("")



print("*"*20,"Selection sorting","*"*20)
import time
start=time.time()
def selectionsort(a):
    n=len(a)
    for i in range(n-2):
        min=i
        for j in  range(i+1,n-1):
            if a[j]<a[min]:
                temp=a[j]
                a[j]=a[min]
                a[min]=temp
alist=[34,46,43,27,57,41,45,21,70]
print("Before sorting:",alist)
selectionsort(alist)
print("After sorting:",alist)
end=time.time()
print(f"Runtime of the program is:{end-start}")
print("")




print("*"*20,"Insertion sorting","*"*20)
import time
start=time.time()
def insertionsort(a):
    n=len(a)
    for i in range(1,n-1):
        k=a[i]
        j=i-1
        while j>+0 and a[j]>k:
            a[j+1]+a[j]
            j=j-1
            a[j+1]=k
alist=[34,46,43,27,57,41,45,21,70]
print("Before sorting:",alist)
insertionsort(alist)
print("After sorting:",alist)
end=time.time()
print(f"Runtime of the program is:{end-start}")
print("")


    









