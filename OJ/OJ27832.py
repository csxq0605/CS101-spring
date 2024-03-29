N ,M= map(int, input().split())
nums = list(map(int, input().split()))
ops = [input().split() for _ in range(M)]
MOD = 65536
prefix_sum = [[0] * (1 << (i+1)) for i in range(16)]
for i in range(N):
    for j in range(16):
        prefix_sum[j][nums[i] % (1 << (j+1))] += 1
for i in range(16):
    for j in range(1, 1 << (i+1)):
        prefix_sum[i][j] += prefix_sum[i][j-1]
add = 0
for op in ops:
    if op[0] == 'C':
        add = (add + int(op[1])) % MOD
    else:
        i = int(op[1])
        r = (1 << (i+1)) - 1 - add % (1 << (i+1))
        l ,ans = map(int,(r - (1 << i) ,0)) if r >= 1 << i else map(int,(r + (1 << i) ,N))
        print(ans + prefix_sum[i][r] - prefix_sum[i][l])