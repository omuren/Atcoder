Q = int(input())
kind = []
num = []
length = 0
for q in range(Q):
    query = input()
    if query == "3":
        print(length)
    else:
        run, x = map(int, query.split())
        if run == 1:
            notin = True
            for k in range(length):
                if x == kind[k]:
                    num[k] += 1
                    notin = False
                    break
            if notin:
                kind.append(x)
                num.append(1)
                length += 1

        else:
            for k in range(length):
                if x == kind[k]:
                    num[k] += -1
                    if num[k] == 0:
                        del kind[k]
                        del num[k]
                        length += -1
                    break

#回答例
# q = int(input())
# cnt = [0] * 1000000 #ここのリストの番号がxの値になる　これで計算時間が短縮されている
# ans = 0
#
# for _ in range(q):
#     t,*x = map(int,input().split())
#     if t == 1:
#         x[0] -= 1 #リストは0からスタートなので-1している
#         cnt[x[0]] += 1 #リスト番号x-1に1を足す
#         if cnt[x[0]] == 1: #1なら種類が増えるからansを1足す
#             ans += 1
#     elif t == 2:
#         x[0] -= 1
#         cnt[x[0]] -= 1
#         if cnt[x[0]] == 0: #0なら種類が減るからansを1減らす
#             ans -= 1
#     else:
#         print(ans)

