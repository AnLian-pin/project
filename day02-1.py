try:
    f=open("abc.txt","r",encoding="utf-8")
    print(f.read())
except Exception as e:
    f=open("abc.txt","w",encoding="utf-8")
    f.write("day02,异常的捕获与处理")
else:
    print("没有异常，正常执行")
finally:
    f.close()