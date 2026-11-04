try:
    f=open("abc.txt","r")
except Exception as e:
    f=open("abc.txt","w")
else:
    print("没有异常，正常执行")
finally:
    f.close()