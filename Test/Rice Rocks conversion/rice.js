//Implementation of rice rocks(An Interactive Introduction to Python) back into full javascript

//Global variables for user interface
var WIDTH = 800;
var HEIGHT = 600;
var score = 0;
var lives = 3;
var time = 0;
var started = false;


//Image Helper prototype
var ImageInfo = function(center,size,radius,lifespan,animated){
	this.center = center;
	this.size = size;
	this.radius = radius;
	var lifespan = none;

	if(lifespan)
		this.lifespan = lifespan;
	else
		this.lifespan = float('inf');
	this.animated = animated;
}

ImageInfo.prototype.get_center() = function() {
	return this.center;
}

ImageInfo.prototype.get_size() = function() {
	return this.size;
}

ImageInfo.prototype.get_radius() = function() {
	return this.radius;
}

ImageInfo.prototype.get_lifespan() = function() {
	return this.lifespan;
}

ImageInfo.prototype.get_animated() = function() {
	return this.animated;
}


//Simplegui prototype which uses existing naming structure to support the loading of images and sounds
var simplegui = function() {}

simplegui.prototype.load_image = function(dataUrl){
	var imageObj = new Image();
	imageObj.onload = function(){
		context.drawImage(this,0,0)
	}
}

simplegui.prototype.load_sound(dataUrl) = function(dataUrl){
	var snd = new Audio(dataUrl);
	snd.play();	
}


//Image/Sound loading section
//art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
//debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
//                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
//need to figureout the simplegui load image
var debris_info = ImageInfo([320, 240], [640, 480])
var debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

// nebula images - nebula_brown.png, nebula_blue.png
var nebula_info = ImageInfo([400, 300], [800, 600])
var nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

// splash image
var splash_info = ImageInfo([200, 150], [400, 300])
var splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

// ship image
var ship_info = ImageInfo([45, 45], [90, 90], 35)
var ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

// missile image - shot1.png, shot2.png, shot3.png
var missile_info = ImageInfo([5,5], [10, 10], 3, 50)
var missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

// asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
var asteroid_info = ImageInfo([45, 45], [90, 90], 40)
var asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

// animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
var explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, true)
var explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

// sound assets purchased from sounddogs.com, please do not redistribute
// .ogg versions of sounds are also available, just replace .mp3 by .ogg
//need to figure out the load sound and set volume
var soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
var missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
var missile_sound.set_volume(.5)
var ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
var explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

// helper functions to handle transformations
function angle_to_vector(ang)
    return [Math.cos(ang), Math.sin(ang)]

function dist(p, q)
    return Math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

//Does group to object collision check
function group_collide(group, other_Object)
    global explosion_group; //how to declare global var
    var collided = false;
    for sprite in set(group){
    	if sprite.collide(other_Object){
			group.remove(sprite);
			collided = true;
			explosion_group.add(Sprite(sprite.pos, [0, 0], 0, 0, explosion_image,explosion_info, explosion_sound));
    	}
	}
    
    return collided;

//Does group to group collision check
function group_group_collide(group, other_Group)
    hit = 0;
    for sprite in set(group){
		if group_collide(other_Group, sprite){
			hit += 1;
			group.remove(sprite);
		}

    }
        
    return hit;


//Supports group sprite processing
function process_sprite_group(spriteSet, canvas):
    for sprites in spriteSet{
    	sprites.draw(canvas);
        if sprites.update()
            spriteSet.remove(sprites);
    }
            

// Ship class
class Ship (pos, vel, angle, image, info){
        this.pos = [pos[0], pos[1]];
        this.vel = [vel[0], vel[1]];
        this.thrust = false;
        this.angle = angle;
        this.angle_vel = 0;
        this.image = image;
        this.image_center = info.get_center();
        this.image_size = info.get_size();
        this.radius = info.get_radius();
        
    function draw(canvas){
    	if this.thrust:
            canvas.draw_image(this.image, [this.image_center[0] + this.image_size[0], this.image_center[1]] , this.image_size,this.pos, this.image_size, this.angle);
        else:
            canvas.draw_image(this.image, this.image_center, this.image_size,this.pos, this.image_size, this.angle);
        
    }

    function update(){
        // update angle
        this.angle += this.angle_vel;
        
        // update position
        this.pos[0] = (this.pos[0] + this.vel[0]) % WIDTH;
        this.pos[1] = (this.pos[1] + this.vel[1]) % HEIGHT;

        // update velocity
        if this.thrust{
        	var acc = angle_to_vector(this.angle);
            this.vel[0] += acc[0] * .1;
            this.vel[1] += acc[1] * .1;
        }
            
        this.vel[0] *= .99;
        this.vel[1] *= .99;

    function set_thrust(on){
		this.thrust = on;
		if on{
			ship_thrust_sound.rewind();
			ship_thrust_sound.play();
        }
        else
			ship_thrust_sound.pause();
	}

	function increment_angle_vel(){
        this.angle_vel += .05;
	}
        
    function decrement_angle_vel(){
        this.angle_vel -= .05;
    }
        
    function shoot(){
        global missile_group;
        forward = angle_to_vector(this.angle);
        missile_pos = [this.pos[0] + this.radius * forward[0], this.pos[1] + this.radius * forward[1]];
        missile_vel = [this.vel[0] + 6 * forward[0], this.vel[1] + 6 * forward[1]];
        a_missile = Sprite(missile_pos, missile_vel, this.angle, 0, missile_image, missile_info, missile_sound);
        missile_group.add(a_missile);
    }

    function get_radius(){
        return this.radius;
    }
    
    function get_pos(){
        return this.pos;
    }
}
}

// Sprite class
class Sprite(pos, vel, ang, ang_vel, image, info, sound = None){
        this.pos = [pos[0],pos[1]];
        this.vel = [vel[0],vel[1]];
        this.init_vel = [vel[0],vel[1]];
        this.angle = ang;
        this.angle_vel = ang_vel;
        this.image = image;
        this.image_center = info.get_center();
        this.image_size = info.get_size();
        this.radius = info.get_radius();
        this.lifespan = info.get_lifespan();
        this.animated = info.get_animated();
        this.age = 0;
        if sound{
            sound.rewind();
            sound.play();
        }

    function draw(canvas){
        center = list(this.image_center)
        if this.animated:
            center[0] = this.image_center[0] + (this.image_size[0] * this.age);
        canvas.draw_image(this.image, center, this.image_size,
                          this.pos, this.image_size, this.angle);
	}

    function update(){
        // update angle
        this.angle += this.angle_vel;
        
        // update position
        this.pos[0] = (this.pos[0] + this.vel[0]) % WIDTH;
        this.pos[1] = (this.pos[1] + this.vel[1]) % HEIGHT;

        this.age += 1;
        if this.age >= this.lifespan
            return true;
        else
            return false;
    }

    function get_position(this)
        return this.pos;
    
    function get_radius(this)
        return this.radius;
        
        //Checks if it collides and returns true if true
    function collide(this, other_Object)
        return dist(this.pos, other_Object.pos) <= this.radius + other_Object.radius;
}    

// key handlers to control ship   
function keydown(key){
    if key == simplegui.KEY_MAP['left']
        my_ship.decrement_angle_vel();
    elif key == simplegui.KEY_MAP['right']
        my_ship.increment_angle_vel();
    elif key == simplegui.KEY_MAP['up']
        my_ship.set_thrust(true);
    elif key == simplegui.KEY_MAP['space']
        my_ship.shoot();
}

function keyup(key){
    if key == simplegui.KEY_MAP['left']
        my_ship.increment_angle_vel();
    elif key == simplegui.KEY_MAP['right']
        my_ship.decrement_angle_vel();
    elif key == simplegui.KEY_MAP['up']
        my_ship.set_thrust(false);
}

// mouseclick handlers that reset UI and conditions whether splash image is drawn
function click(pos){
    global started, lives, score, soundtrack;
    center = [WIDTH / 2, HEIGHT / 2];
    size = splash_info.get_size();
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2);
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2);
    if (not started) and inwidth and inheight{
        started = true;
        lives =3;
        score = 0;
        soundtrack.rewind();
        soundtrack.play();
	}
}

function draw(canvas){
    global time, started, lives, score,rock_group, explosion_group;
    
    // animiate background
    time += 1;
    wtime = (time / 4) % WIDTH;
    center = debris_info.get_center();
    size = debris_info.get_size();
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT]);
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT));
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT));

    // draw UI
    canvas.draw_text("Lives", [50, 50], 22, "White");
    canvas.draw_text("Score", [680, 50], 22, "White");
    canvas.draw_text(str(lives), [50, 80], 22, "White");
    canvas.draw_text(str(score), [680, 80], 22, "White");

    // draw/update ship
    my_ship.draw(canvas);
    my_ship.update();
    
    //Draw rocks/missiles/splosions
    process_sprite_group(rock_group,canvas);
    process_sprite_group(missile_group,canvas);
    process_sprite_group(explosion_group,canvas);
    
    //Rock speed up
    for rock in rock_group{
        for i in range(2)
            rock.vel[i] = rock.init_vel[i] + (rock.init_vel[i] * score * 0.005);
    }
 
    if(group_collide(rock_group,my_ship))
        lives -= 1;
    
    if(lives == 0){
        rock_group = set();
        started = false;
    }

    score += 100 * group_group_collide(missile_group, rock_group);
    
    // draw splash screen if not started
    if(not started)
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size());
 }

// timer handler that spawns a rock    
function rock_spawner(){
    global rock_group, started;
    if started{
        if(len(rock_group) <= 12){
            rock_pos = [Math.random() * WIDTH, Math.random() * HEIGHT];
            rock_vel = [Math.random() * .6 - .3, Math.random() * .6 - .3];
            rock_avel = Math.random() * .2 - .1;
            while(dist(rock_pos, my_ship.pos) < 150){
                rock_pos = [Math.random() *  WIDTH, Math.random() *  HEIGHT];
            }
            a_rock = Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info);
            rock_group.add(a_rock);
        } 
        else
            pass;
    }
}
// initialize stuff
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT);

// initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info);
rock_group = set();
missile_group = set();
explosion_group = set();

// register handlers
frame.set_keyup_handler(keyup);
frame.set_keydown_handler(keydown);
frame.set_mouseclick_handler(click);
frame.set_draw_handler(draw);

timer = simplegui.create_timer(1000.0, rock_spawner);

// get things rolling
timer.start();
frame.start();
