n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

result = []

i = 0
j = 0
while i < len(n_list) or j < len(m_list):
    if n_list[i] <= m_list[j]:
        result.append(n_list[i])
        i += 1
    else:
        result.append(m_list[j])
        j += 1
    while i >= len(n_list) and j < len(m_list):
        result.append(m_list[j])
        j += 1
    while j >= len(m_list) and i < len(n_list):
        result.append(n_list[i])
        i += 1

print(result)

# result = n_list + m_list
#
# result.sort()
#
# print(result)