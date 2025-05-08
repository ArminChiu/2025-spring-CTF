def decrypt(key, ct):
    pt = ''
    for i in range(len(ct)):
        ct_val = ord(ct[i]) - 0x20
        key_val = ord(key[i % len(key)]) - 0x20
        pt_val = (ct_val - key_val) % 95
        pt += chr(pt_val + 0x20)
    return pt

# Given data
key = "welcome_to_the_crypto_world!"
ct = "FK@)k7ESiQNYHXEEWsP&\"r,%)'m~"

# Decrypt
flag = decrypt(key, ct)
print(flag)