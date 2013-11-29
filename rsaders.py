import random
import string

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def ext_gcd(x, y):
    if y == 0:
        return (x, 1, 0)
    else:
        (d, a, b) = ext_gcd(y, x%y)
    return (d, b, a-(x/y)*b)

def toChunks(m, chunkSize):
    chunk_m = []
    for ch in m:
        chunk_m.append(ord(ch).__str__())
    chunk_m_str = string.join(chunk_m, sep='')
    chunks = []
    sz = len(chunk_m_str)
    adet = (sz/chunkSize)
    for i in range(1,adet+1):
        iba = (i - 1) * chunkSize
        iso = iba + chunkSize
        chunks.append(chunk_m_str[iba:iso])
    if not (adet*chunkSize) == sz:
        iba = iso
        iso = sz
        chunks.append(chunk_m_str[iba:iso])
    return chunks

def RSAgenKeys(p,q):
    n = p * q
    pqminus = (p-1) * (q-1)
    e = int(random.random() * n)
    while gcd(pqminus,e) != 1:
        e = int(random.random() * n)
    d,a,b = ext_gcd(pqminus,e)
    if b < 0:
        d = pqminus+b
    else:
        d = b
    return ((e,d,n))

def RSAencrypt(m,e,n):
    ndigits = len(str(n))
    chunkSize = ndigits - 1
    chunks = toChunks(m,chunkSize)
    encList = []
    for messChunk in chunks:
        print messChunk
        c = modexp(messChunk,e,n)
        encList.appe
    return encList
