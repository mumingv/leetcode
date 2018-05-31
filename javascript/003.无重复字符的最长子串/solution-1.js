/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let length = 0; // 最长子串长度
    let begin = end = 0;  // 子串起始下标
    let set = new Set();
    for (let i = 0; i < s.length; i++) {
        if (!set.has(s[i])) {
            set.add(s[i]);
            end = i;
            if (set.size > length) {
                length = set.size;
            }
        } else {
            while (begin < i) {
                if (s[begin] != s[i]) {
                    set.delete(s[begin]);
                    begin++;
                } else {
                    begin++;
                    break;
                }
            }
        }
    }
    return length; 
};

s = "pwwkew";
s = "abcabcbb";
s = "bbbbb";
l = lengthOfLongestSubstring(s);
console.log(l);
