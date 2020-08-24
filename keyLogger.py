num = int(input(""))
index = 0
key =[]
for i in range(num):
    keyS = input("")
    key.append(keyS)
for i in key:
    final_str = []
    for j in i:
        if j =="<" and index !=0:
            index -=1
        elif j ==">" and index != 0 and index != len(final_str):
            index +=1
        elif j == "-" and final_str != []:
            if index == len(final_str):
                index-=1
            final_str.pop()
        elif j!="<" and j !=">" and j != "-":
            final_str.insert(index,j)
            index+=1
    print(''.join(final_str))