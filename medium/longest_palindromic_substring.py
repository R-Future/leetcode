import re


def longest_palindrome(s: str) -> str:
    longest_palindromic_substring = ''
    max_len = 0
    for i, c in enumerate(s):
        # find next c in sub string
        for _iter in re.finditer(c, s[i:]):
            idx = _iter.start()
            sub_str = s[i:idx + 1 + i]
            if sub_str == sub_str[::-1]:
                len_sub_str = len(sub_str)
                if len_sub_str > max_len:
                    longest_palindromic_substring = sub_str
                    max_len = len_sub_str
    return longest_palindromic_substring


if __name__ == '__main__':
    s = 'babad'
    # bab
    print(longest_palindrome(s))
    s = 'cbbd'
    # bb
    print(longest_palindrome(s))
    s = 'a'
    # a
    print(longest_palindrome(s))
