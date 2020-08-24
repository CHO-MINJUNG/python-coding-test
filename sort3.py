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

num_list = []
for i in range(int(input(""))):
    num = int(input(""))
    num_list.append(num)
num_list = QuickSort(num_list)
for i in num_list:
    print(i)