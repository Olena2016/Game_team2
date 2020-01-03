
width=540
height=640
def setup():
    size(width, height)
    background(0)
def rectangle_gray():
    fill(129,135,128)
    rect(0,20,width,height) 
def rectangle_bleu():
    fill(41,90,227)
    rect(10,30,width-20,height) 
def rectangles_red():
    fill(219,29,29)
    x=10
    y=30
    for j in range(10):        
            rect(x,y,(width-20)/10,30)
            x=x+(width-20)/10
            noLoop    
    translate(0,y)       
    noLoop           
def draw():
     rectangle_gray() 
     rectangle_bleu()
     y=30
     rectangles_red()
     pushMatrix()
     for i in range(7): 
        y=(y*i)       
        translate(0,y)
        rectangles_red()
     popMatrix()
     
