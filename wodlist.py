#!/usr/bin/python

import itertools
from tqdm import tqdm
import base64
import time
import sys


# NOTE = Don't Touch This part Of the Code
info = open("crendital64.da",'r')
sample_string = base64.b64decode(info.read())
sys.stdout.write(sample_string.decode("ascii"))

print("")
com_chr = input("[+] Please Enter Here All Word For Combination: >> ")
print("")
Min_length = int(input("[+] Please Enter Minimun length of words: >>"))
print("")
Max_length = int(input("[+] Please Enter Maximum length of Words: >>"))
print(" ")
File_Name = input("[+] Please Enter The File name (To Save All The Words): >>")

Max_length = int(Max_length) + 1


leng_char = len(com_chr)
temp_list = []
for i in range(Min_length,Max_length):
    ans = leng_char**i
    temp_list.append(ans)
total_lines = sum(temp_list)
print(f"[+] Numbers of Total Lines: {total_lines}")
input("[+] Are you Ready?[Press Enter]")
print("")
print("\n\n=============Please Wait=================")
time_started = time.asctime()
start = time.time()

file_open = open(File_Name+".txt",'a')
for i in tqdm(range(Min_length,Max_length), desc="Genrating..."):
    file_open.flush()
    for j in itertools.product(com_chr,repeat=i):
        file_open.write("".join(j)+'\n')
file_open.flush()
file_open.close()
sys.stdout.write("\rDone Successfully")
print("")
print("\n\n===============================Process report===========================")
print(f"[+] Process Started                      :{time_started}")
end = time.time()
print(f"[+] Process completed                    :{time.asctime()}")
total_time= end - start
print(f"[+] Total Time Consumed                  :{'{:.2f}'.format(total_time)} second")
rate = total_lines/total_time
print(f"[+] Rate of Words Generating Per Seconds :{'{:.2f}'.format(rate)}")
print(" ")
print("""
*************************************************************************************
*                              WordList Successfully Genrated                       *
*************************************************************************************  
""")
print(" ")
input("[+]Press Enter To Exit")