import sys

dict={}
names=[]
user1=sys.argv[1].split(",")[0]
user2=sys.argv[1].split(",")[1]
with open("student.txt","r") as f:
    for i in f.readlines():
        name=i.split(":")[0]
        key=i.split(":")[1]
        dict[name]=key.strip("\n")
        names.append(name)
    try:
        print("Name=", user1, ":", dict[user1],"Name=",user2,":",dict[user2])
    except KeyError:
        if user1 in names and user2 not in names:
            print("Name=", user1, ":", dict[user1],user2,"not found")
        elif user2 in names and user1 not in names:
            print("Name=", user2, ":", dict[user1],user1,"not found")
        elif user2 not in names and user1 not in names:
            print(user1,"and",user2,"not found")





