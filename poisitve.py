import os, random

def gl(file):
    gl.ml = []
    with open(file, 'r') as f:
        for line in f:
            gl.ml.append(line)

def cr(list):
    with open("message.vbs", 'w') as f:
        f.write("")
    index = random.randrange(0, (len(list))) 
    with open("message.vbs", 'a') as f:
        vbs = "x=msgbox("+'"'+list[index]+'"'+","+str(0)+","+'"'+"Positivity"+'"'+")"
        for charecter in vbs:
            f.write(charecter)

while True:
    gl("positive.txt")
    cr(gl.ml)
    break