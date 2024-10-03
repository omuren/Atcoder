K = 4
N = 9
S = "EXCELLENT"
k = int(K*0.5)
n = int(N*0.5)

S_count = {}

def check(K, lists):
    k = int(K*0.5)
    check = 1
    for i in range(len(lists)-K):
        K_lists = lists[i:i+K-1]
        eq = 0
        for j in range(k):
            if K_lists[j] == K_lists[K-j+1]:
                eq += 1
            else:
                break
        if eq == k:
            check = 0
            break

    return check

def arrange(k, s):
    lists = list(s)
    if k > len(lists):
        number = 0
    else:
        kaibun_num = lists[0]
        for i in range(len(lists) - 1):
            past_kaibun_num = kaibun_num
            kaibun_num = []
            add = lists[i + 1]

            for past in past_kaibun_num:
                for j in range(len(past) + 1):
                    ap = True

                    if not isinstance(past, list): #pastがlistじゃない場合，リストに変更
                        past = list(past)

                    ap_lists = past[:]  # [:]で値をコピーできる．これをしないと.insert()などで元のリストも変わってしまう
                    ap_lists.insert(j, add)

                    for kaibun_num_i in kaibun_num:
                        if ap_lists[:k] == kaibun_num_i:
                            ap = False
                            break

                    if ap:
                        kaibun_num.append(ap_lists[:k])

        number = len(kaibun_num)

    return(number)

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

all_number = factorial(3)
print(all_number)

for element in S:
    if element in S_count:
        S_count[element] += 1
    else:
        S_count[element] = 1
print(S_count)
list_of_pairs = [[key, int(value)] for key, value in S_count.items()]
print(list_of_pairs)
num_list = []
for i in range(len(list_of_pairs)):
    num_list.extend([i] * list_of_pairs[i][1])
print(num_list)

lists = list(S)
#lists = lists[:K]
#print(lists)

new_lists = []
kaibun_num = lists[0]

for i in range(len(lists)-1):
    past_kaibun_num = kaibun_num
    #print(past_kaibun_num)
    kaibun_num = []
    add = lists[i+1]

    for past in past_kaibun_num:
        for j in range(len(past)+1):
            ap = True
            ap_lists = []
            if not isinstance(past, list):
                past = list(past)
            ap_lists = past[:] #[:]で値をコピーできる．これをしないと.insert()などで元のリストも変わってしまう
            ap_lists.insert(j, add)
            #print(f"ap{ap_lists}")

            for k in range(len(kaibun_num)):
                if ap_lists[:K] == kaibun_num[k]:
                    ap = False
                    break

            if ap:
                kaibun_num.append(ap_lists[:K])
                #print(kaibun_num)

number = len(kaibun_num)

print(number)

a = "aoindff"
b = list(a)
b.sort()
print(b)

