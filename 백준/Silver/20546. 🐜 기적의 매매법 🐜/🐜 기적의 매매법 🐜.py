m = int(input())
p = list(map(int, input().split()))

# BNP
bm = m #준현이가 보유한 돈
bs = 0 #가진 주식 수

for i in p:
    if bm >= i:
        s = bm // i #몫
        bs += s
        bm -= s * i 
b = bm + p[-1] * bs

# TIMING
tm = m
ts = 0

for i in range(3, len(p)):
    # 상승 - 매도
    if p[i-3]<p[i-2]<p[i-1] :
        tm += ts * p[i]
        ts = 0
        
    # 하락 - 매수
    elif p[i-3]>p[i-2]>p[i-1] :
        s = tm // p[i]
        ts += s
        tm -= s * p[i] 
        
t = tm + ts * p[-1]

if t > b :
    print("TIMING")
elif t < b:
    print("BNP")
else :
    print("SAMESAME")