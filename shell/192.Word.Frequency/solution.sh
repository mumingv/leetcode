#!/bin/bash
# 单词数量统计

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -nr | awk '{ print $2,$1 }'
