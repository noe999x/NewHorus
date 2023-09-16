#--> import function into main code

#--> Do not remove
import random

#--> Module Method Chaining
rr = random.randint
rd = random.randrange
rc = random.choice

#--> For Regular Method
def u1():
    aa='Mozilla/5.0 (Linux; Android 6.0.1;'
    b=rc(['5','6','7','8','9','10','11','12'])
    c=' SM-G532G Build/MMB29T; wv)'
    d=rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=rd(1, 999)
    f=rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105'
    h=rd(73,100)
    i='0'
    j=rd(4200,4900)
    k=rd(40,150)
    l='Mobile Safari/537.36 UCBrowser/11.3.0.1130 (UCMini) Mobile'
    uaku1=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    return uaku1

def u2():
    aa='Mozilla/5.0 (Linux; Android 11;'
    b=rc(['6','7','8','9','10','11','12'])
    c='SM-A205F Build/RP1A.200720.012; wv)'
    d=rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=rd(1, 999)
    f=rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71'
    h=rd(73,100)
    i='0'
    j=rd(4200,4900)
    k=rd(40,150)
    l='Mobile Safari/537.36 UCBrowser/11.5.2.1188(SpeedMode) U4/1.0 UCWEB/2.0 (UCMini) Mobile'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    return uaku2

def u3():
    aa='UCWEB/2.0 (Linux; U; Opera Mini/7.1.32052/30.3697;'
    b=rc(['6','7','8','9','10','11','12'])
    c='en-US; SM-G532G Build/MMB29T)'
    d=rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=rd(1, 999)
    f=rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='U2/1.0.0 UCMini/10.9.0.946'
    h=rd(73,100)
    i='0'
    j=rd(4200,4900)
    k=rd(40,150)
    l='(SpeedMode; Android 6.0.1; SM-G532G Build/MMB29T) Mobile'
    uaku3=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    return uaku3

#--> If you want to change the string using your preferred user-agent, simply modify the structure of the string above without changing the function name.
