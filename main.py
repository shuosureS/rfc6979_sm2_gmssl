import hashlib
from gmssl import sm2,sm3,func
import hmac
q=164662474442864913204610293692179443533679901685075671686168943558347871758383
qlen=256
rlen=256

def int2octets(x):#x为整数，返回字符串
    base,minlen=256,32
    code_string = ''.join([chr(x) for x in range(256)])
    result = ""


    while x > 0:
        temp = x % base
        result = code_string[temp] + result
        x =x//base
    if len(result)>=minlen:
        return result
    return 'a'*(minlen-len(result))+result
def bits2octets(string):
    z1=bits2int(string)
    z2=z1%q
    return int2octets(z2)
def bits2int(string):

    base = 256
    code_string =''.join([chr(x) for x in range(256)])
    if len(string)>=qlen:
        string=string[:qlen]
    else:
        string=(qlen-len(string))*code_string[0]+string
    result = 0
    while len(string) > 0:
        result *= 2
        result += code_string.find(string[0])
        string = string[1:]
    return result



def gen_k(data,x):
    v = '\x01' * 32
    k = '\x00' * 32
    h1=sm3.sm3_hash(func.bytes_to_list(data))
    tx=int2octets(x)
    th1=bits2octets(h1)
    k=hmac.new(k.encode(),(v+'\x00'+tx+th1).encode(),hashlib.sha256).digest()
    v = hmac.new(k, v.encode(), hashlib.sha256).digest()
    k = hmac.new(k, v +('\x01' + tx + th1).encode(), hashlib.sha256).digest()
    v = hmac.new(k, v, hashlib.sha256).digest()
    tlen=0
    T=b''
    while(tlen<qlen):
        v = hmac.new(k, v, hashlib.sha256).digest()
        T=T+v
        tlen=len(T)
    TT=T.decode(errors='ignore')
    K=bits2int(TT)
    if K >=1 & K<q:
        return K
    else:
        while K>=q:
            k=hmac.new(k, v +('\x00' ).encode(), hashlib.sha256).digest()
            v=hmac.new(k, v, hashlib.sha256).digest()
            K = bits2int(T.decode(errors='ignore'))
    return K
private_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
public_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
sm2_crypt = sm2.CryptSM2(
    public_key=public_key, private_key=private_key)
data = b"1111" # bytes类型
k=gen_k(data,int(private_key,16))
print(k)
'''
data = b"1111" k=31338491022916135759812321691097177620246
data = b"111"  k=56088773151934583287914657276110050933269961
'''

sign = sm2_crypt.sign(data, hex(k)[2:])
assert sm2_crypt.verify(sign, data)



