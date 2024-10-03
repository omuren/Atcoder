N = int(input())

#sum_L = 0
#sum_R = 0
L_list = []
R_list = []

for n in range(N):
    L, R = map(int, input().split())
    L_list.append(L)
    R_list.append(R)
    #sum_L += L
    #sum_R += R

sum_L = sum(L_list)
sum_R = sum(R_list)

if sum_L <= 0 and sum_R >= 0:
    print("Yes")
    X_list = L_list[:]
    i = 0
    while sum_L <= 0:
        X_list[i] = R_list[i]
        sum_L += R_list[i] - L_list[i]
        i += 1

    X_list[i-1] = X_list[i-1] - sum_L
    print(*X_list)

else:
    print("No")

#3つほどエラーがでてしまった