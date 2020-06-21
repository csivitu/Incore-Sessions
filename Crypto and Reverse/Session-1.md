# Crypto and Reverse

- Date: 21 June 2020
- Authors: [roerohan](https://github.com/roerohan), [thebongy](https://github.com/thebongy)

An intro to reversing challenges, `pwntools`, tips and tricks in Python, and basic ciphers such as Caesar's, XOR, and RSA.

# Requirements

- Python 3

# Source

- [incore.py](./incore.py): Reverse challenge

# Reversing

Python is a really simple and powerful tool for CTFs. We went over:

- Intuition on how to recognize what the challenge is actually doing
- Caesar's cipher - calculating offsets etc.
- binary strings
- netcat
- pwntools

> A detailed description of the challenge can be found [here](https://github.com/csivitu/CTF-Write-ups/blob/master/NahamCon%20CTF/Scripting/Rotten/script.py).

The challenge basically returned a string each time you sent a message, with 1 or 0 characters of the flag in it. This would take hours to solve manually, decrypting the Caesar's cipher everytime. Instead, we wrote a python script to do it for us.

```python
flag = [None]*100
def response(s): 
    offset = ord(s[0]) - ord('s')

    position = 0

    res = ''
    for i in s:
        if not i.isalpha():
            if i.isnumeric():
                position = position*10 + int(i)

            res += i
            continue
        res += chr((ord(i) - ord('a') - offset) % 26 + ord('a'))

    if len(res) == 55:
        return res
    
    flag[position] = res[-2]

    return res

from pwn import remote

r = remote('jh2i.com', 50034)

while True:
    received = r.recv()
    x = received.decode().strip()

    print(x)
    y = response(x)
    r.send(y)    
    print(y)
    print()
    f = ''.join([i for i in flag if i != None])
    print(f)
    print()

# Rotten

```

# Crypto

- [Caesar's Cipher](#Reversing)
- XOR Encryption
- RSA Algorithm
