def count(mid):
    cnt = 1
    sum = 0
    for x in a:
        if sum + x > mid:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


n, m = map(int, input().split())

a = list(map(int, input().split()))

left = 1
right = sum(a)
max_value = max(a)
res = 0
while left <= right:
    mid = (left + right) // 2
    cnt = count(mid)
    if mid >= max_value and cnt <= m:
        res = mid
        right = mid - 1
    else:
        left = mid + 1

print(res)

"""
9 3
1 2 3 4 5 6 7 8 9
"""

# def Count(capacity):
#     cnt=1
#     sum=0
#     for x in Music:
#         if sum+x>capacity:
#             cnt+=1
#             sum=x
#         else:
#             sum+=x
#     return cnt
#
# n, m=map(int, input().split())
# Music=list(map(int, input().split()))
# maxx=max(Music)
# lt=1
# rt=sum(Music)
# res=0
# while lt<=rt:
#     mid=(lt+rt)//2
#     if mid>=maxx and Count(mid)<=m:
#         res=mid
#         rt=mid-1
#     else:
#         lt=mid+1
# print(res)
