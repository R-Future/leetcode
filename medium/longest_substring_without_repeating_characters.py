def length_of_longest_substring(s: str) -> int:
    length_max = 0
    longest_substring = ''
    for char in s:
        idx = longest_substring.find(char)
        if idx == -1:
            longest_substring += char
        else:
            current_length = len(longest_substring)
            if current_length > length_max:
                length_max = current_length
            longest_substring = longest_substring[idx + 1:]
            longest_substring += char
    # compare with the last substring
    last_length = len(longest_substring)
    if last_length > length_max:
        length_max = last_length
    return length_max


if __name__ == '__main__':
    s = "pwwkew"
    l = length_of_longest_substring(s)
    print(l)
