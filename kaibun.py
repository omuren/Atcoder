#値の取得
user_input1 = input()
N, K = map(int, user_input1.split())

S = input()

def check(K, lists):
    k = int(K * 0.5)
    check = 1

    for i in range(len(lists) - K + 1):
        K_lists = lists[i:i + K]
        eq = 0

        for j in range(k):
            if K_lists[j] == K_lists[K - j - 1]:
                eq += 1
            else:
                break

        if eq == k:
            check = 0
            break

    return check

def next_permutation(P): #昇順のPを降順になるまで，辞書順で並べる．
    N = len(P)

    # 1. P[i] < P[i+1] を満たす最大のiを見つける
    i = N - 2
    while i >= 0 and P[i] >= P[i + 1]:
        i -= 1

    if i == -1:
        return None  # これが最後の順列の場合

    # 2. P[i] < P[j] となる最大のjを見つける
    j = N - 1
    while P[i] >= P[j]:
        j -= 1

    # 3. P[i] と P[j] をスワップする
    P[i], P[j] = P[j], P[i]

    # 4. P[i+1], P[i+2], ..., P[N] を逆順に並べ替える
    P[i + 1:] = reversed(P[i + 1:])

    return P

def create_list(S):
    S_count = {}
    for element in S:
        if element in S_count:
            S_count[element] += 1
        else:
            S_count[element] = 1
    list_of_pairs = [[key, int(value)] for key, value in S_count.items()]
    num_list = []

    for i in range(len(list_of_pairs)):
        num_list.extend([i] * list_of_pairs[i][1])

    return num_list

####################使わないものたち
def arrange(s):
    lists = list(s)
    kaibun = lists[0]

    for i in range(len(lists) - 1):
        past_kaibun = kaibun
        kaibun = []
        add = lists[i + 1]

        for past in past_kaibun:
            for j in range(len(past) + 1):
                ap = True
                if not isinstance(past, list): #pastがlistじゃない場合，リストに変更
                    past = list(past)

                ap_lists = past[:]  # [:]で値をコピーできる．これをしないと.insert()などで元のリストも変わってしまう
                ap_lists.insert(j, add)

                for kaibun_i in kaibun:
                    if ap_lists == kaibun_i:
                        ap = False
                        break

                if ap:
                    kaibun.append(ap_lists)

    return(kaibun)

def create_list(S):
    S_count = {}
    for element in S:
        if element in S_count:
            S_count[element] += 1
        else:
            S_count[element] = 1
    list_of_pairs = [[key, int(value)] for key, value in S_count.items()]
    return list_of_pairs

def half(K, list_of_pairs):
    k = int(K*0.5)

    if K//2 == 0:
        for list_of_pair in list_of_pairs:
            half_list = []
            half_list.extend([list_of_pair[0]] * int(list_of_pair[1] / 2))
            number = arrange(k, half_list)

    else:
        number = 0
        for pair in list_of_pairs:
            pair[1] += -1
            half_list = []
            for list_of_pair in list_of_pairs:
                half_list.extend([list_of_pair[0]] * int(list_of_pair[1] / 2))
                number += arrange(k, half_list)


    return number

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main(K, S):
    lists = arrange(S)
    answer = 0
    for T in lists:
        answer += check(K, T)

    return answer

######################################
def main_re(K, S):
    P = create_list(S)
    answer = 0

    while True:
        if P == None:
            break
        answer += check(K, P)
        P = next_permutation(P)

    return answer


print(main_re(K, S))