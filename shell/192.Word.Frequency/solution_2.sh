#!/bin/bash
# 统计词频

filename=words.txt

egrep -o "\b[[:alpha:]]+\b" $filename | \
awk '{ count[$0]++ } END {
    for (ind in count) {
        printf("%s %d\n", ind, count[ind]);
    }
}' | sort -k 2 -nr
