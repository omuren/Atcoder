N, X, Y = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

list_A.sort(reverse=True)
list_B.sort(reverse=True)

sweet = 0
salty = 0

for answer in range(N):
    sweet += list_A[answer]
    salty += list_B[answer]

    if sweet > X:
        break
    elif salty > Y:
        break

print(answer+1)