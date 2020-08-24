def binarySerach(target, l, left, right):
    while left<=right:
        mid = (left+right)//2
        if l[mid]>target:
            right=mid-1
        elif l[mid]<target:
            left = mid+1
        elif l[mid] == target:
            return 1
    return 0

def QuickSort(l):
    if len(l)<=1:
        return l
    pivot = l[len(l)//2]
    front, mid, final = [], [], []
    for i in l:
        if i< pivot:
            front.append(i)
        elif i>pivot:
            final.append(i)
        else:
            mid.append(i)
    return QuickSort(front)+mid+QuickSort(final)
    

final_list = []
Nnum = input("")
Nlist = input("").split()
Nlist = list(map(int,Nlist))
Nlist = QuickSort(Nlist)
Mnum =input("") 
Mlist = input("").split()
Mlist = list(map(int,Mlist))
for i in Mlist:
    print(binarySerach(i, Nlist, 0, int(Nnum)-1))