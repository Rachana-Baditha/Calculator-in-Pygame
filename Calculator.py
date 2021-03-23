import pygame

pygame.init()

wn = pygame.display.set_mode((300,450))
pygame.display.set_caption("Calculator")

class button:
    
    def __init__(self,text,bcolor,tcolor,x,y,height,width):
        self.bcol = bcolor
        self.x = x
        self.y = y
        self.h = height
        self.w = width
        self.tcol = tcolor
        
        self.size = 24
        self.font = pygame.font.SysFont("verdana",self.size)
        self.txt = self.font.render(text,True,self.tcol)
        
        self.tw = self.txt.get_width()
        self.th = self.txt.get_height()
        

def drawCalci():
    
    global math
    on_screen = ""
    
    pygame.draw.rect(wn, (135, 140, 148), (0, 0, 300, 450)) 
    
    #Screen
    if len(math) == 1:
        on_screen = "{}".format(math[0])
    elif len(math) == 2:
        on_screen = "{} {}".format(math[0],math[1])
    elif len(math) == 3:
        on_screen = "{} {} {}".format(math[0], math[1], math[2])
    
    screen.txt = screen.font.render(on_screen,True,screen.tcol)
    screen.tw = screen.txt.get_width()
    screen.th = screen.txt.get_height()
        
    pygame.draw.rect(wn, screen.bcol, (screen.x, screen.y, screen.w, screen.h))
    
    if len(math) > 0:
        wn.blit(screen.txt,(screen.w - screen.tw, screen.h - screen.th))
    

    #Number Buttons
    pygame.draw.rect(wn, b0.bcol, (b0.x,b0.y,b0.w,b0.h))
    pygame.draw.rect(wn, b1.bcol, (b1.x,b1.y,b1.w,b1.h))
    pygame.draw.rect(wn, b2.bcol, (b2.x,b2.y,b2.w,b2.h))
    pygame.draw.rect(wn, b3.bcol, (b3.x,b3.y,b3.w,b3.h))
    pygame.draw.rect(wn, b4.bcol, (b4.x,b4.y,b4.w,b4.h))
    pygame.draw.rect(wn, b5.bcol, (b5.x,b5.y,b5.w,b5.h))
    pygame.draw.rect(wn, b6.bcol, (b6.x,b6.y,b6.w,b6.h))
    pygame.draw.rect(wn, b7.bcol, (b7.x,b7.y,b7.w,b7.h))
    pygame.draw.rect(wn, b8.bcol, (b8.x,b8.y,b8.w,b8.h))
    pygame.draw.rect(wn, b9.bcol, (b9.x,b9.y,b9.w,b9.h))
    pygame.draw.rect(wn, bdec.bcol, (bdec.x,bdec.y,bdec.w,bdec.h))
    
    wn.blit(b0.txt, (b0.x + (b0.w - b0.tw)//2 , b0.y + (b0.h - b0.th)//2 ))
    wn.blit(b1.txt, (b1.x + (b1.w - b1.tw)//2 , b1.y + (b1.h - b1.th)//2 ))
    wn.blit(b2.txt, (b2.x + (b2.w - b2.tw)//2 , b2.y + (b2.h - b2.th)//2 ))
    wn.blit(b3.txt, (b3.x + (b3.w - b3.tw)//2 , b3.y + (b3.h - b3.th)//2 ))
    wn.blit(b4.txt, (b4.x + (b4.w - b4.tw)//2 , b4.y + (b4.h - b4.th)//2 ))
    wn.blit(b5.txt, (b5.x + (b5.w - b5.tw)//2 , b5.y + (b5.h - b5.th)//2 ))
    wn.blit(b6.txt, (b6.x + (b6.w - b6.tw)//2 , b6.y + (b6.h - b6.th)//2 ))
    wn.blit(b7.txt, (b7.x + (b7.w - b7.tw)//2 , b7.y + (b7.h - b7.th)//2 ))
    wn.blit(b8.txt, (b8.x + (b8.w - b8.tw)//2 , b8.y + (b8.h - b8.th)//2 ))
    wn.blit(b9.txt, (b9.x + (b9.w - b9.tw)//2 , b9.y + (b9.h - b9.th)//2 ))
    wn.blit(bdec.txt, (bdec.x + (bdec.w - bdec.tw)//2 , bdec.y + (bdec.h - bdec.th)//2 ))
    
    
    #Math Operators
    
    pygame.draw.rect(wn, badd.bcol, (badd.x,badd.y,badd.w,badd.h))
    pygame.draw.rect(wn, bsub.bcol, (bsub.x,bsub.y,bsub.w,bsub.h))
    pygame.draw.rect(wn, bmul.bcol, (bmul.x,bmul.y,bmul.w,bmul.h))
    pygame.draw.rect(wn, bdiv.bcol, (bdiv.x,bdiv.y,bdiv.w,bdiv.h))
    
    wn.blit(badd.txt, (badd.x + (badd.w - badd.tw)//2 , badd.y + (badd.h - badd.th)//2 ))
    wn.blit(bsub.txt, (bsub.x + (bsub.w - bsub.tw)//2 , bsub.y + (bsub.h - bsub.th)//2 ))
    wn.blit(bmul.txt, (bmul.x + (bmul.w - bmul.tw)//2 , bmul.y + (bmul.h - bmul.th)//2 ))
    wn.blit(bdiv.txt, (bdiv.x + (bdiv.w - bdiv.tw)//2 , bdiv.y + (bdiv.h - bdiv.th)//2 ))
    
    #Other Buttons
    
    pygame.draw.rect(wn, bpow.bcol, (bpow.x,bpow.y,bpow.w,bpow.h))
    pygame.draw.rect(wn, bclr.bcol, (bclr.x,bclr.y,bclr.w,bclr.h))
    pygame.draw.rect(wn, beq.bcol, (beq.x,beq.y,beq.w,beq.h))
    
    wn.blit(bpow.txt, (bpow.x + (bpow.w - bpow.tw)//2 , bpow.y + (bpow.h - bpow.th)//2 ))
    wn.blit(bclr.txt, (bclr.x + (bclr.w - bclr.tw)//2 , bclr.y + (bclr.h - bclr.th)//2 ))
    wn.blit(beq.txt, (beq.x + (beq.w - beq.tw)//2 , beq.y + (beq.h - beq.th)//2 ))

        
    pygame.display.update()

def checkclick(click, m_x, m_y):
    
    global math
    global count
    global power
    global flag
    
    res = 0
    #DONT FORGET TO IMPLEMENT DECIMAL CHECKER!!!
        
    if flag == 1:
        math.append(0)
        flag = 0
        
    #Power Button
    if (m_x > bpow.x and m_x < bpow.x + bpow.w) and (m_y > bpow.y and m_y < bpow.y + bpow.h):
        if power == True:
            power = False
        else:
            power = True
         
    #Clear Button
    elif (m_x > bclr.x and m_x < bclr.x + bclr.w) and (m_y > bclr.y and m_y < bclr.y + bclr.h):
        math.clear()
        flag = 1
        count = 0
            
    #Number Buttons (0-9)
    elif (m_x > b0.x and m_x < b0.x + b0.w) and (m_y > b0.y and m_y < b0.y + b0.h):  #Button 0
        math[count]*=10
        math[count]+=0
        
    elif (m_x > b1.x and m_x < b1.x + b1.w) and (m_y > b1.y and m_y < b1.y + b1.h):  #Button 1
        math[count]*=10
        math[count]+=1
        
    elif (m_x > b2.x and m_x < b2.x + b2.w) and (m_y > b2.y and m_y < b2.y + b2.h):  #Button 2
        math[count]*=10
        math[count]+=2
        
    elif (m_x > b3.x and m_x < b3.x + b3.w) and (m_y > b3.y and m_y < b3.y + b3.h):  #Button 3
        math[count]*=10
        math[count]+=3
        
    elif (m_x > b4.x and m_x < b4.x + b4.w) and (m_y > b4.y and m_y < b4.y + b4.h):  #Button 4
        math[count]*=10
        math[count]+=4
        
    elif (m_x > b5.x and m_x < b5.x + b5.w) and (m_y > b5.y and m_y < b5.y + b5.h):  #Button 5
        math[count]*=10
        math[count]+=5
        
    elif (m_x > b6.x and m_x < b6.x + b6.w) and (m_y > b6.y and m_y < b6.y + b6.h):  #Button 6
        math[count]*=10
        math[count]+=6
        
    elif (m_x > b7.x and m_x < b7.x + b7.w) and (m_y > b7.y and m_y < b7.y + b7.h):  #Button 7
        math[count]*=10
        math[count]+=7
        
    elif (m_x > b8.x and m_x < b8.x + b8.w) and (m_y > b8.y and m_y < b8.y + b8.h):  #Button 8
        math[count]*=10
        math[count]+=8
        
    elif (m_x > b9.x and m_x < b9.x + b9.w) and (m_y > b9.y and m_y < b9.y + b9.h):  #Button 9
        math[count]*=10
        math[count]+=9
        
    elif (m_x > bdec.x and m_x < bdec.x + bdec.w) and (m_y > bdec.y and m_y < bdec.y + bdec.h) and count==0:  #Button .
        pass  #INSERT LOGIC LATER
    
    #Operator Buttons
    elif (m_x > badd.x and m_x < badd.x + badd.w) and (m_y > badd.y and m_y < badd.y + badd.h) and count==0:  #Button +
        count+=1
        math.append("+")
        count+=1
        flag = 1
    
    elif (m_x > bsub.x and m_x < bsub.x + bsub.w) and (m_y > bsub.y and m_y < bsub.y + bsub.h) and count==0:  #Button -
        count+=1
        math.append("-")
        count+=1
        flag = 1
        
    elif (m_x > bmul.x and m_x < bmul.x + bmul.w) and (m_y > bmul.y and m_y < bmul.y + bmul.h) and count==0:  #Button *
        count+=1
        math.append("*")
        count+=1
        flag = 1
    
    elif (m_x > bdiv.x and m_x < bdiv.x + bdiv.w) and (m_y > bdiv.y and m_y < bdiv.y + bdiv.h) and count==0:  #Button /
        count+=1
        math.append("/")
        count+=1
        flag = 1
        
    elif (m_x > beq.x and m_x < beq.x + beq.w) and (m_y > beq.y and m_y < beq.y + beq.h) and count == 2:  #Button =
        
        if math[1] == '+':
            res = math[0] + math[2]
        elif math[1] == '-':
            res = math[0] - math[2]
        elif math[1] == '*':
            res = math[0]*math[2]
        elif math[1] == '/':
            res = math[0]/math[2]
        
        math.clear()
        math.append(res)
        count = 0
        
    
#Screen
screen = button("",(191, 195, 201),(54, 53, 51),15,15,120,270) 

#Number Buttons
b7 = button("7",(54, 53, 51),(245, 115, 22),15,222,42,42)
b8 = button("8",(54, 53, 51),(245, 115, 22),72,222,42,42)
b9 = button("9",(54, 53, 51),(245, 115, 22),129,222,42,42)
    
b4 = button("4",(54, 53, 51),(245, 115, 22),15,279,42,42)
b5 = button("5",(54, 53, 51),(245, 115, 22),72,279,42,42)
b6 = button("6",(54, 53, 51),(245, 115, 22),129,279,42,42)
    
b1 = button("1",(54, 53, 51),(245, 115, 22),15,336,42,42)
b2 = button("2",(54, 53, 51),(245, 115, 22),72,336,42,42)
b3 = button("3",(54, 53, 51),(245, 115, 22),129,336,42,42)
    
bdec = button(".",(54, 53, 51),(245, 115, 22),15,393,42,42)
b0 = button("0",(54, 53, 51),(245, 115, 22),72,393,42,99)

#Operator Buttons

badd = button("+",(245, 115, 22),(54, 53, 51),186,222,42,42)
bsub = button("-",(245, 115, 22),(54, 53, 51),186,279,42,42)
bmul = button("*",(245, 115, 22),(54, 53, 51),186,336,42,42)
bdiv = button("/",(245, 115, 22),(54, 53, 51),186,393,42,42)

#Other Buttons

bpow = button("P",(255,0,0),(255,255,255),243,165,42,42)
bclr = button("C",(54, 53, 51),(245, 115, 22),243,222,99,42)
beq = button("=",(245, 115, 22),(54, 53, 51),243,336,99,42)

math = []
count = 0
flag = 1

power = False
run = True

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
            
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    drawCalci()
    
    
    event = pygame.event.wait()
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONUP:
            checkclick(click[0],mouse[0],mouse[1]) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()