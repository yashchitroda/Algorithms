def columnar_encrypt(text,key):
    m = { i: [] for i in key }
    cols = [list(text[j:j+len(key)]) for j in range(0,len(text), len(key))]
    if len(cols[-1]) < len(key):
        while len(cols[-1]) != len(key):
            cols[-1].append(' ')
    i=0
    for k in m.keys():
        if i< len(key):
            for j in cols:
                m[k] += j[i]
            i += 1
    s = {k: m[k] for k in sorted(m)}
    cipher = ''
    for i in s.keys():
        for x in s[i]:
            cipher += x
    print(m)
    return cipher
print(columnar_encrypt('tree is green', 'HACK'))
