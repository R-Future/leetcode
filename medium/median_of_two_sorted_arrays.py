def find_median_sorted_arrays(nums1: list, nums2: list) -> float:
    len_1 = len(nums1)
    len_2 = len(nums2)
    nums3 = []
    i_1 = 0
    i_2 = 0
    while i_1 < len_1 and i_2 < len_2:
        if nums1[i_1] < nums2[i_2]:
            nums3.append(nums1[i_1])
            i_1 += 1
        else:
            nums3.append(nums2[i_2])
            i_2 += 1
    if i_1 < len_1:
        nums3.extend(nums1[i_1:])
    else:
        nums3.extend(nums2[i_2:])
    len_3 = len_1 + len_2
    mid = len_3 // 2
    if len_3 % 2 == 0:
        return float(nums3[mid] + nums3[mid - 1]) / 2
    else:
        return float(nums3[mid])


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(find_median_sorted_arrays(nums1, nums2))
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(find_median_sorted_arrays(nums1, nums2))
