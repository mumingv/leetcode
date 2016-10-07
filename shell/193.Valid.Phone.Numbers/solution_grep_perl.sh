#!/bin/bash
# 过滤出有效的电话号码

grep -P '^(\d{3}-|\([0-9]{3}\) )\d{3}-\d{4}$' file.txt
