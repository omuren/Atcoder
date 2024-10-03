N = int(input())
list_A = list(map(int, input().split()))

if N == 1:
    print(N)
    exit()

d0 = list_A[1] - list_A[0] + 1
num = 0
answer = N
for i in range(N-1):
    d = list_A[i+1] - list_A[i]

    if d0 == d:
        num += 1
    else:
        answer += num*(num+1)/2
        num = 1

    d0 = d

answer += num*(num+1)/2

print(int(answer))