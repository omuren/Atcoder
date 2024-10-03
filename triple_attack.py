N = int(input())
H_list = list(map(int, input().split()))
T = 0
r_T = 0
for n in range(N):
    q, r = divmod(H_list[n], 5)
    if r_T == 0:
        if r > 2:
            T += 3*q + 3
        elif r == 0:
            T += 3*q
        else:
            T += 3*q + r
            r_T = r

    elif r_T == 1:
        if r > 1:
            T += 3*q + 2
            r_T = 0
        elif r == 1:
            T += 3*q + 1
            r_T = 2
        else:
            T += 3*q

    else:
        if r == 0:
            T += 3*q
        elif r == 4:
            T += 3*q + 2
            r_T = 1
        else:
            T += 3*q + 1
            r_T = 0

print(T)

#回答例　スマートだった
# N = int(input())
# A = list(map(int,input().split()))
# T = 0
# for a in A:
#   num = a//5
#   T += num*3
#   a -= num*5
#   while a>0: #a<=0でおしまい
#     T+=1
#     if T%3==0: #３の倍数なら3引いて３の倍数じゃないなら１引く
#       a-=3
#     else:
#       a-=1
#
# print(T)
