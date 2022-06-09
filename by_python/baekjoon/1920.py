N = int(input())
nums1 = list(map(int, input().split()))
nums_dict = {i: 1 for i in nums1}

M = int(input())
nums2 = list(map(int, input().split()))

for n in nums2:
    try:
        if nums_dict[n] == 1:
            print(1)
    except:
        print(0)


"""
5
4 1 5 2 3
5
1 3 7 9 5
"""