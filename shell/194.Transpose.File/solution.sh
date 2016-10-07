#!/bin/bash
# 行列转置

# 获取列数
col_num=`head -n 1 file.txt | wc -w`
# 转置每一列
for i in `seq ${col_num}`; do
    echo `cut -d " " -f ${i} file.txt`
done
