for num in range(int(input(""))):
    F = int(input(""))
    friend_list = []
    for i in range(F):
        twofriend = input("").split()
        friend_list.append(twofriend)
        friend_num = 2
        for j in range(i):
            if twofriend[0] in friend_list[j] or twofriend[1] in friend_list[j]:
                friend_num+=2
                diff = set(twofriend)-set(friend_list[0])
                friend_num-=len(diff)
        print(friend_num)