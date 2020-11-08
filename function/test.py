def combinationSum(candidates, target):
    dp = [[] for i in range(target+1)]

    for c in candidates:
        for i in range(target+1):
            if i<c:
                continue
            if i==c:
                dp[i].append(c)
            else:
                for blist in dp[i-c]:
                    dp[i].append(blist+c)

    return dp
print(combinationSum([6,9,20], 18))
list2 = [list(set(x)) for x in combinationSum([6,9,20], 18) if x != []]
for i in list2:
    print(str(i).replace("[", '').replace("]", ''))