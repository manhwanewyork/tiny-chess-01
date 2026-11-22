import json,os,sys,urllib.request as R,urllib.error as E
U=os.environ.get("MAKEFUN_ENV_URL")or sys.exit()
BG=50000
MA=100000
V=[0,100,320,330,500,900,0]
def p(t,r,f):
 c=min(f,7-f)+min(r,7-r)
 return[0,0,4,8,14,24,40,0][r]+(f in(3,4))*(r>2)*max(0,15-5*abs(r-4)) if t==1 else[0,6*c-20,4*c-8,(r==6)*15+(r==0 and f in(3,4))*5,2*c-6][t-1] if t<6 else 0
Y=[0]*2048
for x in range(1,15):
 t=x&7;o=x>>3
 if t==0 or t>5:continue
 for s in range(128):
  if s&136:continue
  r=s>>4;f=s&7;q=r if o==0 else 7-r
  Y[x*128+s]=(V[t]+p(t,q,f))*(1 if o==0 else-1)
Q=[0]*16
for t in(2,3,4,5):Q[t]=Q[t+8]=V[t]
G=0x9E3779B97F4A7C15;M=(1<<64)-1
CK=[15]*128;CK[0]=13;CK[7]=14;CK[4]=12;CK[112]=7;CK[119]=11;CK[116]=3
KN=(-33,-31,-18,-14,14,18,31,33)
KI=(-1,1,-16,16,-15,-17,15,17)
BI=(-15,-17,15,17)
RO=(-1,1,-16,16)
B=[0]*128
S=0;C=0;P=-1;F=0
K=[-1,-1]
Z=0;PS=0;NP=0;BW=0;BB=0
D=[];T={};L=[[0,0] for _ in range(128)]
N=0;LM=0;AB=False;HI=[]
def n(s):return"abcdefgh"[s&7]+str((s>>4)+1)
def u(m):
 q=m>>14&7
 return n(m&127)+n(m>>7&127)+(" pnbrqk"[q] if q else"")
def k(s,y):
 b=B;e=y<<3
 if y==0:
  if not(s-15)&136 and b[s-15]==1:return 1
  if not(s-17)&136 and b[s-17]==1:return 1
 else:
  if not(s+15)&136 and b[s+15]==9:return 1
  if not(s+17)&136 and b[s+17]==9:return 1
 for d in KN:
  t=s+d
  if not t&136 and b[t]==2|e:return 1
 for d in KI:
  t=s+d
  if not t&136 and b[t]==6|e:return 1
 for d in BI:
  t=s+d
  while not t&136:
   q=b[t]
   if q:
    if q==3|e or q==5|e:return 1
    break
   t+=d
 for d in RO:
  t=s+d
  while not t&136:
   q=b[t]
   if q:
    if q==4|e or q==5|e:return 1
    break
   t+=d
 return 0
def g(o=0):
 out=[];b=B;us=S;th=us^1
 for fr in range(128):
  if fr&136:continue
  pc=b[fr]
  if not pc or pc>>3!=us:continue
  t=pc&7
  if t==1:
   fwd=16 if us==0 else-16;rk=fr>>4;lr=6 if us==0 else 1;sr=1 if us==0 else 6;one=fr+fwd
   if b[one]==0:
    if rk==lr:
     for pr in(5,4,3,2):out.append(fr|one<<7|pr<<14)
    elif not o:
     out.append(fr|one<<7);two=one+fwd
     if rk==sr and b[two]==0:out.append(fr|two<<7|1<<20)
   for d in(fwd-1,fwd+1):
    to=fr+d
    if to&136:continue
    tg=b[to]
    if tg and tg>>3==th:
     if rk==lr:
      for pr in(5,4,3,2):out.append(fr|to<<7|pr<<14|1<<17)
     else:out.append(fr|to<<7|1<<17)
    elif to==P:out.append(fr|to<<7|1<<17|1<<18)
   continue
  if t==2 or t==6:
   for d in(KN if t==2 else KI):
    to=fr+d
    if to&136:continue
    tg=b[to]
    if tg==0 and not o or tg and tg>>3==th:out.append(fr|to<<7|(1<<17 if tg else 0))
   if t==6 and not o:
    bs=0 if us==0 else 112
    if K[us]==bs+4 and C and not k(bs+4,th):
     for bt,em,at,kg in((1 if us==0 else 4,(5,6),(5,6),6),(2 if us==0 else 8,(3,2,1),(3,2),2)):
      if C&bt and all(B[bs+x]==0 for x in em) and not any(k(bs+x,th) for x in at):out.append(bs+4|(bs+kg)<<7|1<<19)
   continue
  st=BI if t==3 else RO if t==4 else KI
  for d in st:
   to=fr+d
   while not to&136 and b[to]==0:
    if not o:out.append(fr|to<<7)
    to+=d
   if not to&136 and b[to] and b[to]>>3==th:out.append(fr|to<<7|1<<17)
 return out
def mk(m):
 global S,C,P,F,Z,PS,NP,BW,BB
 fr=m&127;to=m>>7&127;pr=m>>14&7;pc=B[fr];us=S
 cs=to-(16 if us==0 else-16) if m>>18&1 else to;cap=B[cs]
 D.append((m,cap,C,P,F,Z,PS,NP,BW,BB,K[us]))
 if cap:
  Z^=(cap*128+cs)*G&M;B[cs]=0;PS-=Y[cap*128+cs];NP-=Q[cap]
  if cap&7==3:
   if us==0:BB-=1
   else:BW-=1
 Z^=(pc*128+fr)*G&M;B[fr]=0;PS-=Y[pc*128+fr]
 pl=pr|us<<3 if pr else pc;B[to]=pl;Z^=(pl*128+to)*G&M;PS+=Y[pl*128+to]
 if pr:NP+=Q[pl]
 if pc&7==6:K[us]=to
 if m>>19&1:
  rf=fr+3 if to>fr else fr-4;rt=fr+1 if to>fr else fr-1;rk=B[rf]
  Z^=(rk*128+rf)*G&M;B[rf]=0;PS-=Y[rk*128+rf];B[rt]=rk;Z^=(rk*128+rt)*G&M;PS+=Y[rk*128+rt]
 Z^=C*G&M;C&=CK[fr]&CK[to];Z^=C*G&M
 if P!=-1:Z^=(P&7)*G&M
 P=-1
 if m>>20&1 and((not(to+1)&136 and B[to+1]==1|(us^1)<<3)or(not(to-1)&136 and B[to-1]==1|(us^1)<<3)):
  P=(fr+to)>>1;Z^=(P&7)*G&M
 F=0 if pc&7==1 or cap else F+1
 S=us^1;Z^=G;HI.append(Z)
 if k(K[us],S):uk();return 0
 return 1
def uk():
 global S,C,P,F,Z,PS,NP,BW,BB
 m,cap,C,P,F,Z,PS,NP,BW,BB,kw=D.pop()
 HI.pop()
 S^=1;fr=m&127;to=m>>7&127;pr=m>>14&7;us=S
 if m>>19&1:
  rf=fr+3 if to>fr else fr-4;rt=fr+1 if to>fr else fr-1;B[rf]=B[rt];B[rt]=0
 pl=B[to];B[to]=0;B[fr]=1|us<<3 if pr else pl
 if cap:
  cs=to-(16 if us==0 else-16) if m>>18&1 else to;B[cs]=cap
 K[us]=kw
def ks(s,c,ph,rs):
 r=s>>4;f=s&7;q=r if c==0 else 7-r
 return(([20,25,10,0,0,10,25,20][f] if q==0 else max(-50,-15*q))*ph+(8*(min(f,7-f)+min(q,7-q))-24)*rs)//6400
def ev():
 ph=min(NP,6400);rs=6400-ph
 s=PS+ks(K[0],0,ph,rs)-ks(K[1],1,ph,rs)
 s+=30*(BW>=2)-30*(BB>=2)
 return s if S==0 else-s
def od(mv,pl,tt=0):
 k0=L[pl][0];k1=L[pl][1]
 def sc(m):
  if m==tt:return 1000000
  s=0
  if m>>17&1:
   tg=B[m>>7&127];s=100000+10*V[tg&7 if tg else 1]-(B[m&127]&7)
  pr=m>>14&7
  if pr:s+=200000+V[pr]
  if s==0 and m==k0:s=50000
  elif s==0 and m==k1:s=40000
  return s
 mv.sort(key=sc,reverse=True)
def qs(a,b,pl):
 global N,AB
 N+=1
 if LM and N>=LM:AB=True;return 0
 ck=k(K[S],S^1);best=-MA-1
 if not ck:
  s=ev()
  if s>=b:return s
  best=s
  if s>a:a=s
 mv=g(not ck);od(mv,pl);lg=0
 for m in mv:
  if not mk(m):continue
  lg+=1;s=-qs(-b,-a,pl+1);uk()
  if AB:return 0
  if s>best:best=s
  if s>=b:return s
  if s>a:a=s
 if ck and lg==0:return-MA+pl
 return best
def sr(d,a,b,pl):
 global N,AB
 if pl>0 and(F>=100 or HI.count(Z)>1):return 0
 if d<=0:return qs(a,b,pl)
 N+=1
 if LM and N>=LM:AB=True;return 0
 e=T.get(Z);tt=0
 if e:
  tt=e[3]
  if e[0]>=d:
   s=e[1]
   if e[2]==1:return s
   if e[2]==2 and s>=b:return s
   if e[2]==3 and s<=a:return s
 a0=a;mv=g();od(mv,pl,tt);lg=0;best=-MA-1;bm=0
 for m in mv:
  if not mk(m):continue
  lg+=1;s=-sr(d-1,-b,-a,pl+1);uk()
  if AB:return 0
  if s>best:best=s;bm=m
  if s>a:a=s
  if a>=b:
   if not m>>17&1 and not m>>14&7 and L[pl][0]!=m:L[pl][1]=L[pl][0];L[pl][0]=m
   break
 if lg==0:return-MA+pl if k(K[S],S^1) else 0
 fl=3 if best<=a0 else 2 if best>=b else 1
 if len(T)<400000:T[Z]=(d,best,fl,bm)
 return best
def rt():
 global N,LM,AB
 mv=[]
 for m in g():
  if mk(m):mv.append(m);uk()
 if not mv:return 0
 if len(mv)==1:return mv[0]
 od(mv,0);N=0;AB=False;best=mv[0];bs=0;sc=[(m,0) for m in mv]
 for d in range(1,65):
  LM=0 if d==1 else BG;AB=False;a=-MA-1
  for i in range(len(sc)):
   m=sc[i][0];mk(m);s=-sr(d-1,-MA-1,-a,1);uk()
   if AB:break
   sc[i]=(m,s)
   if s>a:a=s
  else:
   sc.sort(key=lambda x:x[1],reverse=True);best=sc[0][0];bs=sc[0][1]
   if bs>=MA-200:break
   continue
  break
 return best
def pf(fen):
 global S,C,P,F,Z,PS,NP,BW,BB
 pa=fen.split()
 for i in range(128):B[i]=0
 rw=pa[0].split("/");Z=0;PS=0;NP=0;BW=0;BB=0
 for r in range(8):
  f=0
  for ch in rw[r]:
   if ch.isdigit():f+=int(ch)
   else:
    pc=" pnbrqk".index(ch.lower())|(0 if ch<"a" else 8);sq=(7-r)*16+f;B[sq]=pc;f+=1
    Z^=(pc*128+sq)*G&M;PS+=Y[pc*128+sq];NP+=Q[pc]
    if pc&7==3:
     if pc>>3==0:BW+=1
     else:BB+=1
    if pc&7==6:K[pc>>3]=sq
 S=0 if pa[1]=="w" else 1;C=0
 if pa[2]!="-":
  for i,ch in enumerate("KQkq"):
   if ch in pa[2]:C|=1<<i
 P=-1
 if pa[3]!="-":P=(int(pa[3][1])-1)*16+ord(pa[3][0])-97
 F=int(pa[4]) if len(pa)>4 else 0
 Z^=C*G&M
 if P!=-1:Z^=(P&7)*G&M
 if S==1:Z^=G
def ch(fen,lg):
 try:
  pf(fen);HI.append(Z);m=rt()
  if m:
   x=u(m)
   if x in lg:return x
 except Exception:pass
 return lg[0]
def po(a,b):
 q=R.Request(U+a,json.dumps(b).encode(),{"content-type":"application/json"})
 try:
  with R.urlopen(q)as r:return json.load(r)
 except E.HTTPError as e:sys.exit(e.code)
while 1:
 W=po("/game",{})
 if W["status"]=="done":break
 while W["status"]=="your_move":
  W=po("/move",{"game":W["game"],"move":ch(W["fen"],W["legal_moves"])})
 print("game",W["game"],W["outcome"],W["reason"],file=sys.stderr)
