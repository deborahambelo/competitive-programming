def isSubset( a1, a2, n, m):
    count_a2 = dict()
    for num in a2:
        if num in count_a2:
            count_a2[num] += 1
        else:
            count_a2[num] = 1
            
    count_a1 = dict()
    for num in a1:
        if num in count_a1:
            count_a1[num] += 1
        else:
            count_a1[num] = 1
            
    for key in count_a2:
        if (key in count_a1) and count_a2[key] <= count_a1[key]:
            continue
        return "No"
    return "Yes"
