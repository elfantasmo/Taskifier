from pathlib import Path


File=("to-do.txt")
file1=Path("to-do.txt")
fin=False
if not file1.is_file():
    fi=open(File, "w+")
    fi.close()
    fio=open(File+"lol","w+")
    fio.close()

while fin==False:



    print("\n1=Check Active Tasks")
    print("2=Add a Task")
    print("3=Clear a Task")
    print("4=Stop To-Do manager")
    d= int(input())

    i = 1
    if(d==1):
        i = 1
        f = open(File,"r")
        print("")
        for linesd in f:
            if(i>1):
                print(str(i-1)+"-"+linesd)
            i = i + 1
        f.close()
    if(d==2):
        f = open(File,"a")
        print("\nWrite your task!")
        p=input()
        f.write("\n"+p)
        f.close()
        print("Done")
        print("")
    if(d==3):
        f = open(File, "r")
        for liness in f:
            if i>1:
                print(str(i-1) + "-" + liness)
            i = i + 1
        lines = f.readlines()
        f.close()
        print("\n Clear a Task")

        done=int(input())
        if done<=0:
            print("0 or less is invalid! Please try again")
            done = int(input())

        with open(File, "r") as infile:
            linesds = infile.readlines()

        with open(File+"lol", "w") as outfile:
            for pos, line in enumerate(linesds):
                if pos != done:
                    outfile.write(line)


            infile.close()
            outfile.close()
        l=open(File+"lol","r+")

        datas=l.read()
        s=open(File,"w")
        s.write(datas)

        s.close()
        l.close()
    if(d==4):
        fin=True
        print("\nHave a nice day")
