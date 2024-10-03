S = list(input())
T = list(input())

num = 0
ans = []
T_large_element = []
T_large_element_num = []

for i in range(len(S)):
    if T[i] == S[i]:
        pass

    elif T[i] < S[i]:
        num += 1
        S[i] = T[i]
        ans.append(''.join(S.copy()))
    else:
        num += 1
        T_large_element.append(T[i])
        T_large_element_num.append(i)

for j in range(len(T_large_element)):
    S[T_large_element_num[-j-1]] = T[T_large_element_num[-j-1]]
    ans.append(''.join(S.copy()))

print(num)
for answer in ans:
    print(answer)
