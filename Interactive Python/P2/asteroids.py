# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def ang_to_rad(ang):
    return ang * (3.14/180)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, 
        self.pos, self.image_size, self.angle)

    def update(self):
        forward = angle_to_vector(self.angle)
        
        for i in range(2):
            self.pos[i] += self.vel[i]
        
        self.pos[0] %= 800
        self.pos[1] %= 600
        
        self.angle += self.angle_vel
        
        if self.thrust == True:
            for i in range(2):
                self.vel[i] *= .7
                self.vel[i] += forward[i]
        else:
            for i in range(2):
                self.vel[i] *= .95
    
    #stop turning
    def stopTurn(self):
        self.angle_vel = 0
    
    #turn left
    def turnL(self):
        self.angle_vel -= ang_to_rad(4)
    
    #turn right                                 
    def turnR(self):
        self.angle_vel += ang_to_rad(4)
            
    #boosters engage
    def boosts(self):
        self.thrust = True
        self.image_center = [130,45]
        ship_thrust_sound.play()
        
    #no gas
    def stop_Boost(self):
        self.thrust = False
        self.image_center = [45,45]
        ship_thrust_sound.pause()
                                     
    #pew pew
    def shoot(self):
        global a_missile
        forward = angle_to_vector(self.angle)
        speed = [0,0]
        mPos = [0,0]
        
        for i in range(2):
            speed[i] = self.vel[i] * 2 * abs(forward[i])
        print self.pos
        
        mPos[0] = self.pos[0] + self.radius * angle_to_vector(self.angle)[0]
        mPos[1] = self.pos[1] + self.radius * angle_to_vector(self.angle)[1]
        print mPos
        a_missile = Sprite(mPos, speed, self.angle, 0, missile_image, missile_info, missile_sound)

# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, 
        self.pos, self.image_size, self.angle)
 
    def update(self):
        for i in range(2):
            self.pos[i] += self.vel[i]
        
        self.pos[0] %= 800
        self.pos[1] %= 600
        
        self.angle += self.angle_vel       

           
def draw(canvas):
    global time, lives, score
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_text('Lives: ' + str(lives),(20,30),25,"white")
    canvas.draw_text('Score: ' + str(score),(680,30),25,"white")
    
    
    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()

# Press handler

def key_press(key):
    for i in pinputs:
        if key == simplegui.KEY_MAP[i]:
            pinputs[i]()
  
# Release handler

def key_release(key):
    for i in rinputs:
        if key == simplegui.KEY_MAP[i]:
            rinputs[i]()    
    
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    vel = [0,0]
    pos = [0,0]
    
    for i in range(2):
        vel[i] = random.randint(-3,3)
    
    pos[0] = random.randint(0,WIDTH)
    pos[1] = random.randint(0,HEIGHT)
    ang = ang_to_rad(random.randint(-5,5))
    
    a_rock = Sprite(pos, vel, 0, ang, asteroid_image, asteroid_info)


    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# Inputs for keyboard handlers.
pinputs = {"up": my_ship.boosts,
           "right": my_ship.turnR,
           "left": my_ship.turnL,
           "space": my_ship.shoot}
rinputs = {"up": my_ship.stop_Boost,
           "right": my_ship.stopTurn,
           "left": my_ship.stopTurn}

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_press)
frame.set_keyup_handler(key_release)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
