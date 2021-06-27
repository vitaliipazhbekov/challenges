# list
# need to work out

ttt = int(input())
L = []
for i in range(ttt):
    args = input().split(" ")
    if args[0] == "append":
        ttt.append(int(args[1]))
    elif args[0] == "insert":
        ttt.insert(int(args[1]), int(args[2]))
    elif args[0] == "remove":
        ttt.remove(int(args[1]))
    elif args[0] == "pop":
        ttt.pop()
    elif args[0] == "sort":
        ttt.sort()
    elif args[0] == "reverse":
        ttt.reverse()
    elif args[0] == "print":
        print(ttt)

