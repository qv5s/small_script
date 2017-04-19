from tkinter import *
import random
import time
class Ball(object):
    def __init__(self,canvas,color,paddle):
        self.color1=['blue','red','black','green']
        self.canvas=canvas
        self.paddle=paddle
        self.id=self.canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        a=[-3,-2,-1,1,2,3]
        self.x=random.choice(a)
        self.y=-3
        self.a=0
    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0]and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                canvas.itemconfig(self.id,fill=random.choice(self.color1))
                canvas.itemconfig(self.paddle.id,fill=random.choice(self.color1))
                return 1
        return 0
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[3]==350:
            self.a=1
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas.winfo_height():
            self.y=-3
        if self.hit_paddle(pos)==1:
            self.y=-3
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas.winfo_width():
            self.x=-3
class Paddle(object):
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=self.canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>",self.turn_right)
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.canvas.winfo_width():
            self.x=0
    def turn_left(self,Event):
        self.x=-2
    def turn_right(self,Event):
        self.x=2

if __name__=='__main__':
    tk=Tk()
    tk.title('game')
    tk.resizable(0,0)
    tk.wm_attributes('-topmost',1)
    tk.wm_attributes('-alpha',0.7)
    canvas=Canvas(tk,width=500,height=400)
    canvas.pack()
    paddle=Paddle(canvas,'blue')
    ball=Ball(canvas,'red',paddle)
    while 1:
        if ball.a==0:
            ball.draw()
            paddle.draw()
        if ball.a==1:
            time.sleep(1)
            exit()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)