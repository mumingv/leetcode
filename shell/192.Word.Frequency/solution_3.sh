#!/bin/bash
# 单词数量统计

declare -A words_array
file='words.txt'

# 使用关联数组保存单词统计计数
function word_count {
    # 统计
    while read line; do
        array=(${line})
        for word in ${array[*]}; do
            let words_array[${word}]++
        done
    done < ${file}
    # 输出
    for word in ${!words_array[*]}; do
        echo ${word} ${words_array[${word}]}
    done
}

word_count | sort -k 2 -nr
