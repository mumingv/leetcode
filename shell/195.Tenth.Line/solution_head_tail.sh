#!/bin/bash
# 打印文件的第10行

# 获取文件的行数
lineNum=`cat file.txt | wc -l`

# 打印文件的第10行(不够10行则不打印)
if [ $lineNum -ge 10 ]; then
    head -10 file.txt | tail -1  
fi
