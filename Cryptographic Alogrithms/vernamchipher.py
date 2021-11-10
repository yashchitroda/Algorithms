vernam_dict = dict((i, chr(i + 96)) for i in range(1, 27))
# Vernam by replacing char of plain by char(ord(sum of plain and key))
def vernam_encrypt(plain, key):
    plain = plain.lower()
    ckey = ''.join([(key[i % len(key)]) for i in range(len(list(plain)))])
    print(ckey)
    cipher = ''
    for i in range(len(plain)):
        if plain[i] == ' ':
            cipher += ' '
        else:
            cipher += vernam_dict[(ord(plain[i]) + ord(ckey[i])) % 26]
    print(cipher, plain)

print(vernam_encrypt('mountains are bae', 'HELLO'))



def vernam_decrypt(ctext, key):
    cupper = ctext.upper()
    text_num = [letters.index(u) for u in cupper]
    intm_key = [letters.index(ik) for ik in key]
    c = ''
    for i in range(len(cupper)):
        ee = text_num[i] - intm_key[i]
        if ee < 0:
            c += letters[ee + 26]
        else:
            c += letters[ee]
    return c
  
