def print_file_info(file_name):
    f=None
    try:
        f=open(file_name,"r",encoding="utf-8")
        print(f.read())
    except Exception as e:
        print(f"文件出现异常，原因是:{e}")
    finally:
        if f:
            f.close()

def append_to_file(file_name,date):
    f=open(file_name,"a",encoding="utf-8")
    f.write(date)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    print_file_info("../temp.txt")
    append_to_file("../abc.txt","当前日期:2026-11-4")