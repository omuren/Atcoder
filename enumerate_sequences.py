N, K = map(int, input().split())
R_list = list(map(int, input().split()))

A_list = [1]*N

if N % K == 0:
    print(' '.join(map(str, A_list)))

while A_list != R_list:
    for i in range(N):
        if A_list[N-1-i] < R_list[N-1-i]:
            A_list[N-1-i] += 1
            break
        else:
            A_list[N-1-i] = 1

    if sum(A_list) % K == 0:
        print(' '.join(map(str, A_list)))