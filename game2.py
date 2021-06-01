import pygame
import sys
import random
import math

size = width, height = 600,750  # 设置窗口
flyv=8
flyxiao=3
flyda=20,40
flyman=2.5
bulv=20
bulv2=3
flylan=100
flylife=5
flyval=5
emenybulsize=6
flywudi=100
#7反弹
#8sanzi
class Fly(object):

    def __init__(self,id=1):
        self.sx=30
        self.sy=30
        self.py=650
        self.px=270
        self.vx=0
        self.vy=0
        self.v=flyv
        self.fire1=0
        self.fire2=0
        self.fire3=0
        self.fire4=0
        self.cd1=0
        self.cd2=0
        self.cd3=0
        self.val=0
        self.lan=flylan
        self.rect = pygame.Rect(self.px, self.py, self.sx, self.sy)
        self.san=0.2
        self.vsan=-0.02
        self.life=flylife
        self.san3=bulv
        self.wudi=0
        self.xiao=0
        self.score=-30
        self.id=id
    def fire(self):
        if moshi== 0 or moshi==3:
            if self.fire1==1:
                self.fire1=0
                if moshi==3 and self.id==2:
                    si=0
                    if len(bul3)==0:
                        bul3.append(Bul(self.px+self.sx/2,self.py,0,bulv,1,20))
                else:
                    si=0
                    if len(bul)==0:
                        bul.append(Bul(self.px+self.sx/2,self.py,0,-bulv,1,20))
            return
        if self.fire1==1:
            if self.cd1==0 and self.lan>=2:
                self.lan-=2
                if self.san<=0 or self.san>=0.3:
                    self.vsan*=-1
                self.san+=self.vsan
                bul.append(Bul(self.px+self.sx/2,self.py,0,-bulv,1,30))
                bul.append(Bul(self.px + self.sx / 2, self.py, bulv*math.sin(self.san), -bulv*math.cos(self.san),1,30))
                bul.append(Bul(self.px + self.sx / 2, self.py, -bulv*math.sin(self.san), -bulv*math.cos(self.san),1,30))
                for i in range(self.val):
                    t=random.random()*0.1
                    bul.append(Bul(self.px + self.sx / 2, self.py, bulv * math.sin(t), -bulv * math.cos(t),1,20))
                self.cd1=3
        if self.fire2==1:
            if self.cd2==0 and self.lan>=5:
                self.lan-=5
                bul.append(Bul(self.px + self.sx / 2, self.py, 0, -bulv,2))
                self.cd2=5
        if self.fire3==1:
            if self.cd3==0 and self.lan>=2:
                self.lan-=2
                t=random.random()
                if t<self.val*0.1: self.lan+=1
                self.san3*=-1
                bul.append(Bul(self.px + self.sx / 2+self.san3, self.py+self.sy/2, self.san3, 0,3,20))
                self.cd3=1
        if self.fire4==1 and self.lan>30:
            self.lan-=30
            self.fire4=0;
            for i in range(18):
                t=1/18*2*math.pi*i
                bul.append(Bul(self.px + self.sx / 2+100* math.sin(t), self.py+self.sy/2+100* math.cos(t), bulv * math.sin(t), bulv * math.cos(t),5,8))

    def update(self):
        self.wudi=max(0,self.wudi-1)
        self.cd1=max(0,self.cd1-1)
        self.cd2 = max(0, self.cd2-1)
        self.cd3 = max(0, self.cd3 - 1)
        self.px=self.px+self.vx*self.v;
        self.py=self.py+self.vy*self.v;
        self.px=max(0,self.px)
        self.px=min(width-self.sx,self.px)
        if moshi==3:
            if self.id==1:
                self.py = height-180
            else :self.py=150
        else:
            if moshi==0:
                self.py=max(600,self.py)
            else :self.py=max(0,self.py)
            self.py=min(height-self.sy,self.py)
        if self.xiao==1 and self.lan>-111:
            self.rect = pygame.Rect(self.px+self.sx/2, self.py+self.sy/2, flyxiao, flyxiao)
            self.lan-=0
            self.v=flyman
        else :
            self.rect = pygame.Rect(self.px, self.py, self.sx, self.sy)
            self.xiao=0
            self.v=flyv
        if (self.wudi/2)%2==0 or self.wudi<70 :
            if self.id==2 :screen.blit(guang2, (self.px, self.py))
            else :
                if self.xiao==1:
                    temp = pygame.Surface((30, 30)).convert()
                    temp.blit(guang, (0, 0))
                    temp.set_alpha(100)
#                    temp=pygame.transform.rotate(temp, time2)
                    screen.blit(temp, (self.px,self.py))
                    pygame.draw.rect(screen, (255, 0, 0), self.rect, 5)
                else :
                    screen.blit(guang, (self.px, self.py))

        if self.wudi>0:
            rect1=pygame.Rect(self.px+self.sx+2, self.py, self.sx/3, self.wudi/flywudi*self.sy)
            pygame.draw.rect(screen, (255, 200, 100), rect1, 0)
class Bul(object):
    def __init__(self,px,py,vx,vy,id=1,v=bulv):
        self.sx=3
        self.sy=5
        self.px=px
        self.py=py
        self.v=v
        self.id = id;
        if self.id == 4 or self.id ==6or self.id==7:
            if self.v==bulv:
                self.v = bulv2
            self.sx=emenybulsize
            self.sy=emenybulsize
        self.l=math.sqrt(vx*vx+vy*vy)
        self.vx=self.v*vx/self.l
        self.vy=self.v*vy/self.l
        self.die=0
        self.time=0
        self.rect = pygame.Rect(self.px, self.py, self.sx, self.sy)

    def up(self):
        self.time+=1
        if self.time>=600:self.die=1
        self.px+=self.vx
        self.py+=self.vy
        if self.id==3 or self.id==5:return
        if self.id==2 and self.time==20 : self.die=1
        if self.px+self.sx<0 or self.px>width :
            if self.id==7:
                self.vx*=-1
            else: self.die=1
        if self.py+self.sy<0 or self.py>height:
            if self.id==7 and self.py<0:
                self.vy*=-1
            else :self.die=1
        if self.die==1 and self.id==2:
            for i in range(8+2*fly.val):
                k=random.random()*2*math.pi
                if i<fly.val:
                    bul.append(Bul(self.px,self.py,self.vy*math.sin(k),self.vy*math.cos(k),8))
                else :bul.append(Bul(self.px, self.py, self.vy * math.sin(k), self.vy * math.cos(k),8))
    def gen(self):
        ma=1111111111
        x=0
        y=0
        for i in emeny:
            l=(i.px-self.px)*(i.px-self.px)+(i.py-self.py)*(i.py-self.py)
            if l<ma :
                x = i.px+5 - self.px
                y=i.py+5-self.py;
                ma=l
        if x==0 and y==0 :
            self.vx=0
            self.vy=0
        else :
            l=math.sqrt(x*x+y*y)
            x=self.v*x/l/2+self.vx
            y=self.v*y/l/2+self.vy
            l = math.sqrt(x * x + y * y)
            self.vx=x/l*self.v
            self.vy=y/l*self.v
    def gen2(self):
        ma = 1111111111
        x = 0
        y = 0
        for i in bul2:
            if i .id==6 :continue
            l = (i.px - self.px) * (i.px - self.px) + (i.py - self.py) * (i.py - self.py)
            if l < ma:
                x = i.px - self.px
                y = i.py - self.py;
                ma = l
        if x == 0 and y == 0:
            self.vx = 0
            self.vy = 0
        else:
            l = math.sqrt(x * x + y * y)
            self.vx = x / l * self.v
            self.vy = y / l * self.v
    def update(self):
        self.rect = pygame.Rect(self.px, self.py, self.sx, self.sy)
        if moshi!=1:
            screen.blit(zidan, (self.px, self.py))
        else :
            if self.id==4or self.id==7:
                screen.blit(z2[int(self.time/10)%4], (self.px-emenybulsize, self.py-emenybulsize))
            elif self.id == 6:
                pygame.draw.rect(screen, (255, 255, 0), self.rect, 5)
            elif self.id==1 :
                screen.blit(pz1, (self.px - 18, self.py - 25))
            else :
                screen.blit(pz[int(self.time/5)%2], (self.px-6, self.py-5))
class Enemy1(object):
    def __init__(self,px,py,die,vx=2,vy=1.5,tt=100,id=1):
        self.sx=30
        self.sy=30
        self.px=px
        self.py=py
        self.vx=vx
        self.shix=self.sx
        self.shiy=self.sy
        self.vy=vy
        self.die=die
        self.t=0
        self.tt=tt
        self.cun=0
        self.id=id
        self.rect = pygame.Rect(self.px, self.py, max(self.sx,self.die), max(self.sy,self.die))
        self.font = pygame.font.SysFont("Arial",20)
        self.jiao=0
    def up(self):
        if moshi==0 and self.vy!=0:
            x=fly.px+fly.sx-self.px-self.sx
            y=fly.py-self.py
            k=1
            if self.px>width/4*3:self.vx=-2
            if self.px<width/4:self.vx=2
            if y<100 and abs(x)<abs(y)+self.sx:
                if  (x<y+30 or x>y+30):
                    k=-1
                self.vx = abs(2) * k
            if len(bul)>0:
                x=bul[0].px-(self.px+self.sx)
                y=bul[0].py-(self.py)
                if y>0and abs(x)<50:
                    if x>0:
                        k = -1
                    self.vx=abs(2) *k

        else :
            if self.t%self.tt==0: self.vx*=-1;
        self.py+=max(0,(self.vy));
        self.px+=self.vx;
        if moshi==0:
            if self.px+self.sx>width or self.px<0 : self.vx*=-1
            if self.px+self.sx>width:self.px=width-self.sx
            if self.px<0: self.px=0
        else :
            if self.px > width or self.px+self.sx < 0: self.vx *= -1
        if self.py>height :
            if moshi==0:self.py=0
            else :self.die=0
    def fire(self):
        if self.id==7:
            if time%7==0:
                for i in range(9):
                    jiao = self.jiao
                    jiao = (jiao/6 + i * 40) % 360 / 180 * math.pi
                    bul2.append(Bul(self.px + self.shix / 2 ,
                                    self.py + self.shix / 2 ,math.cos(-jiao),
                                    math.sin(-jiao), 4))
                    bul2.append(Bul(self.px + self.shix / 2+100*math.cos(jiao),
                                    self.py + self.shix / 2+100*math.sin(jiao), math.cos(jiao+math.pi/5*3),
                                    math.sin(jiao+math.pi/5*3), 4))

            return
        if self.id==6:
            if time%180==0:
                x=random.random()*width
                y=random.random()*height/2
                for i in range(72):
                    jiao = (10 * i) / 180 * math.pi
                    bul2.append(Bul(x,
                                    y, bulv2 * math.cos(jiao),
                                    bulv2 * math.sin(jiao), 7))
            return
        if self.id==5:
            if time%4==0:
                x=fly.px-self.px
                x1=-fly.px-self.px
                x2=width*2-fly.px-self.px
                y=fly.py-self.py
                l=math.sqrt((x*x)+(y*y))
                l1 = math.sqrt((x1 * x1) + (y * y))
                l2 = math.sqrt((x2 * x2) + (y * y))
                bul2.append(Bul(self.px,self.py,x/l,y/l, 7,2*bulv2))
                bul2.append(Bul(self.px, self.py, x1 / l1, y / l1, 7,2*bulv2*l1/l))
                bul2.append(Bul(self.px, self.py, x2 / l2, y / l2, 7,2*bulv2*l2/l))
            return
        if self.id==2:
            if (int(time / 10)) % 10 < 8 and time % 4 == 0:
                for i in range(12):
                    jiao = self.jiao
                    jiao = (jiao + i * 30) % 360 / 180 * math.pi
                    bul2.append(Bul(self.px + self.shix / 2 + self.shix * math.cos(jiao),
                                    self.py + self.shix / 2 + self.shix * math.sin(jiao), bulv2 * math.cos(jiao),
                                    bulv2 * math.sin(jiao), 4))
            return
        if self.id==3:
            if (int(time / 10)) % 10 < 7and time % 4 == 0:
                for i in range(12):
                    jiao = (self.jiao+30*i)/math.pi
                    bul2.append(Bul(self.px + self.shix / 2 + self.shix * math.cos(jiao),
                                    self.py + self.shix / 2 + self.shix * math.sin(jiao), bulv2 * math.cos(jiao),
                                    bulv2 * math.sin(jiao), 4))
            return
        if self.id==4:
            if (int(time / 10)) % 10 < 10and time % 30 == 0:
                for i in range(72):
                    jiao = (5*i)/180*math.pi
                    bul2.append(Bul(self.px + self.shix / 2 + self.shix * math.cos(jiao),
                                    self.py + self.shix / 2 + self.shix * math.sin(jiao), bulv2 * math.cos(jiao),
                                    bulv2 * math.sin(jiao), 4))
            return
        if self.die<=10 : return
        if (int(time2/10))%10<3 and time2%4==0:
            for i in range(12):
                jiao=self.jiao
                jiao=(jiao+i*30)%360/180*math.pi
                bul2.append(Bul(self.px + self.shix / 2+self.shix*math.cos(jiao), self.py + self.shix/2+self.shix*math.sin(jiao), bulv2*math.cos(jiao), bulv2*math.sin(jiao), 4))
        if self.cun==0:
            t=1
            k=0;
            m=random.random()
            if m<=k : self.cun=t
        elif self.cun>0 :
            self.cun-=1
            x=fly.px-self.px
            y=fly.py-self.py
            t=random.random()
            if t>0.1 :
                x=random.random()-0.5
                y=random.random()-0.5
            l=math.sqrt(x*x+y*y)
            t=random.random()
            if t<0.1:bul2.append(Bul(self.px+self.die/2,self.py+self.die,bulv2*x/l,bulv2*y/l,6))
            else : bul2.append(Bul(self.px+self.die/2,self.py+self.die,bulv2*x/l,bulv2*y/l,4))

    def attack(self,t):
        if self.rect.colliderect(t.rect):
            return 1;
        return 0;
    def update(self):
        self.t += 1
        self.jiao += 1
        self.shix=min(max(self.sx,self.die),30)
        self.shiy = min(max(self. sy,self. die), 30)
        if self.id>1 or self.die>10 :
            self.shix=50
            self.shiy=50
        self.rect = pygame.Rect(self.px, self.py, self.shix, self.shiy)
        if moshi!=1:
            screen.blit(m2[int(time2/20)%3], (self.px, self.py))
        else :
            if self.die>10:
                #pygame.draw.rect(screen, (255, 255, 255), self.rect, 0)
                screen.blit(boss, (self.px-20, self.py-20))
                screen.blit(self.font.render(str(self.die), -1, (255, 0, 0)), (self.px+self.sx/5*2, self.py+55))
            else : screen.blit(m11, (self.px, self.py))
class Box(object):
    def __init__(self,px,py,id):
        self.sx=20
        self.sy=20
        self.px=px
        self.py=py
        self.vx=0
        self.vy=0
        self.die=0
        self.id=id
        self.t=0
        self.v=4
        self.rect = pygame.Rect(self.px, self.py, self.sx, self.sy)

    def up(self):
        if self.rect.colliderect(fly.rect) :
            self.die=1
            if self.id==1:
                fly.val=min(flyval,fly.val+1);
            if self.id==2:
                fly.life=min(flylife,fly.life+1)
        x=fly.px-self.px
        y=fly.py-self.py
        l=math.sqrt(x*x+y*y)
        x = self.v * x / l / 3 + self.vx
        y = self.v * y / l / 3 + self.vy
        l = math.sqrt(x * x + y * y)
        self.vx = x / l * self.v
        self.vy = y / l * self.v
        self.px+=self.vx
        self.py+=self.vy
    def update(self):
        self.rect = pygame.Rect(self.px, self.py, self.sx, self.sy)
        if self.id==1:
            screen.blit(huoli, (self.px-15, self.py-10))
        if self.id==2:
            screen.blit(xiebao, (self.px-15, self.py-15))
class Boom(object):
    def __init__(self, px, py):
        self.px = px
        self.py = py
        self.dan=128
        self.time=0
        self.time2=0
    def update(self):
        screen.blit(bom, (self.px, self.py))
        self.time+=1

def checkbul():
    de=[]
    for i in bul:
        if i.id==3: i.gen()
        if i.id==5: i.gen2()
        i.up()
        if i.die==1:de.append(i)
    for i in de:
        bul.remove(i)
    de.clear()
    if moshi==3:
        for i in bul3:
            i.up()
            if i.rect.colliderect(fly.rect):de.append(i)
            elif i.die == 1: de.append(i)
        for i in de:
            bul3.remove(i)
        de.clear()
        for i in bul:
            if i.rect.colliderect(fly2.rect):de.append(i)
            elif i.die == 1: de.append(i)
        for i in de:
            bul.remove(i)
        de.clear()

    for i in bul2:
        i.up()
        if i.die == 1: de.append(i)
    for i in de:
        bul2.remove(i)
    de.clear()
    for i in bul:
        for j in bul2:
            if i.id==5 and i.rect.colliderect(j.rect):
                bul2.remove(j);
                de.append(i)
                break;
    for i in de:
        bul.remove(i);
    de.clear()
    if fly.wudi==0:
        for i in bul2:
            if fly.rect.colliderect(i.rect):
                fly.wudi=flywudi
                fly.life-=1
                bul2.remove(i)
                break;
def checkemeny():
    de = []
    for i in emeny:
        i.up()
        if i.die == 0: de.append(i)
    for i in de:
        emeny.remove(i)
    de.clear()
    for i in emeny:
        db=[]
        for j in bul:
            if i.attack(j)==1:
                i.die-=1
                db.append(j);
                j.die=1
                j.up()
                if i.die==0 :
                    de.append(i);
                    break;
        for j in db: bul.remove(j);
        db.clear()
    for i in de:
        boom.append(Boom(i.px,i.py))
        emeny.remove(i);
        fly.score+=1
        if moshi==0 and len(emeny)>0:
            k=random.randint(0,len(emeny)-1)
            kk=emeny[k]
            emeny.remove(kk)
            emeny.append(Enemy1(kk.px,kk.py, 1, 2,2));
        t=random.random()
        if moshi==1:
            if t>0.9 and fly.val<5:
                box.append(Box(i.px,i.py,1));
            t = random.random()
            if t > 0.7+fly.life*0.06:
                box.append(Box(i.px, i.py, 2));
    de.clear()
    if moshi==3:
        for i in emeny:
            db=[]
            for j in bul3:
                if i.attack(j)==1:
                    i.die-=1
                    db.append(j);
                    j.die=1
                    j.up()
                    if i.die==0 :
                        de.append(i);
                        break;
            for j in db: bul3.remove(j);
            db.clear()
        for i in de:
            emeny.remove(i);
            fly2.score+=1
        de.clear()
    for i in emeny:
        i.fire()
        if fly.wudi==0:
            if i.attack(fly):
                fly.wudi=flywudi;
                fly.life-=1
def checkbox():
    de=[]
    for i in box:
        i.up()
        if i.die==1:de.append(i)
    for i in de:
        box.remove(i);
    de.clear()
def checkboom():
    de=[]
    for i in boom:
        if i.time==10:
            de.append(i)
    for i in de:
        boom.remove(i)
    de.clear()
def createMap():
    screen.fill((0, 0, 0))
    screen.blit(heise, (0, 0))
    checkbul()
    checkemeny()
    checkbox()
    checkboom()
    fly.fire()
    fly.update()
    if moshi==3:
        fly2.update()
        fly2.fire()
        for i in bul3: i.update()
    for i in bul: i.update();
    for i in box:i.update()
    for i in bul2:i.update()
    for i in boom:i.update()
    for i in emeny: i.update()
    si=0
    for i in emeny:si+=1
    #screen.blit(font.render('emeny:'+str(si), -1, (0, 255, 250)), (100, 100))
    if moshi!=3:
        rect = pygame.Rect(80, 50, 100,20)
        rect2=pygame.Rect(80, 50, fly.lan/flylan*100,20)
        rect3 = pygame.Rect(80, 20, 100, 20)
        rect4 = pygame.Rect(80, 20, fly.life / flylife * 100, 20)
        pygame.draw.rect(screen, (255, 0, 0), rect3, 2)
        pygame.draw.rect(screen, (255, 0, 0), rect4, 0)
        if moshi==1:pygame.draw.rect(screen, (0, 255, 255),rect, 2)
        if moshi==1:pygame.draw.rect(screen, (0, 255, 255), rect2,0)
        if moshi==1:screen.blit(font.render('power:', -1, (0, 255, 250)), (0, 45))
        screen.blit(font.render('life:', -1, (255, 0, 0)), (0, 15))
        if moshi==1:screen.blit(font.render('val:' + str(fly.val), -1, (0, 255, 250)), (0, 73))
        if moshi==0:screen.blit(font.render('score:' + str(fly.score+30), -1, (0, 255, 250)), (0, 100))
        if moshi==1:screen.blit(font.render('score:' + str(fly.score), -1, (0, 255, 250)), (0, 100))
    screen.blit(font.render('time:' + str(int(time2/60)), -1, (0, 255, 250)), (0, 140))
    screen.blit(font.render('time:' + str(int(time2/60)), -1, (0, 255, 250)), (0, 140))

    pygame.display.update()  # 更新显示
def init(id=1):
    global time
    global time3
    global sumt
    sumt=0
    time=0
    time3+=1
    if id==2:
        de=[]
        for i in bul2:
            de.append(i)
        for i in de:
            bul2.remove(i)
        de.clear()
def level_1():
    global time3
    global time
    global sumt

    if time3==-1:ha.append(11)#1 da
    elif ha[time3]==11:
        if time==1:
            emeny.append(Enemy1(width/2, 200, 20, 0, 0, 100,7));
        if len(emeny)==0: init()
    if time3 == -1: ha.append(10)#80 san
    elif ha[time3]==10:
        for i in range(40):
            if time==i*2:
                sumt+=2
                k=random.random()*width
                emeny.append(Enemy1(k, 0, 2, 0,4,1000));
        if time==sumt+60:init()
    if time3 == -1: ha.append(2)#40 xie
    elif ha[time3]==2:
        for i in range(20):
            if time==i*20:
                sumt+=20
                emeny.append(Enemy1(0, 0, 5, 2,2,1000));
                emeny.append(Enemy1(width, 0, 5, -2,2,1000));
                emeny.append(Enemy1(100, 0, 5, 2, 2, 1000));
                emeny.append(Enemy1(width-100, 0, 5, -2, 2, 1000));
        if time==sumt+60:init()
    if time3==-1:ha.append(1)#30 kuai
    elif ha[time3]==1:
        for i in range(5):
            if time==i*30:
                sumt+=30
                for j in range(10):
                    emeny.append(Enemy1(width/10*j, 0, 2,0, 8, 1000));
        if time==sumt+60:init()
    if time3==-1:ha.append(3)#40 cha
    elif ha[time3]==3:
        for i in range(30):
            if time ==i*10:
                sumt+=10
                emeny.append(Enemy1(width/10*i, 0, 3, 0, 4, 1000));
                emeny.append(Enemy1(width-width / 10 * i, 0, 3, 0, 4, 1000));
                emeny.append(Enemy1(0, 0, 5, 2, 2, 1000));
                emeny.append(Enemy1(width, 0, 5, -2, 2, 1000));
                emeny.append(Enemy1(width /2, 0, 3, 0, 4, 1000));
        if time==sumt+60:init()
    if time3==-1:ha.append(4)#1 da
    elif ha[time3]==4:
        if time==10:
            emeny.append(Enemy1(width /2, 0, 200, 2, 0, 100));
        if time ==60: init()
    if time3==-1:ha.append(5)#40  xie
    elif ha[time3]==5:
        for i in range(20):
            if time==i*20:
                sumt+=20
                emeny.append(Enemy1(0, 0, 5, 5,3,1000));
                emeny.append(Enemy1(width, 0, 5, -5,3,1000));
        if time==sumt+60:init()
    if time3==-1:ha.append(7)#50 kuai xie
    elif ha[time3]==7:
        for i in range(5):
            if time==i*30:
                sumt+=30
                for j in range(10):
                    k=5
                    if j%2==0:k*=-1;
                    emeny.append(Enemy1(width/10*j, 0, 4,k, 10, 1000));
        if time==sumt+60:init()
    if time3==-1:ha.append(8)#1 da
    elif ha[time3]==8:
        if time==10:
            emeny.append(Enemy1(width /2, 10, 500, 2, 0, 100,2));
        if time ==60: init()
    if time3 == -1: ha.append(9)#60 san
    elif ha[time3]==9:
        for i in range(100):
            if time==i*2:
                sumt+=2
                k=random.random()*width
                emeny.append(Enemy1(k, 0, 4, 0,7,1000));
        if len(emeny)==0:init(2)
    if time3==-1:ha.append(12)#boss
    elif ha[time3]==12:
        if time<=0:
            emeny.append(Enemy1(width/3, 200, 100, 0, 0, 100,4));
            emeny.append(Enemy1(width/3*2, 200,100, 0, 0, 100, 4));
        if len(emeny)==0: init(2)
    if time3 == -1: ha.append(10)  # 80 san
    if time3 == -1: ha.append(7)  # 50 kuai xie
    if time3==-1:ha.append(13)#boss
    elif ha[time3]==13:
        if time<=0:
            emeny.append(Enemy1(width/2, 200, 600, 0, 0, 100,2));
        if len(emeny)==0: init(2)
    if time3 == -1: ha.append(2)#40 xie
    if time3==-1:ha.append(14)#boss
    elif ha[time3]==14:
        if time<=0:
            emeny.append(Enemy1(width/2, 200, 300, 0, 0, 100,5));
        if len(emeny)==0: init(2)
    if time3 == -1: ha.append(9)  # 60 san
    if time3==-1:ha.append(15)#boss
    elif ha[time3]==15:
        if time<=0:
            emeny.append(Enemy1(width/3, 200, 100, 0, 0, 100,3));
            emeny.append(Enemy1(width / 3*2, 200, 100, 0, 0, 100, 4));
        if len(emeny)==0: init(2)
    if time3 == -1: ha.append(2)  # 40 xie
    if time3==-1:ha.append(16)#boss
    elif ha[time3]==16:
        if time<=0:
            emeny.append(Enemy1(width/2, 200, 600, 0, 0, 100,6));
        if len(emeny)==0: init(2)
    if time3 == -1: ha.append(9)#60 san
    if time3==-1:ha.append(17)#boss
    elif ha[time3]==17:
        if time<=0:
            emeny.append(Enemy1(width/2, 200, 600, 0, 0, 100,7));
        if len(emeny)==0: init(2)
    if time3 == -1:ha.append(6)#5 da
    elif ha[time3] == 6:
        for i in range(5):
            if time == i*300:
                sumt+=300
                emeny.append(Enemy1(width / 2, 30, 150, 2, 0, 100));
        if time%20==0:
            emeny.append(Enemy1(0, 0, 5, 5, 2, 1000));
            emeny.append(Enemy1(width, 0, 5, -5, 2, 1000));
        if time == sumt+300: init()
    print(ha[time3])
    if time3==-1:ha.append(-1)
    if ha[time3]==-1 and time2>100:
        ha[time3]=random.randint(1,17)
        ha.append(-1)

if __name__ == '__main__':

    pygame.init()
    pygame.mixer.init()
    boom=[]
    fly=Fly()
    bul=[]
    ha=[]
    bul2=[]
    bul3=[]
    emeny=[]
    box=[]
    font = pygame.font.SysFont("SimHei", 30)
    screen = pygame.display.set_mode(size)  # 显示窗口
    clock = pygame.time.Clock()  # 初始化pygame
    time2=0
    time3=-1
    sumt=0
    time=0
    ting=1
    moshi=0

    if ting==1:
        daodan = pygame.transform.smoothscale(pygame.image.load("image/daodan.png"), (31, 10))
        huoli = pygame.transform.smoothscale(pygame.image.load("image/huoli.png"), (50, 40))
        xiebao = pygame.transform.smoothscale(pygame.image.load("image/xiebao.png"), (50, 50))
        pz1 = pygame.transform.smoothscale(pygame.image.load("image/zidan1.png"), (39, 55))
        pz2 = pygame.transform.smoothscale(pygame.image.load("image/player_zidan2.png"),(15, 15))
        pz3 = pygame.transform.smoothscale(pygame.image.load("image/player_zidan3.png"), (15, 15))
        pz=[]
        pz.append(pz2)
        pz.append(pz3)
        boss = pygame.transform.smoothscale(pygame.image.load("image/boss1_1.png"),(90, 90))
        z21 = pygame.transform.smoothscale(pygame.image.load("image/zidan2_1.png"), (3*emenybulsize, 3*emenybulsize))
        z22 = pygame.transform.smoothscale(pygame.image.load("image/zidan2_2.png"), (3*emenybulsize, 3*emenybulsize))
        z23 = pygame.transform.smoothscale(pygame.image.load("image/zidan2_3.png"), (3*emenybulsize, 3*emenybulsize))
        z24 = pygame.transform.smoothscale(pygame.image.load("image/zidan2_4.png"), (3*emenybulsize, 3*emenybulsize))
        z2 = []
        z2.append(z21)
        z2.append(z22)
        z2.append(z23)
        z2.append(z24)
        m11 = pygame.transform.smoothscale(pygame.image.load("image/m1.png"), (30, 30))
        bom = pygame.transform.smoothscale(pygame.image.load("image/boom.png"), (30,30 ))
        m21 = pygame.transform.smoothscale(pygame.image.load("image/m2_1.png"), (30, 30))
        m22 = pygame.transform.smoothscale(pygame.image.load("image/m2_2.png"), (30, 30))
        m23 = pygame.transform.smoothscale(pygame.image.load("image/m2_3.png"), (30, 30))
        m2 = []
        m2.append(m21)
        m2.append(m22)
        m2.append(m23)
        zidan = pygame.transform.smoothscale(pygame.image.load("image/zidan.png"), (5, 11))
        guang = pygame.image.load("image/player.png")
        guang = pygame.transform.smoothscale(guang, (30, 30))
        guang.set_colorkey((255, 255, 255))
        guang2 = pygame.transform.smoothscale(pygame.image.load("image/player2.png"), (30, 30))
        xingkong = pygame.image.load("image/xingkong.jpeg")
        xingkong = pygame.transform.smoothscale(xingkong, (width, height))
        heise = pygame.image.load("image/ditu.jpg")
        heise = pygame.transform.smoothscale(heise, (width, height))
        flytu = pygame.transform.smoothscale(pygame.image.load("image/heise.jpeg"), (width, height))


    while True:
        clock.tick(60)
        screen.blit(xingkong, (0, 0))
        img = pygame.image.load("image/xx.png")
        img = pygame.transform.smoothscale(img, (400, 150))
        screen.blit(img, (100, 120))
        # screen.fill((100, 100, 100))
        fl=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit()
            if event.type == pygame.KEYUP :
                if event.key ==pygame.K_j :
                    fl=1
                if event.key == pygame.K_w:
                    if moshi==1: moshi=0
                    if moshi==3 : moshi=1
                if event.key == pygame.K_s:
                    if moshi==1:moshi=3
                    if moshi==0: moshi=1
        rect1 = pygame.Rect(210, 355, 20, 20)
        rect2 = pygame.Rect(210, 425, 20, 20)
        rect3 = pygame.Rect(210, 495, 20, 20)

        if moshi==0:screen.blit(guang, (200, 355))
        if moshi==1:screen.blit(guang, (200, 425))
        if moshi==3:screen.blit(guang, (200, 495))
        # jingdian = pygame.image.load("image/经典模式.png")
        # jingdian = pygame.transform.smoothscale(jingdian, (100, 50))
        screen.blit(font.render(" 经典模式 ", -1, (255, 255, 250)), (240, 350))
        screen.blit(font.render(' 狂暴模式 ', -1, (255, 255, 250)), (240, 420))
        screen.blit(font.render(' 对战模式 ', -1, (255, 255, 250)), (240, 490))
        # screen.blit(font.render(' Made by python_4 ', -1, (255, 255, 250)), (350, 600))
        # screen.blit(font.render('en j kai shi you xi', -1, (255, 255, 250)), (100, 380))
        si = pygame.image.load("image/四组.png")
        si = pygame.transform.smoothscale(si, (200, 50))
        screen.blit(si, (320, 550))
        pygame.display.update()  # 更新显示
        if fl==1 : break;

    if moshi==3:fly2=Fly(2)
    if moshi==0:

        for i in range(3):
            for j in range(10):
                emeny.append(Enemy1(20+j*50, 10+i*35, 1, -1,0));
        fly.score = -30
        source_path = u'yinyue1.mp3'.encode('utf-8')
        pygame.mixer.music.load(source_path)
        pygame.mixer.music.play(-1, 0)
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        fly.vx -= 1
                    if event.key == pygame.K_d:
                        fly.vx += 1
                    if event.key == pygame.K_w:
                        fly.vy -= 1
                    if event.key == pygame.K_s:
                        fly.vy += 1
                    if event.key == pygame.K_j:
                        fly.fire1 = 1
                    if event.key == pygame.K_k:
                        fly.fire2 = 1
                    if event.key == pygame.K_l:
                        fly.fire3 = 1
                    if event.key == pygame.K_SPACE:
                        fly.xiao = 1
                    if event.key == pygame.K_h:
                        fly.fire4 = 1
                    if event.key == pygame.K_p:
                        ting *= -1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        fly.vx += 1
                    if event.key == pygame.K_d:
                        fly.vx -= 1
                    if event.key == pygame.K_w:
                        fly.vy += 1
                    if event.key == pygame.K_s:
                        fly.vy -= 1
                    if event.key == pygame.K_j:
                        fly.fire1 = 0
                    if event.key == pygame.K_k:
                        fly.fire2 = 0
                    if event.key == pygame.K_l:
                        fly.fire3 = 0
                    if event.key == pygame.K_SPACE:
                        fly.xiao = 0
                    if event.key == pygame.K_h:
                        fly.fire4 = 0
            if ting == -1: continue;
            if fly.score==0:
                ting *= -1;
                screen.blit(font.render('press p to be continue', -1, (255, 255, 250)), (200, 300))
                pygame.display.update()  # 更新显示
                fly.score=1
                continue
            if fly.life == 0:
                ting *= -1;
                xingkong = pygame.image.load("image/xingkong.jpeg")
                xingkong = pygame.transform.smoothscale(xingkong, (width, height))
                screen.blit(xingkong, (0, 0))
                screen.blit(font.render("GAME OVER", -1, (255, 255, 250)), (200, 300))
                screen.blit(font.render("最后成绩", -1, (255, 255, 250)), (200, 350))
                screen.blit(font.render('score:' + str(fly.score + 30), -1, (255, 255, 250)), (200, 400))
                screen.blit(font.render('time:' + str(int(time2 / 60)), -1, (255, 255, 250)), (200, 450))
                pygame.display.update()  # 更新显示
                fly.life = 5
                continue
            time2 += 1
            time += 1
            if time >= 100 and fly.score >= 0:
                time = 0
                for i in range(1):
                    tx = random.random() * 600
                    ty = random.random() * 100
                    life = random.randint(5, 20)
                    k = random.randint(1, 2);
                    if k == 1: k = -2
                    if k == 2: k = 2
                    emeny.append(Enemy1(tx, ty, 1, k));

            fly.lan = min(flylan, fly.lan + 1)
            createMap()
    if moshi==1:
        fly.score=0
        while True:
            clock.tick(60)
            # screen.fill((0, 0, 0))
            xingkong = pygame.image.load("image/xingkong.jpeg")
            xingkong = pygame.transform.smoothscale(xingkong, (width, height))
            screen.blit(xingkong, (0, 0))
            img = pygame.image.load("image/anjian.png")
            img = pygame.transform.smoothscale(img, (400, 150))
            screen.blit(img, (100, 120))
            fl = 0
            screen.blit(font.render('左上角血条 以及 蓝条', -1, (255, 0, 0)), (160, 320))
            screen.blit(font.render('空格 判定点缩小，速度变慢', -1, (255, 0, 0)), (160, 360))
            screen.blit(font.render('j 普通子弹', -1, (255, 0, 0)), (160, 400))
            screen.blit(font.render('k 爆裂子弹', -1, (255, 0, 0)), (160, 440))
            screen.blit(font.render('l 跟踪子弹', -1, (255, 0, 0)), (160, 480))
            screen.blit(font.render('h 拦截子弹', -1, (255, 0, 0)), (160, 520))
            rect1 = pygame.Rect(130, 570, 20, 20)
            rect2 = pygame.Rect(130, 610, 20, 20)
            screen.blit(huoli, (130 - 15, 570 - 10))
            screen.blit(xiebao, (130 - 15, 610 - 15))
            #pygame.draw.rect(screen, (255, 50, 100), rect1, 0)
            #pygame.draw.rect(screen, (255, 0, 0), rect2, 0)
            screen.blit(font.render(' 增强火力 ', -1, (255, 0, 0)), (160, 560))
            screen.blit(font.render(' 血包 ', -1, (255, 0, 0)), (160, 600))
            # screen.blit(font.render('en j kai shi you xi', -1, (255, 255, 250)), (100, 350))

            pygame.display.update()  # 更新显示
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_j:
                        fl = 1
            if fl == 1: break;
        source_path = u'yinyue2.mp3'.encode('utf-8')
        pygame.mixer.music.load(source_path)
        pygame.mixer.music.play(-1, 0)
        level_1();
        init()
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    sys.exit()
                if event.type == pygame.KEYDOWN  :
                    if event.key ==pygame.K_a :
                        fly.vx-=1
                    if event.key ==pygame.K_d :
                        fly.vx+=1
                    if event.key ==pygame.K_w :
                        fly.vy-=1
                    if event.key == pygame.K_s:
                        fly.vy+=1
                    if event.key == pygame.K_j:
                        fly.fire1=1
                    if event.key == pygame.K_k:
                        fly.fire2=1
                    if event.key == pygame.K_l:
                        fly.fire3 = 1
                    if event.key == pygame.K_SPACE:
                        fly.xiao=1
                    if event.key == pygame.K_h:
                        fly.fire4=1
                    if event.key == pygame.K_p:
                        ting*=-1
                if event.type == pygame.KEYUP :
                    if event.key ==pygame.K_a :
                        fly.vx+=1
                    if event.key ==pygame.K_d :
                        fly.vx-=1
                    if event.key ==pygame.K_w :
                        fly.vy+=1
                    if event.key == pygame.K_s:
                        fly.vy-=1
                    if event.key == pygame.K_j:
                        fly.fire1=0
                    if event.key == pygame.K_k:
                        fly.fire2=0
                    if event.key == pygame.K_l:
                        fly.fire3 = 0
                    if event.key == pygame.K_SPACE:
                        fly.xiao=0
                    if event.key == pygame.K_h:
                        fly.fire4=0
            if ting==-1 : continue;
            if fly.life == 0:
                ting *= -1;
                xingkong = pygame.image.load("image/xingkong.jpeg")
                xingkong = pygame.transform.smoothscale(xingkong, (width, height))
                screen.blit(xingkong, (0, 0))
                screen.blit(font.render("GAME OVER", -1, (255, 255, 250)), (200, 300))
                screen.blit(font.render("最后成绩", -1, (255, 255, 250)), (200, 350))
                screen.blit(font.render('score:' + str(fly.score), -1, (255, 255, 250)), (200, 400))
                screen.blit(font.render('time:' + str(int(time2 / 60)), -1, (255, 255, 250)), (200, 450))
                pygame.display.update()  # 更新显示
                fly.life = 5
                continue
            time2+=1
            time += 1
            level_1()
            if time < -100 and fly.score>=0:
                time = 0
                for i in range(10):
                    tx = random.random() * 600
                    ty = random.random() * 100
                    life = random.randint(5, 20)
                    k = random.randint(1, 2);
                    if k == 1: k = -2
                    if k == 2: k = 2
                    emeny.append(Enemy1(tx, ty,int(life/5), k));

            fly.lan = min(flylan, fly.lan + 1)
            createMap()
    if moshi==3:
        while True:
            clock.tick(60)
            # screen.fill((0, 0, 0))
            xingkong = pygame.image.load("image/xingkong.jpeg")
            xingkong = pygame.transform.smoothscale(xingkong, (width, height))
            screen.blit(xingkong, (0, 0))
            img = pygame.image.load("image/anjian.png")
            img = pygame.transform.smoothscale(img, (400, 150))
            screen.blit(img, (100, 120))
            fl = 0
            screen.blit(font.render('player1 a 左移', -1, (255, 250, 0)), (100, 400))
            screen.blit(font.render('        d 右移', -1, (255, 250, 0)), (100, 440))
            screen.blit(font.render('        f 发射子弹', -1, (255, 250, 0)), (100, 480))
            screen.blit(font.render('player2 <- 左移 ', -1, (255, 250, 0)), (100, 550))
            screen.blit(font.render('        -> 右移', -1, (255, 250, 0)), (100, 590))
            screen.blit(font.render('        right_ctrl 发射子弹', -1, (255, 250, 0)), (100, 630))
            # screen.blit(font.render('en j kai shi you xi', -1, (255, 255, 250)), (100, 350))

            pygame.display.update()  # 更新显示
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_j:
                        fl = 1
            if fl == 1: break;
        source_path = u'yinyue3.mp3'.encode('utf-8')
        pygame.mixer.music.load(source_path)
        pygame.mixer.music.play(-1, 0)
        for i in range(3):
            for j in range(10):
                emeny.append(Enemy1(20 + j * 50, 10 + i * 35, 1, -1, 0,100));
                emeny.append(Enemy1(20 + j * 50, height-30-(10 + i * 35), 1, -1, 0,100));
        fly.score = -30
        fly2.score=-30
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        fly.vx -= 1
                    if event.key == pygame.K_d:
                        fly.vx += 1
                    if event.key == pygame.K_w:
                        fly.vy -= 1
                    if event.key == pygame.K_s:
                        fly.vy += 1
                    if event.key == pygame.K_f:
                        fly.fire1 = 1
                    if event.key == pygame.K_p:
                        ting *= -1
                    if event.key == pygame.K_LEFT:
                        fly2.vx -= 1
                    if event.key == pygame.K_RIGHT:
                        fly2.vx += 1
                    if event.key == pygame.K_RCTRL:
                        fly2.fire1 = 1
                    if event.key == pygame.K_p:
                        ting *= -1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        fly.vx += 1
                    if event.key == pygame.K_d:
                        fly.vx -= 1
                    if event.key == pygame.K_w:
                        fly.vy += 1
                    if event.key == pygame.K_s:
                        fly.vy -= 1
                    if event.key == pygame.K_f:
                        fly.fire1 = 0
                    if event.key == pygame.K_LEFT:
                        fly2.vx += 1
                    if event.key == pygame.K_RIGHT:
                        fly2.vx -= 1
                    if event.key == pygame.K_RCTRL:
                        fly2.fire1 = 0
            if ting == -1: continue;
            if fly.score == 0 or fly2.score==0:
                ting *= -1;
                if fly.score==0:
                    screen.blit(font.render('player1 win!', -1, (255, 255, 250)), (200, 300))
                else :
                    screen.blit(font.render('player2 win!', -1, (255, 255, 250)), (200, 300))

                pygame.display.update()  # 更新显示
                fly.score = 1
                continue
            time2 += 1
            fly.lan = min(flylan, fly.lan + 1)
            createMap()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(font.render('Game Over', -1, (0, 0, 0)), (300, 300))
        pygame.display.update()  # 更新显示
    pygame.quit()
