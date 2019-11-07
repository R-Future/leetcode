"""
n_rows = 3
shift = 4
the zigzag of indices,
0   4   8
1 3 5 7 9
2   6   10
======================
n_rows = 4
shift = 6
the zigzag of indices,
0     6       12
1   5 7    11 13
2 4   8 10    14
3     9       15
======================
n_rows = 5
shift = 8
the zigzag of indices,
0       8           16
1     7 9        15 17
2   6   10    14    18
3 5     11 13       19
4       12          20
...
======================
shift = 2 * (n_rows - 1)
the zigzag of indices,
0                                              0+shift                                                  0+2*shift
1                                  1+shift-1*2 1+shift                                    1+2*shift-1*2 1+2*shift
2                      2+shift-2*2             2+shift                      2+2*shift-2*2               2+2*shift
3          3+shift-3*2                         3+shift        3+2*shift-3*2                             3+2*shift
.
.       ...
.
n_rows-1                                       n_rows-1+shift                                           n_rows-1+2*shift
======================
Special cases:
1, n_rows = 1
2, s = 'A', n_rows > 1
"""


def convert(s: str, n_rows: int) -> str:
    if n_rows == 1:
        return s
    shift = 2 * (n_rows - 1)
    len_s = len(s)
    s_re = ''
    is_visited = [False] * len_s
    for i_row in range(n_rows):
        idx = i_row
        while idx < len_s:
            idx_pre_char = idx - i_row * 2
            if idx_pre_char > -1 and not is_visited[idx_pre_char]:
                s_re += s[idx_pre_char]
                is_visited[idx_pre_char] = True
            if not is_visited[idx]:
                s_re += s[idx]
                is_visited[idx] = True
            idx += shift
        # maybe the index of last one in this row is not idx, is the previous one.
        idx_pre_char = idx - i_row * 2
        if -1 < idx_pre_char < len_s and not is_visited[idx_pre_char]:
            s_re += s[idx_pre_char]
            is_visited[idx_pre_char] = True
    return s_re


if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    n_rows = 3
    #  == 'PAHNAPLSIIGYIR'
    print(convert(s, n_rows))
    s = 'PAYPALISHIRING'
    n_rows = 4
    #  == 'PINALSIGYAHRPI'
    print(convert(s, n_rows))
    s = 'P'
    n_rows = 3
    #  == 'P'
    print(convert(s, n_rows))
