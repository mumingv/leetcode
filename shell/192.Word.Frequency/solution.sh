#!/bin/bash
# 单词数量统计

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{ print $2,$1 }'
