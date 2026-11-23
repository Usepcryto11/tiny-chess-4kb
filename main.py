import json as J,os as O,urllib.request as U
V=0,100,320,330,500,900,0;M=100000
D=-17,-15,15,17;R=-16,-1,1,16;j=-33,-31,-18,-14,14,18,31,33;y=D+R
PD=0,0,(j,0),(D,1),(R,1),(y,1),(y,0)
Q=[(7-s//16)**2 for s in range(128)]
H=0,1,2,3,3,2,1,0
Z={116:3,119:1,112:2,4:12,7:4,0:8}
B=[0]*128;S=1;W=116;X=4;N=0;G=60000;A=0;Cs=15;st=[];K={}
def w():
 global B,S,W,X,Cs;B=[0]*128;S=1;W=116;X=4;Cs=15
 for i,p in enumerate((4,2,3,5,6,3,2,4)):B[i]=-p;B[i+112]=p;B[i+16]=-1;B[i+96]=1
def f(s):return(8-int(s[1]))*16+ord(s[0])-97
def v(s):return f(s[:2])|(f(s[2:4])<<7)|(((s[4:]and'nbrq'.index(s[4])+2)or 0)<<14)
def a(q,c):
 if any(not(q+c*d&136)and B[q+c*d]==c for d in(15,17)):return 1
 if any(not(q+d&136)and B[q+d]==(2*c if d in j else 6*c)for d in j+y):return 1
 for d in D+R:
  t=q+d
  while not(t&136) and not B[t]:t+=d
  if not(t&136) and(B[t]==5*c or B[t]==(3,4)[d in R]*c):return 1
 return 0
def p(ms,sq,t2):
 ms.extend(sq|(t2<<7)|(pr<<14)for pr in((5,4,3,2)if(t2>>4)==(1-S)//2*7 else(0,)))
def g():
 ms=[]
 for sq in range(128):
  if sq&136:continue
  pz=B[sq]
  if pz==0 or pz*S<0:continue
  t=abs(pz)
  if t==1:
   d=-16*S;t2=sq+d
   if not(t2&136) and B[t2]==0:
    p(ms,sq,t2)
    if(sq>>4)==6-(1-S)//2*5:
     t3=sq+2*d
     if B[t3]==0:ms.append(sq|(t3<<7))
   for t2 in sq+d-1,sq+d+1:
    if t2&136:continue
    q=B[t2]
    if q and q*S<0:p(ms,sq,t2)
  else:
   ds,sl=PD[t]
   for d in ds:
    t2=sq+d
    while not(t2&136):
     q=B[t2]
     if q:
      if q*S<0:ms.append(sq|(t2<<7))
      break
     ms.append(sq|(t2<<7))
     if not sl:break
     t2+=d
 for kf,kt,em,bt in(116,118,(117,118),1),(116,114,(115,114,113),2),(4,6,(5,6),4),(4,2,(3,2,1),8):
  if Cs&bt and(kf==116)==(S>0)and all(not B[x]for x in em)and all(not a(x,-S)for x in(kf,)+em[:2]):ms.append(kf|(kt<<7))
 return ms
def m(mv):
 global S,W,X,Cs;f=mv&127;t=(mv>>7)&127;pr=(mv>>14)&7;pz=B[f];cp=B[t];cq=t
 if cp==0 and abs(pz)==1 and t&7!=(f&7):cq=t+16*S;cp=B[cq]
 st.append((mv,cp,cq,Cs,W,X));pl=pr*S if pr else pz;B[f]=0
 if cq!=t:B[cq]=0
 B[t]=pl
 if abs(pz)==6 and abs(t-f)==2:
  rf=t+1 if t>f else t-2;rt=t-1 if t>f else t+1;rr=B[rf];B[rf]=0;B[rt]=rr
 Cs&=~Z.get(f,0)&~Z.get(t,0)
 if abs(pz)==6:W,X=(t,X)if S>0 else(W,t)
 S=-S
 if a(W if S<0 else X,S):n();return 0
 return 1
def n():
 global S,W,X,Cs;mv,cp,cq,Cs,W,X=st.pop();f=mv&127;t=(mv>>7)&127;pr=(mv>>14)&7;S=-S;pl=B[t];B[f]=S if pr else pl;B[t]=0
 if cp:B[cq]=cp
 if abs(B[f])==6 and abs(t-f)==2:
  rf=t+1 if t>f else t-2;rt=t-1 if t>f else t+1;rr=B[rt];B[rt]=0;B[rf]=rr
def e():
 return sum((V[t:=abs(p)]+(Q[i if p>0 else i^112]if t==1 else 5*(H[i&7]+H[i>>4])if t<6 else 0))*(p//t)for i,p in enumerate(B)if p)*S+8
def o(ms,kl=0):ms.sort(key=lambda mv:(mv!=kl,-abs(B[(mv>>7)&127])))
def s(d,al,be,pl):
 global N,A;N+=1
 if N>=G:A=1;return 0
 if d<=0:
  ck=a(W if S>0 else X,-S)
  if ck:ms=g()
  else:
   st2=e()
   if st2>=be:return be
   if st2>al:al=st2
   ms=[mv for mv in g() if B[(mv>>7)&127]or(mv>>14)&7]
 else:ms=g()
 o(ms,K.get(pl,0));be2=-M-1;lg=0
 for mv in ms:
  if not m(mv):continue
  lg+=1;sc=-s(d-1 if d>0 else 0,-be,-al,pl+1);n()
  if A:return 0
  if sc>be2:be2=sc
  if sc>al:al=sc
  if al>=be:K[pl]=mv;break
 if d<=0:
  if ck and be2<-M:return -M+pl
  return al if not ck else be2
 if lg==0:return -M+pl if a(W if S>0 else X,-S)else 0
 return be2
def k(mv_uci,lg_uci):
 global N,A;w()
 for uu in mv_uci:
  if not m(v(uu)):return lg_uci[0]
 ms=[mv for mv in g() if m(mv)and not n()]
 o(ms);be=ms[0]
 for d in range(1,65):
  N=0;A=0;al=-M-1;bm=be
  for mv in ms:
   if not m(mv):continue
   sc=-s(d-1,-M-1,-al,1);n()
   if A:break
   if sc>al:al=sc;bm=mv
  if A:break
  be=bm
 a=be&127;t=(be>>7)&127;p=(be>>14)&7
 return f'{chr(97+a%8)}{8-a//16}{chr(97+t%8)}{8-t//16}{"nbrq"[p-2]if p else""}'
def pt(ph,bd):
 try:return J.load(U.urlopen(O.environ['MAKEFUN_ENV_URL']+ph,J.dumps(bd).encode()))
 except:return{}
def main():
 while 1:
  g=pt('/game',{})
  if g.get('status')=='done':break
  while g.get('status')=='your_move':
   lm=g['legal_moves']
   try:m=k(g['moves'],lm)
   except:m=lm[0]
   g=pt('/move',{'game':g['game'],'move':m})
main()
