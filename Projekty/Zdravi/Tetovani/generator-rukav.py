import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont
OUT='/tmp/claude-0/-home-user-Claude/9af43446-ef02-5723-aeca-8e80a134c248/scratchpad/tat/'
src=Image.open('/root/.claude/uploads/9af43446-ef02-5723-aeca-8e80a134c248/ff98dc19-image.png').convert('RGB')
src=src.resize((src.size[0]//2,src.size[1]//2),Image.LANCZOS)
W,H=src.size
raw=np.asarray(src).astype(np.float32)/255.
a=np.clip((np.clip(raw,0,1)**0.40-0.27)/0.67,0,1)*255.
R,G,B=a[...,0],a[...,1],a[...,2]; lum=0.299*R+0.587*G+0.114*B
def m2i(m): return Image.fromarray((np.clip(m,0,1)*255).astype(np.uint8))
def i2m(i): return np.asarray(i).astype(np.float32)/255.
def blur(m,r): return i2m(m2i(m).filter(ImageFilter.GaussianBlur(r)))
def ink(base,al,f):
    al=np.clip(al,0,1)[...,None]; f=np.array(f,np.float32)[None,None,:]
    return base*(1-al)+(base*f)*al
ARM=[(150,205),(255,168),(362,163),(378,300),(362,430),(344,560),(327,700),(318,820),
     (340,930),(400,1062),(432,1150),(358,1192),(300,1120),(245,1030),(200,930),
     (168,820),(140,700),(118,570),(100,450),(95,330),(112,248)]
pmg=Image.new('L',(W,H),0); ImageDraw.Draw(pmg).polygon(ARM,fill=255); poly=i2m(pmg)
shirt=((B-R)>10)|((lum<70)&((B-R)>0))
am=m2i(poly*(~shirt)).filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.MinFilter(9))
arm=blur(i2m(am)*poly*(1-((B-R)>28).astype(np.float32)),2.5)
arm=np.clip((arm-0.45)*4,0,1)
dark=np.clip((150-lum)/90,0,1)*arm
solid=((lum<72)*arm).astype(np.float32)
yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
ELB=(243,742)
# tlumené, průsvitné zelené (multiply filtry)
MOSS=(0.63,0.87,0.67); DEEP=(0.52,0.80,0.56); OLIV=(0.70,0.84,0.57); TEAL=(0.60,0.86,0.79)
def nf(seed,sh=(34,30)):
    n=np.random.default_rng(seed).random(sh).astype(np.float32)
    return np.asarray(Image.fromarray((n*255).astype(np.uint8)).resize((W,H),Image.BICUBIC)).astype(np.float32)/255.
def stroke(pts,wid,seed=1,steps=500,wob=0.0):
    img=Image.new('L',(W,H),0); d=ImageDraw.Draw(img)
    pts=np.array(pts,float); wid=np.array(wid,float)
    t=np.linspace(0,len(pts)-1,steps)
    xs=np.interp(t,np.arange(len(pts)),pts[:,0]); ys=np.interp(t,np.arange(len(pts)),pts[:,1])
    ws=np.interp(t,np.linspace(0,len(pts)-1,len(wid)),wid)
    r2=np.random.default_rng(seed)
    for x,y,w in zip(xs,ys,ws):
        if wob: x+=r2.normal(0,wob); y+=r2.normal(0,wob)
        d.ellipse([x-w/2,y-w/2,x+w/2,y+w/2],fill=255)
    return i2m(img)
def splat(pts,n,seed,spread=30,scale=1.6):
    img=Image.new('L',(W,H),0); d=ImageDraw.Draw(img); pts=np.array(pts,float)
    r2=np.random.default_rng(seed); t=r2.random(n)*(len(pts)-1)
    xs=np.interp(t,np.arange(len(pts)),pts[:,0]); ys=np.interp(t,np.arange(len(pts)),pts[:,1])
    for x,y in zip(xs,ys):
        x+=r2.normal(0,spread); y+=r2.normal(0,spread*1.5)
        rr=0.6+abs(r2.normal(0,1))*scale
        d.ellipse([x-rr,y-rr,x+rr,y+rr],fill=255)
    return i2m(img)

# 1 PRŮTAH
p1=[(316,200),(290,322),(260,452),(230,580),(209,690),(203,792),(224,884),(268,986),(316,1070)]
band=blur(stroke(p1,[130,124,110,96,83,71,62,54,44],3),11)
band=np.clip(band*1.15*np.clip(nf(12,(16,70))*1.5+0.32,0,1),0,1)
di=Image.new('L',(W,H),0); dd=ImageDraw.Draw(di); r3=np.random.default_rng(5)
for bx,by in [(300,330),(268,470),(240,560),(226,608),(210,700),(196,762),(250,898),(283,980)]:
    dd.rectangle([bx,by,bx+int(r3.integers(2,4)),by+int(r3.integers(45,150))],fill=255)
al1=np.clip(np.maximum(band*0.62,blur(i2m(di),2)*1.5*0.45),0,1)*arm*(1-0.92*solid)
v1=ink(a,al1,MOSS)
# 2 KRAJINA
reg=blur((yy<730).astype(np.float32),55)
elb=blur((((xx-ELB[0])/95)**2+((yy-ELB[1])/108)**2<1).astype(np.float32),26)
al2=np.clip(dark*1.9*np.maximum(reg,elb*0.95),0,1)*arm*(1-0.8*solid)*0.9
v2=ink(a,al2,MOSS)
# 3 JEMNÉ CÁKANCE
s=np.clip(splat([(258,560),(240,660),(228,750),(218,840),(232,930)],430,13,spread=44,scale=1.25)
         +splat([(322,262),(296,380),(268,500)],170,11,spread=40,scale=1.0)*0.9
         +splat([(214,980),(246,1050)],90,17,spread=34,scale=1.0)*0.7,0,1)
al3=np.clip(blur(s,0.9)*1.25,0,1)*arm*0.62
v3=ink(a,al3,DEEP)
# 4 PROTIVÁHA SLUNCI
mass=blur((((xx-243)/102)**2+((yy-880)/160)**2<1).astype(np.float32),24)
mass=np.clip(mass*1.3*np.clip(nf(21,(40,26))*1.7+0.2,0,1),0,1)
arc=np.zeros((H,W),np.float32)
for k,off in enumerate([0,17,36]):
    arc=np.maximum(arc,stroke([(300-off,758),(250-off,830),(214-off,916),(232-off,1006)],[8,11,9,5],30+k,wob=0.7))
echo=blur((((xx-ELB[0])/76)**2+((yy-ELB[1])/84)**2<1).astype(np.float32),22)
al4=np.clip(mass*0.62+blur(arc,2)*0.75+echo*0.42,0,1)*arm*(1-0.9*solid)
v4=ink(a,al4,OLIV)
# 5 DIAGONÁLY
dz=np.clip(stroke([(372,258),(240,430),(112,596)],[15,11,6],41,wob=0.9)
          +stroke([(380,300),(250,480),(124,656)],[12,9,5],42,wob=0.9)
          +stroke([(330,560),(252,700),(206,842),(228,980)],[10,8,6,4],43,wob=0.9),0,1)
dz=blur(dz,2.2)*np.clip(nf(31,(150,18))*2.2-0.15,0,1)*np.clip(nf(37,(22,40))*1.5+0.2,0,1)*1.4
al5=np.clip(dz*1.35+blur(splat([(300,420),(240,560),(214,700),(222,860)],260,44,spread=26,scale=1.2),0.8)*0.7,0,1)*arm*0.85
v5=ink(a,al5,DEEP)
# 6 NEGATIVNÍ PROSTOR
free=np.clip(1-blur(dark,14)*2.2,0,1)*arm
zone=blur(((yy>430)&(yy<980)).astype(np.float32),50)
al6=np.clip(free*zone*np.clip(nf(51,(26,22))*1.8+0.1,0,1)*1.1,0,1)*0.6
v6=ink(a,al6,TEAL)

CZ=['PŮVODNÍ','1 — PRŮTAH','2 — ZELEŇ DO KRAJINY','3 — CÁKANCE',
    '4 — PROTIVÁHA SLUNCI','5 — PODÉL DIAGONÁL','6 — NEGATIVNÍ PROSTOR']
ps=[a,v1,v2,v3,v4,v5,v6]
for i,p in enumerate(ps): Image.fromarray(np.clip(p,0,255).astype(np.uint8)).save(OUT+f'r{i}.png')
X0,X1,Y0,Y1=72,448,150,1205
sc=0.80; pw,ph=int((X1-X0)*sc),int((Y1-Y0)*sc); pad,lab=12,40
cols=4; rows=2
sheet=Image.new('RGB',(pw*cols+pad*(cols+1),(ph+lab)*rows+pad*(rows+1)),(18,18,18))
d=ImageDraw.Draw(sheet); font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',19)
for i,p in enumerate(ps):
    r,c=divmod(i,cols); x=pad+c*(pw+pad); y=pad+r*(ph+lab+pad)
    sheet.paste(Image.fromarray(np.clip(p,0,255).astype(np.uint8)).crop((X0,Y0,X1,Y1)).resize((pw,ph),Image.LANCZOS),(x,y))
    d.text((x+2,y+ph+10),CZ[i],font=font,fill=(235,235,235))
sheet.save(OUT+'navrhy-ruka.png'); print('ok',sheet.size)
