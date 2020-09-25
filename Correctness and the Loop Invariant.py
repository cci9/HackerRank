
def insertion_sort(ar):
    #for i in range(1, len(l)):
        #j = i-1
        #key = l[i]
        #while (j > 0) and (l[j] > key):
           #l[j+1] = l[j]
           #j -= 1
        #l[j+1] = key
    for i in range(1, len(ar)):
        for j in range(i):
            if ar[i] < ar[j]:
                a = ar[i]
                ar.pop(i)
                ar.insert(j, a)

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))

