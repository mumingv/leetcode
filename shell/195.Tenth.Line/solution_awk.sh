#!/bin/bash
# 打印文件的第10行

cat file.txt | awk 'NR==10 { print $0 }'
