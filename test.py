f=open("temp.txt","r",encoding="utf-8")
for line in f:
    line=line.strip()
    if line.split(",")[-1]=="正式":
        f2=open("text.txt","a",encoding="utf-8")
        f2.write(line)
        f2.write("\n")
        f2.close()
f.close()