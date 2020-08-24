age_list = []
name_list = []
for i in range(int(input(""))):
    age, name = input("").split()
    index = 0
    if age_list == []:
        age_list.append(int(age))
        name_list.append(name)
        break
    elif len(age_list)<1000:
        for j in age_list:
            if int(age)<int(j) :
                break
            index+=1
        if age_list !=[]:
            age_list.insert(index,age)
            name_list.insert(index,name)
    else:
        
    
for i in range(len(age_list)):
    print(age_list[i],name_list[i])