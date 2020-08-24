scale1 = input("음계를 입력하시오: ")
scale_list = scale1.split()
scale_list = list(map(int, scale_list))
if int(scale_list[0])==1:
    for i in range(1,len(scale_list)):
        if scale_list[i-1]+1 == scale_list[i]:
            if i == len(scale_list)-1 :
                print("ascending")
            continue
        else:
            print("mixed")
            break
elif int(scale_list[0])==8:
    for i in range(1,len(scale_list)):
        if scale_list[i-1]-1 == scale_list[i]:
            if i == len(scale_list)-1 :
                print("descending")
            continue
        else:
            print("mixed")
            break
else:
    print("mixed")