N, M =map(int, input().split())
A_list = list(map(int, input().split()))

if sum(A_list) <= M:
    print("infinite")
    exit()

A_list.sort()

sum_A = 0
x = 0
for n in range(len(A_list)-1):
    sum_A += A_list[n]
    grants =sum_A + (N-n-1)*A_list[n+1]
    if grants > M:
        x = (M - sum_A) // (N-n-1)
        break

print(x)

#交通費が低い人から順に支給していく．
# n人目が満額支給されたとき，n+1人目からN人目まではn人目と同じ額を支給する．
# 予算額を超えたら　((n-1)人目までの満額 ) + ((N-m+1)人にx円)< (予算の残額 )　 となる最大のxにする
# x = int((M-A_list[:n-2])/(N-m+1))

##二分探索法を用いる
def binary_search(arr,x):
  #l,rはどこからどこまでの配列を調べるかを与えます
  l = -1
  r = len(arr) - 1
  while r-l>1:
    mid = l + (r-l)//2
    if x == arr[mid]:  # xがちょうど中間にあったとき
      return mid
    elif x < arr[mid]: # xが左側の配列にあるとき
      r = mid
    else:              # xが右側の配列にあるとき
      l = mid
  if x==arr[r]:
      return r
  return -1