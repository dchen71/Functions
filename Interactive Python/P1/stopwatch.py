# template for "Stopwatch: The Game"

import simplegui, time

# define global variables
cTime = 0
x = 0 #successful stop
y = 0 #total stop
running = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    d = t % 10
    c = ((t - d) % 100) /10
    b = (t / 100) % 6
    a = int(t/600)
    return(str(a) + ':' + str(b) + str(c) + '.' + str(d))
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global running
    running = True
    timer.start()

def stop_handler():
    global x, y, running
    if(running == True):
        if(cTime %10 == 0):
            x+= 1
        y += 1
        running = False
    timer.stop()

def reset_handler():
    global cTime, x ,y
    cTime = 0
    x = 0
    y = 0
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global cTime
    cTime += 1
    

# define draw handler
def draw_handler(canvas):
    global cTime
    canvas.draw_text(format(cTime),(180,100),20,"white")
    canvas.draw_text('Success: '+ str(x),(280,40),20,"white")
    canvas.draw_text('Total: ' + str(y),(280,20),20,"white")

    
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 400, 200)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_handler)
frame.add_button("Stop", stop_handler)
frame.add_button("Reset", reset_handler)


# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric
