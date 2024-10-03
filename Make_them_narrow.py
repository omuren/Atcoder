N, K = map(int, input().split())
list_A = list(map(int, input().split()))

list_A.sort()
answer = list_A[N-K-1] - list_A[0]
for i in range(K+1):
    answer = min(answer, list_A[N-K-1+i]-list_A[i])

print(answer)

#Correct!!!