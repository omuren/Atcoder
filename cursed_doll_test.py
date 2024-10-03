#値の取得
NTP = input()
L = input()
N, T, P = map(int, NTP.split())
L_lists = list(map(int, L.split()))

#L_listsを降順に
L_lists.sort(reverse=True)

#P番目に長い髪の人をLpとする
Lp = L_lists[P-1]

#LpがT以上になるまでループ
answer = 0
while Lp < T:
    answer += 1
    Lp += 1

print(answer)