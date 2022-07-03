ct = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
ct = bytes.fromhex(ct)

# print(ct)
flag_format = b"crypto{"
key = [ o1^o2 for (o1, o2) in zip(ct, flag_format)] 
# + [ord("y")]
print(key)

flag = []
key_len = len(key)
for i in range(len(ct)):
    flag.append(
        ct[i] ^ key[i % key_len]
    )
flag = "".join(chr(o) for o in flag)
print(flag)