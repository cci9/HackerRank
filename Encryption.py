def encryption(s):
    l = (len(s))**0.5
    if int(l) * int(l) == len(s):
        r = int(l)
        c = int(l)
    else:
        r = int(l)
        c = int(l + 1)
    i = 0
    p = ''
    j = 1
    while i < len(s):
        if i == max((r * j), (c * j)) - 1:
            j += 1
            p = p + s[i] + '\n'
            i = i + 1
        else:
            p = p + s[i]
            i = i + 1
    q = ''
    for i in range(max(r, c)):
        q = q + p[i]
        k = 1
        for j in range(len(p)):
            if j == i + max(r, c) * k + k:
                q = q + p[j]
                k = k + 1
        q = q + ' '
    return q