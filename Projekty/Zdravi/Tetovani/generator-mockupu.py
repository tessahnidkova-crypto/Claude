import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont
OUT='/tmp/claude-0/-home-user-Claude/9af43446-ef02-5723-aeca-8e80a134c248/scratchpad/tat/'
src=Image.open('/root/.claude/uploads/9af43446-ef02-5723-aeca-8e80a134c248/da7b52a1-image.png').crop((150,900,1050,1850)).convert('RGB')
raw=np.asarray(src).astype(np.float32)/255.
# tone-map (fotka je P3/HDR a syrově hodně tmavá)
y=np.clip(raw,0,1)**0.40
a=np.clip((y-0.27)/0.67,0,1)*255.
W,H=src.size
R,G,B=a[...,0],a[...,1],a[...,2]
lum=0.299*R+0.587*G+0.114*B
bg=(lum>205)&(np.abs(R-B)<25)
skin=(~bg).astype(np.float32)
dark=((lum<95)*skin)
def m2i(m): return Image.fromarray((np.clip(m,0,1)*255).astype(np.uint8))
def i2m(i): return np.asarray(i).astype(np.float32)/255.
def blur(m,r): return i2m(m2i(m).filter(ImageFilter.GaussianBlur(r)))
def ink(base,alpha,filt):
    al=np.clip(alpha,0,1)[...,None]; f=np.array(filt,np.float32)[None,None,:]
    return base*(1-al)+(base*f)*al
F_MOSS=(0.46,0.88,0.55); F_TEAL=(0.44,0.86,0.78); F_DEEP=(0.28,0.74,0.38); F_LIME=(0.58,0.97,0.42)
yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
CX,CY=360,520
near=np.clip(blur(np.clip(1-np.sqrt(((xx-CX)/300)**2+((yy-CY)/300)**2),0,1),20)*2.6,0,1)
def brush(cx,cy,rx,ry,rot,seed,edge=0.5):
    rng=np.random.default_rng(seed); n=rng.random((28,26)).astype(np.float32)
    n=np.asarray(Image.fromarray((n*255).astype(np.uint8)).resize((W,H),Image.BICUBIC)).astype(np.float32)/255.
    c,s=np.cos(rot),np.sin(rot)
    X=((xx-cx)*c+(yy-cy)*s)/rx; Y=(-(xx-cx)*s+(yy-cy)*c)/ry
    return blur(np.clip((1.0-np.sqrt(X*X+Y*Y))/edge+(n-0.5)*0.85,0,1),9)
# 1 LAZURA
sw=np.maximum(brush(300,440,290,130,-1.02,11), brush(235,540,190,95,-0.95,5)*0.9)
drip=np.zeros((H,W),np.float32)
rng=np.random.default_rng(4)
for dx0 in [150,192,236,300,355,410,455]:
    w0=rng.integers(3,7); l0=rng.integers(90,260)
    y0=int(560+rng.integers(-40,60))
    drip[y0:y0+l0, dx0:dx0+w0]=0.75
drip=blur(drip,3)*1.2
al1=np.clip(np.maximum(sw*0.8, drip*0.55),0,1)*skin*(1-0.92*dark)
v1=ink(a,al1,F_MOSS)
# 2 MISPRINT
sh=blur(np.roll(np.roll(dark,-34,0),-28,1),2.0)
al2=np.clip(sh-dark*1.3,0,1)*near*1.0*skin
v2=ink(a,al2,F_DEEP)
# 3 LINKY + CAKANCE
core=i2m(m2i(dark).filter(ImageFilter.MinFilter(9)).filter(ImageFilter.MaxFilter(15)))
al3=np.clip(blur(np.clip(dark-core,0,1),1.0)*1.8,0,1)*near
v3=ink(a,al3,F_DEEP)
# 4 GLOW
h=np.clip((blur(dark,28)-0.12)*1.6,0,1)
al4=h*(1-dark)*skin*near*0.95
v4=ink(a,al4,F_TEAL)
# 5 JEDEN LISTEK
pet=blur(((((xx-268)/105)**2+((yy-575)/120)**2)<1).astype(np.float32),8)
inside=np.clip((blur(dark,9)-0.25)*2.2,0,1)
shade=np.clip((110-lum)/70,0,1)*skin
al5=np.clip(pet*inside*(0.35+0.85*shade),0,1)*0.95
v5=ink(a,al5,F_LIME)
CZ=['PŮVODNÍ (dorovnaný jas)','1 — LAZURA ZA ČTYŘLÍSTKEM','2 — POSUNUTÁ VRSTVA (misprint)',
    '3 — ZELENÉ LINKY A CÁKANCE','4 — PODSVÍCENÍ / GLOW','5 — JEN JEDEN LÍSTEK']
ps=[a,v1,v2,v3,v4,v5]
for i,p in enumerate(ps): Image.fromarray(np.clip(p,0,255).astype(np.uint8)).save(OUT+f'x{i}.png')
sc=0.62; pw,ph=int(W*sc),int(H*sc); pad,lab=14,48
sheet=Image.new('RGB',(pw*3+pad*4,(ph+lab)*2+pad*3),(18,18,18)); d=ImageDraw.Draw(sheet)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',23)
for i,p in enumerate(ps):
    r,c=divmod(i,3); x=pad+c*(pw+pad); yb=pad+r*(ph+lab+pad)
    sheet.paste(Image.fromarray(np.clip(p,0,255).astype(np.uint8)).resize((pw,ph),Image.LANCZOS),(x,yb))
    d.text((x+4,yb+ph+12),CZ[i],font=font,fill=(235,235,235))
sheet.save(OUT+'navrhy.png'); print('ok')
