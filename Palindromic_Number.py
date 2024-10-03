N = input()
N_int = int(N)
N_list = [int(n) for n in N]
digits = len(N_list)

def create_list(remainder, k):
    rd_list = [int(rd) for rd in str(remainder)]
    while len(rd_list) < k+1:
        rd_list.insert(0, 0)
    rd_list_reverse = rd_list[:]
    rd_list_reverse.reverse()
    return(rd_list, rd_list_reverse)

if N_int < 10:
    answer = N_int -1
    print(answer)
    exit()

if N_list[0] == 1:
    k = digits-2
    remainder = N_int - 2*10**k

else:
    k = digits-1
    remainder = N_int - 2*10**k

if remainder < 9*10**k:
    rd_list, rd_list_reverse = create_list(remainder, k)
    del rd_list_reverse[0]
    answer_list = rd_list + rd_list_reverse

else:
    remainder += -9*10**k
    rd_list, rd_list_reverse = create_list(remainder, k)
    answer_list = rd_list + rd_list_reverse

answer_list[-1] += 1
answer_list[0] += 1

answer = int(''.join(map(str, answer_list)))
print(answer)