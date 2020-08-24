stack_num = int(input(""))
final_list = []
stack_list=[]
max_num = 0
prev_num = None
test_TF = True
for i in range(stack_num):
    num = int(input(""))
    if prev_num ==None:
        for i in range(num):
            stack_list.append(i+1)
            final_list.append("+")
            if max_num<i+1:
                max_num = i+1
        prev_num=num
        stack_list.pop()
        final_list.append("-")
    elif prev_num>num:
        if stack_list[len(stack_list)-1] != num :
            test_TF = False
            break
        else:
            stack_list.pop()
            final_list.append("-")
            prev_num=num
    elif prev_num<num:
        for i in range(max_num, num):
            stack_list.append(i+1)
            final_list.append("+")
            if max_num<i+1:
                max_num = i+1
        prev_num=num
        stack_list.pop()
        final_list.append("-")
if test_TF == False:
    print("NO")
else:
    for i in final_list:
        print(i)
