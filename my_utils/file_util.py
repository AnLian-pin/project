def str_reverse(s):
    temp=""
    for i in range(1,len(s)+1):
        temp+=s[-i]
    return temp

def substr(s,x,y):
    temp=""
    for i in range(x,y):
        temp+=s[i]
    return temp

if __name__ == '__main__':
    print(str_reverse("hello"))
    print(substr("hello",1,3))