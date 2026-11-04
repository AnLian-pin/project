import my_utils.file_util
from my_utils import str_util

print(my_utils.file_util.str_reverse("伤心狗狗今天继续学习"))
print(my_utils.file_util.substr("伤心狗狗今天继续学习",0,4))
str_util.print_file_info("text.txt")
str_util.append_to_file("abc.txt","\n继续加油")