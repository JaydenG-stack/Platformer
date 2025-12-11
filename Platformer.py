import turtle
import random

screen = turtle.Screen()
screen.title("Turtle Runner - Enhanced Edition")
screen.setup(width=800, height=400)
screen.tracer(0)

# Enhanced gradient sky background
bg = turtle.Turtle()
bg.hideturtle()
bg.speed(0)
bg.penup()
bg.goto(-400, -200)
for i in range(40):
    color = (0.4 + i * 0.015, 0.6 + i * 0.01, 0.95 + i * 0.001)
    screen.colormode(1)
    bg.color(color)
    bg.begin_fill()
    bg.setx(-400)
    bg.sety(-200 + i * 5)
    for _ in range(2):
        bg.forward(800)
        bg.left(90)
        bg.forward(5)
        bg.left(90)
    bg.end_fill()

# Add sun
sun = turtle.Turtle()
sun.hideturtle()
sun.penup()
sun.goto(300, 150)
sun.color("#ffd700")
sun.begin_fill()
sun.circle(30)
sun.end_fill()
# Sun rays
for angle in range(0, 360, 45):
    sun.goto(300, 150)
    sun.setheading(angle)
    sun.pendown()
    sun.pensize(3)
    sun.color("#ffed4e")
    sun.forward(45)
    sun.penup()

# Detailed mountains with multiple layers
mountains = turtle.Turtle()
mountains.hideturtle()
mountains.speed(0)
# Back mountains
mountains.penup()
mountains.goto(-400, -80)
mountains.color("#2d3e40")
mountains.begin_fill()
for x in range(-400, 401, 60):
    mountains.goto(x, random.randint(-60, 40))
mountains.goto(400, -200)
mountains.goto(-400, -200)
mountains.end_fill()
# Front mountains
mountains.penup()
mountains.goto(-400, -100)
mountains.color("#4b5c5e")
mountains.begin_fill()
for x in range(-400, 401, 70):
    mountains.goto(x, random.randint(-80, 10))
mountains.goto(400, -200)
mountains.goto(-400, -200)
mountains.end_fill()

# Textured ground with grass detail
ground = turtle.Turtle()
ground.hideturtle()
ground.penup()
ground.goto(-400, -200)
ground.pendown()
ground.color("#3b7a2a")
ground.begin_fill()
for _ in range(2):
    ground.forward(800)
    ground.left(90)
    ground.forward(100)
    ground.left(90)
ground.end_fill()

# Add grass blades
for _ in range(30):
    grass = turtle.Turtle()
    grass.hideturtle()
    grass.penup()
    grass.goto(random.randint(-390, 390), -100)
    grass.setheading(90)
    grass.color(random.choice(["#2d5016", "#3b7a2a", "#4a8c34"]))
    grass.pendown()
    grass.pensize(2)
    grass.forward(random.randint(8, 15))
    grass.right(random.randint(20, 40))
    grass.forward(random.randint(3, 8))

# Soil layer with texture
soil = turtle.Turtle()
soil.hideturtle()
soil.penup()
soil.goto(-400, -200)
soil.pendown()
soil.color("#5e3d1b")
soil.begin_fill()
for _ in range(2):
    soil.forward(800)
    soil.left(90)
    soil.forward(20)
    soil.left(90)
soil.end_fill()

# Add small rocks/pebbles on ground
for _ in range(15):
    rock = turtle.Turtle()
    rock.hideturtle()
    rock.shape("circle")
    rock.color(random.choice(["#6b5b4a", "#8b7355", "#4a3f35"]))
    rock.shapesize(random.uniform(0.3, 0.6))
    rock.penup()
    rock.goto(random.randint(-380, 380), random.randint(-120, -105))
    rock.showturtle()

# Enhanced clouds with more detail
clouds = []
for _ in range(5):
    cloud_x = random.randint(-350, 350)
    cloud_y = random.randint(90, 180)
    # Create fluffy cloud with multiple puffs
    for i in range(5):
        puff = turtle.Turtle()
        puff.hideturtle()
        puff.shape("circle")
        puff.color("white")
        puff.penup()
        offset_x = i * 15 - 30
        offset_y = random.randint(-8, 8)
        puff.goto(cloud_x + offset_x, cloud_y + offset_y)
        puff.shapesize(random.uniform(1.8, 2.5))
        puff.showturtle()
        clouds.append(puff)

# Enhanced player with details
player = turtle.Turtle()
player.shape("turtle")
player.shapesize(2, 2)
player.penup()
player.goto(-250, -100)
player_speed_y = 0
player_speed_x = 0
gravity = -0.8
is_jumping = False
on_platform = False

# Player color selection
player_color = screen.textinput("Turtle Color", "Choose your turtle color:\n(blue, red, green, purple, orange, pink, yellow, white)\n\nOr enter a hex color like #ff5733")
if not player_color or player_color.strip() == "":
    player_color = "blue"
else:
    player_color = player_color.strip().lower()

# Validate and set color
valid_colors = ["blue", "red", "green", "purple", "orange", "pink", "yellow", "white", "black", "brown", "cyan", "magenta"]
if player_color not in valid_colors and not player_color.startswith("#"):
    player_color = "blue"

player.color(player_color)

# Add player shadow
player_shadow = turtle.Turtle()
player_shadow.hideturtle()
player_shadow.shape("circle")
player_shadow.color("gray")
player_shadow.shapesize(1, 1.5)
player_shadow.penup()
player_shadow.goto(player.xcor(), -120)
player_shadow.showturtle()

# Platform system
platforms = []
platform_speed = 5

# Star collectibles
stars = []

def create_platform(x, y, width):
    platform = turtle.Turtle()
    platform.hideturtle()
    platform.shape("square")
    platform.color("#8b6f47")
    platform.shapesize(stretch_wid=1, stretch_len=width)
    platform.penup()
    platform.goto(x, y)
    platform.width = width * 20  # Actual width in pixels
    platform.height = 20
    platform.showturtle()
    
    # Platform shadow
    shadow = turtle.Turtle()
    shadow.hideturtle()
    shadow.shape("square")
    shadow.color("#5d4a2f")
    shadow.shapesize(stretch_wid=0.8, stretch_len=width)
    shadow.penup()
    shadow.goto(x + 3, y - 3)
    shadow.showturtle()
    platform.shadow = shadow
    
    # Platform decoration
    for i in range(int(width * 2)):
        deco = turtle.Turtle()
        deco.hideturtle()
        deco.shape("circle")
        deco.color("#6b5838")
        deco.shapesize(0.3, 0.3)
        deco.penup()
        deco.goto(x - width * 10 + i * 10, y)
        deco.showturtle()
        if not hasattr(platform, 'decorations'):
            platform.decorations = []
        platform.decorations.append(deco)
    
    # Add star collectible on platform (60% chance)
    if random.random() < 0.6:
        star = create_star(x, y + 35)
        stars.append(star)
        platform.star = star
    
    return platform

def create_star(x, y):
    star = turtle.Turtle()
    star.hideturtle()
    star.penup()
    star.goto(x, y)
    star.color("#ffd700")
    star.speed(0)
    
    # Draw 5-pointed star
    star.begin_fill()
    for _ in range(5):
        star.forward(15)
        star.right(144)
    star.end_fill()
    
    # Add glow effect
    glow = turtle.Turtle()
    glow.hideturtle()
    glow.shape("circle")
    glow.color("#ffed4e")
    glow.shapesize(1.2, 1.2)
    glow.penup()
    glow.goto(x, y)
    glow.showturtle()
    star.glow = glow
    
    # Animation counter
    star.pulse_count = 0
    star.collected = False
    
    return star

def spawn_platform():
    if not game_running:
        return
    y_positions = [-50, -20, 10, 40]
    y = random.choice(y_positions)
    width = random.uniform(2, 4)
    platform = create_platform(400, y, width)
    platforms.append(platform)
    next_spawn = random.randint(2000, 3500)
    screen.ontimer(spawn_platform, next_spawn)

obstacles = []
shooters = []
bullets = []
miners = []
obstacle_speed = 5

score = 0
high_score = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(0, -170)
pen.color("white")
pen.write("Score: 0 | High Score: 0", align="center", font=("Arial", 18, "bold"))

# Health system
health = 3
health_display = []
for i in range(3):
    heart = turtle.Turtle()
    heart.hideturtle()
    heart.shape("circle")
    heart.color("red")
    heart.shapesize(0.8, 0.8)
    heart.penup()
    heart.goto(-350 + i * 30, 170)
    heart.showturtle()
    health_display.append(heart)

game_running = True

def jump():
    global is_jumping, player_speed_y
    if not is_jumping:
        is_jumping = True
        player_speed_y = 15

def move_left():
    global player_speed_x
    player_speed_x = -8

def move_right():
    global player_speed_x
    player_speed_x = 8

def stop_movement():
    global player_speed_x
    player_speed_x = 0

def check_platform_collision():
    global is_jumping, player_speed_y, on_platform
    on_platform = False
    
    player_bottom = player.ycor() - 20
    player_left = player.xcor() - 20
    player_right = player.xcor() + 20
    
    # Check ground collision
    if player_bottom <= -100:
        if player_speed_y < 0:
            player.sety(-80)
            player_speed_y = 0
            is_jumping = False
            on_platform = True
        return
    
    # Check platform collisions (only when falling)
    if player_speed_y < 0:
        for plat in platforms:
            plat_top = plat.ycor() + plat.height/2
            plat_bottom = plat.ycor() - plat.height/2
            plat_left = plat.xcor() - plat.width/2
            plat_right = plat.xcor() + plat.width/2
            
            # Check horizontal overlap
            if player_right > plat_left and player_left < plat_right:
                # Check if player is landing on platform from above
                if player_bottom <= plat_top and player_bottom >= plat_bottom:
                    # Prevent landing if player was already below the platform
                    if player.ycor() - player_speed_y > plat_top:
                        player.sety(plat_top + 20)
                        player_speed_y = 0
                        is_jumping = False
                        on_platform = True
                        return

def spawn_obstacle():
    if not game_running:
        return
    obstacle = turtle.Turtle()
    obstacle.shape("circle")
    color = random.choice(["#e63946", "#f4a261", "#6a4c93", "#1d3557"])
    obstacle.color(color)
    size = random.uniform(1.8, 3.2)
    obstacle.shapesize(stretch_wid=size, stretch_len=size)
    obstacle.penup()
    obstacle.goto(400, -100)
    obstacles.append(obstacle)
    
    # Add glow effect
    glow = turtle.Turtle()
    glow.hideturtle()
    glow.shape("circle")
    glow.color(color)
    glow.shapesize(size + 0.5)
    glow.penup()
    glow.goto(400, -100)
    glow.showturtle()
    obstacle.glow = glow
    
    next_spawn = random.randint(1000, 2000)
    screen.ontimer(spawn_obstacle, next_spawn)

def shoot_bullet(x, y):
    if not game_running:
        return
    bullet = turtle.Turtle()
    bullet.shape("circle")
    bullet.color("#4cc9f0")
    bullet.shapesize(0.5, 0.5)
    bullet.penup()
    bullet.goto(x, y)
    bullets.append(bullet)
    
    # Add bullet trail
    trail = turtle.Turtle()
    trail.hideturtle()
    trail.shape("circle")
    trail.color("#7dd3fc")
    trail.shapesize(0.3, 0.3)
    trail.penup()
    trail.goto(x, y)
    trail.showturtle()
    bullet.trail = trail
    
    def move_bullet():
        if not game_running:
            bullet.hideturtle()
            if hasattr(bullet, 'trail'):
                bullet.trail.hideturtle()
            return
        bullet.sety(bullet.ycor() - 15)
        if hasattr(bullet, 'trail'):
            bullet.trail.goto(bullet.xcor(), bullet.ycor() + 10)
        if bullet.ycor() < -200:
            bullet.hideturtle()
            if hasattr(bullet, 'trail'):
                bullet.trail.hideturtle()
            if bullet in bullets:
                bullets.remove(bullet)
            return
        screen.ontimer(move_bullet, 30)
    move_bullet()

def spawn_shooter():
    if not game_running:
        return
    shooter = turtle.Turtle()
    shooter.shape("triangle")
    shooter.color("#4361ee")
    shooter.shapesize(stretch_wid=2.5, stretch_len=2.5)
    shooter.setheading(270)
    shooter.penup()
    shooter.goto(400, random.randint(70, 150))
    shooters.append(shooter)
    
    # Add shooter outline
    outline = turtle.Turtle()
    outline.hideturtle()
    outline.shape("triangle")
    outline.color("#1e3a8a")
    outline.shapesize(2.8, 2.8)
    outline.setheading(270)
    outline.penup()
    outline.goto(400, shooter.ycor())
    outline.showturtle()
    shooter.outline = outline
    
    def move_shooter():
        if not game_running:
            shooter.hideturtle()
            if hasattr(shooter, 'outline'):
                shooter.outline.hideturtle()
            return
        shooter.setx(shooter.xcor() - 3)
        if hasattr(shooter, 'outline'):
            shooter.outline.goto(shooter.xcor(), shooter.ycor())
        if shooter.xcor() < -450:
            shooter.hideturtle()
            if hasattr(shooter, 'outline'):
                shooter.outline.hideturtle()
            shooters.remove(shooter)
            return
        if random.random() < 0.04:
            shoot_bullet(shooter.xcor(), shooter.ycor() - 20)
        screen.ontimer(move_shooter, 30)
    move_shooter()
    next_spawn = random.randint(3500, 6500)
    screen.ontimer(spawn_shooter, next_spawn)

def MinerBlock():
    if not game_running:
        return
    x = random.randint(-300, 300)
    
    # Enhanced warning with pulsing effect
    warning = turtle.Turtle()
    warning.hideturtle()
    warning.shape("triangle")
    warning.color("red")
    warning.penup()
    warning.goto(x, -120)
    warning.setheading(90)
    warning.shapesize(1.5, 1.5)
    warning.showturtle()
    
    # Pulsing animation
    pulse_count = [0]
    def pulse():
        if pulse_count[0] >= 10:
            return
        size = 1.5 + 0.3 * (pulse_count[0] % 2)
        warning.shapesize(size, size)
        pulse_count[0] += 1
        screen.ontimer(pulse, 100)
    pulse()
    
    def spawn_from_ground():
        warning.hideturtle()
        if not game_running:
            return
        
        # Enhanced explosion effect with more particles
        particles = []
        for _ in range(20):
            particle = turtle.Turtle()
            particle.hideturtle()
            particle.shape("circle")
            particle.color(random.choice(["#ff6b35", "#f7931e", "#fdc500", "#e63946", "#ff4500"]))
            particle.shapesize(random.uniform(0.6, 1.5))
            particle.penup()
            particle.goto(x, -130)
            particle.showturtle()
            particles.append(particle)
            angle = random.randint(0, 360)
            speed = random.uniform(4, 10)
            dx = speed * random.uniform(-1, 1)
            dy = speed * random.uniform(0.5, 1.5)
            def animate_particle(p=particle, vx=dx, vy=dy, life=25):
                if not game_running or life <= 0:
                    p.hideturtle()
                    return
                p.goto(p.xcor() + vx, p.ycor() + vy)
                p.shapesize(p.shapesize()[0] * 0.9)
                screen.ontimer(lambda: animate_particle(p, vx, vy * 0.93 - 0.4, life - 1), 30)
            animate_particle()
        
        # Dust cloud effect
        for _ in range(8):
            dust = turtle.Turtle()
            dust.hideturtle()
            dust.shape("circle")
            dust.color("#8b7355")
            dust.shapesize(random.uniform(1, 2))
            dust.penup()
            dust.goto(x + random.randint(-20, 20), -140)
            dust.showturtle()
            def fade_dust(d=dust, life=15):
                if life <= 0:
                    d.hideturtle()
                    return
                d.sety(d.ycor() + 2)
                d.shapesize(d.shapesize()[0] * 0.95)
                screen.ontimer(lambda: fade_dust(d, life - 1), 50)
            fade_dust()
        
        # Enhanced miner block
        block = turtle.Turtle()
        block.shape("square")
        block.color("#6f4e37")
        block.shapesize(stretch_wid=2.5, stretch_len=2.5)
        block.penup()
        block.goto(x, -150)
        miners.append(block)
        
        # Block shadow
        block_shadow = turtle.Turtle()
        block_shadow.hideturtle()
        block_shadow.shape("square")
        block_shadow.color("#4a3020")
        block_shadow.shapesize(2.8, 2.8)
        block_shadow.penup()
        block_shadow.goto(x + 5, -155)
        block_shadow.showturtle()
        block.shadow = block_shadow
        
        def rise():
            if not game_running:
                return
            block.sety(block.ycor() + 9)
            if hasattr(block, 'shadow'):
                block.shadow.goto(block.xcor() + 5, block.ycor() - 5)
            if block.ycor() >= -70:
                block.hideturtle()
                if hasattr(block, 'shadow'):
                    block.shadow.hideturtle()
                miners.remove(block)
                return
            screen.ontimer(rise, 30)
        rise()
    screen.ontimer(spawn_from_ground, 1000)

def spawn_miner():
    if not game_running:
        return
    MinerBlock()
    next_spawn = random.randint(4500, 7500)
    screen.ontimer(spawn_miner, next_spawn)

def update_score():
    global score, high_score
    score += 1
    if score > high_score:
        high_score = score
    pen.clear()
    pen.write(f"Score: {score} | High Score: {high_score}", align="center", font=("Arial", 18, "bold"))

def collect_star(star):
    global score, high_score
    score += 5
    if score > high_score:
        high_score = score
    pen.clear()
    pen.write(f"Score: {score} | High Score: {high_score}", align="center", font=("Arial", 18, "bold"))
    
    # Collection animation
    star.collected = True
    original_y = star.ycor()
    
    def float_away(count=0):
        if count < 15:
            star.sety(star.ycor() + 3)
            if hasattr(star, 'glow'):
                star.glow.goto(star.xcor(), star.ycor())
            scale = 1.2 - (count * 0.08)
            if hasattr(star, 'glow'):
                star.glow.shapesize(scale, scale)
            screen.ontimer(lambda: float_away(count + 1), 30)
        else:
            star.hideturtle()
            if hasattr(star, 'glow'):
                star.glow.hideturtle()
    
    float_away()

def check_star_collection():
    player_left = player.xcor() - 20
    player_right = player.xcor() + 20
    player_top = player.ycor() + 20
    player_bottom = player.ycor() - 20
    
    for star in list(stars):
        if not star.collected:
            star_x = star.xcor()
            star_y = star.ycor()
            
            if (player_right > star_x - 15 and player_left < star_x + 15 and
                player_top > star_y - 15 and player_bottom < star_y + 15):
                collect_star(star)
                stars.remove(star)

def take_damage():
    global health
    if health > 0:
        health -= 1
        health_display[health].hideturtle()
        # Flash effect
        original_color = player_color
        player.color("red")
        screen.ontimer(lambda: player.color(original_color), 100)
        if health == 0:
            game_over()
            return True
    return False

def check_collision():
    player_left = player.xcor() - 20
    player_right = player.xcor() + 20
    player_top = player.ycor() + 20
    player_bottom = player.ycor() - 20
    
    for obs in obstacles:
        obs_radius = obs.shapesize()[0] * 10
        if player.distance(obs) < (20 + obs_radius):
            return obs
    
    for shooter in shooters:
        shooter_size = shooter.shapesize()[0] * 10
        if player.distance(shooter) < (20 + shooter_size):
            return shooter
    
    for bullet in bullets:
        if player.distance(bullet) < 25:
            return bullet
    
    for miner in miners:
        miner_left = miner.xcor() - 25
        miner_right = miner.xcor() + 25
        miner_top = miner.ycor() + 25
        miner_bottom = miner.ycor() - 25
        
        if (player_right > miner_left and player_left < miner_right and
            player_top > miner_bottom and player_bottom < miner_top):
            return miner
    
    return None

def restart_game():
    global game_running, score, health, player_speed_x, player_speed_y, is_jumping, on_platform
    global obstacles, shooters, bullets, miners, platforms, stars
    
    # Clear all game objects
    for t in obstacles + shooters + bullets + miners:
        t.hideturtle()
        if hasattr(t, 'glow'):
            t.glow.hideturtle()
        if hasattr(t, 'outline'):
            t.outline.hideturtle()
        if hasattr(t, 'trail'):
            t.trail.hideturtle()
        if hasattr(t, 'shadow'):
            t.shadow.hideturtle()
    
    for plat in platforms:
        plat.hideturtle()
        if hasattr(plat, 'shadow'):
            plat.shadow.hideturtle()
        if hasattr(plat, 'decorations'):
            for deco in plat.decorations:
                deco.hideturtle()
        if hasattr(plat, 'star'):
            plat.star.hideturtle()
            if hasattr(plat.star, 'glow'):
                plat.star.glow.hideturtle()
    
    for star in stars:
        star.hideturtle()
        if hasattr(star, 'glow'):
            star.glow.hideturtle()
        if hasattr(plat, 'star'):
            plat.star.hideturtle()
            if hasattr(plat.star, 'glow'):
                plat.star.glow.hideturtle()
    
    for star in stars:
        star.hideturtle()
        if hasattr(star, 'glow'):
            star.glow.hideturtle()
    
    # Reset lists
    obstacles.clear()
    shooters.clear()
    bullets.clear()
    miners.clear()
    platforms.clear()
    stars.clear()
    
    # Reset player
    player.showturtle()
    player.goto(-250, -100)
    player.color("blue")
    player_speed_x = 0
    player_speed_y = 0
    is_jumping = False
    on_platform = False
    
    # Reset shadow
    player_shadow.showturtle()
    player_shadow.goto(player.xcor(), -120)
    
    # Reset score
    score = 0
    pen.clear()
    pen.goto(0, -170)
    pen.color("white")
    pen.write(f"Score: {score} | High Score: {high_score}", align="center", font=("Arial", 18, "bold"))
    
    # Reset health
    health = 3
    for heart in health_display:
        heart.showturtle()
    
    # Restart game
    game_running = True
    screen.ontimer(spawn_obstacle, 2000)
    screen.ontimer(spawn_shooter, 4000)
    screen.ontimer(spawn_miner, 5000)
    screen.ontimer(spawn_platform, 1500)
    game_loop()

def game_over():
    global game_running
    game_running = False
    pen.goto(0, 0)
    pen.color("red")
    pen.write("GAME OVER", align="center", font=("Arial", 32, "bold"))
    pen.goto(0, -30)
    pen.color("white")
    pen.write(f"Final Score: {score}", align="center", font=("Arial", 20, "normal"))
    pen.goto(0, -60)
    pen.color("#4cc9f0")
    pen.write("Press R to Restart", align="center", font=("Arial", 18, "normal"))
    player.hideturtle()
    player_shadow.hideturtle()
    for t in obstacles + shooters + bullets + miners:
        t.hideturtle()
        if hasattr(t, 'glow'):
            t.glow.hideturtle()
        if hasattr(t, 'outline'):
            t.outline.hideturtle()
        if hasattr(t, 'trail'):
            t.trail.hideturtle()
        if hasattr(t, 'shadow'):
            t.shadow.hideturtle()
    for plat in platforms:
        plat.hideturtle()
        if hasattr(plat, 'shadow'):
            plat.shadow.hideturtle()
        if hasattr(plat, 'decorations'):
            for deco in plat.decorations:
                deco.hideturtle()

def game_loop():
    global player_speed_y, player_speed_x, is_jumping
    if not game_running:
        return
    
    # Apply gravity continuously
    if player.ycor() > -80 or not on_platform:
        player_speed_y += gravity
    
    # Update vertical position
    new_y = player.ycor() + player_speed_y
    player.sety(new_y)
    
    # Check platform collisions after moving
    check_platform_collision()
    
    # Apply horizontal movement
    new_x = player.xcor() + player_speed_x
    if new_x < -360:
        new_x = -360
    if new_x > 360:
        new_x = 360
    player.setx(new_x)
    
    # Calculate shadow position
    shadow_y = -120
    shadow_found = False
    
    # Find the highest surface below the player
    for plat in platforms:
        if (player.xcor() + 20 > plat.xcor() - plat.width/2 and 
            player.xcor() - 20 < plat.xcor() + plat.width/2):
            plat_surface = plat.ycor() + plat.height/2
            if plat_surface < player.ycor() and plat_surface > shadow_y - 120:
                shadow_y = plat_surface - 15
                shadow_found = True
    
    # Update shadow
    player_shadow.goto(player.xcor(), shadow_y)
    distance_to_shadow = abs(player.ycor() - shadow_y)
    shadow_scale = max(0.3, 1.0 - (distance_to_shadow * 0.005))
    player_shadow.shapesize(shadow_scale * 0.8, shadow_scale * 1.2)
    
    # Move and update platforms
    for plat in list(platforms):
        new_plat_x = plat.xcor() - platform_speed
        plat.setx(new_plat_x)
        
        if hasattr(plat, 'shadow'):
            plat.shadow.goto(new_plat_x + 3, plat.ycor() - 3)
        
        if hasattr(plat, 'decorations'):
            for i, deco in enumerate(plat.decorations):
                deco.setx(new_plat_x - plat.width * 10 + i * 10)
        
        # Move star with platform
        if hasattr(plat, 'star') and not plat.star.collected:
            plat.star.goto(new_plat_x, plat.star.ycor())
            if hasattr(plat.star, 'glow'):
                plat.star.glow.goto(new_plat_x, plat.star.ycor())
        
        # Remove off-screen platforms
        if plat.xcor() < -450:
            plat.hideturtle()
            if hasattr(plat, 'shadow'):
                plat.shadow.hideturtle()
            if hasattr(plat, 'decorations'):
                for deco in plat.decorations:
                    deco.hideturtle()
            if hasattr(plat, 'star'):
                plat.star.hideturtle()
                if hasattr(plat.star, 'glow'):
                    plat.star.glow.hideturtle()
                if plat.star in stars:
                    stars.remove(plat.star)
            platforms.remove(plat)
    
    # Animate stars (pulsing effect)
    for star in stars:
        if not star.collected:
            star.pulse_count += 1
            scale = 1.0 + 0.2 * abs((star.pulse_count % 40) - 20) / 20
            if hasattr(star, 'glow'):
                star.glow.shapesize(scale, scale)
    
    # Check star collection
    check_star_collection()
    
    # Move and update obstacles
    for obs in list(obstacles):
        new_obs_x = obs.xcor() - obstacle_speed
        obs.setx(new_obs_x)
        
        if hasattr(obs, 'glow'):
            obs.glow.goto(new_obs_x, obs.ycor())
        
        # Remove off-screen obstacles and award points
        if obs.xcor() < -450:
            obs.hideturtle()
            if hasattr(obs, 'glow'):
                obs.glow.hideturtle()
            obstacles.remove(obs)
            update_score()
    
    # Check collisions
    collision = check_collision()
    if collision:
        if not take_damage():
            # Remove the collided object
            if collision in obstacles:
                collision.hideturtle()
                if hasattr(collision, 'glow'):
                    collision.glow.hideturtle()
                obstacles.remove(collision)
            elif collision in bullets:
                collision.hideturtle()
                if hasattr(collision, 'trail'):
                    collision.trail.hideturtle()
                bullets.remove(collision)
            elif collision in miners:
                collision.hideturtle()
                if hasattr(collision, 'shadow'):
                    collision.shadow.hideturtle()
                miners.remove(collision)
            elif collision in shooters:
                collision.hideturtle()
                if hasattr(collision, 'outline'):
                    collision.outline.hideturtle()
                shooters.remove(collision)
    
    # Update screen
    screen.update()
    screen.ontimer(game_loop, 20)  # ~50 FPS

screen.listen()
screen.onkey(jump, "w")
screen.onkey(jump, "Up")
screen.onkey(restart_game, "r")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_right, "Right")
screen.onkeyrelease(stop_movement, "a")
screen.onkeyrelease(stop_movement, "d")
screen.onkeyrelease(stop_movement, "Left")
screen.onkeyrelease(stop_movement, "Right")

screen.ontimer(spawn_obstacle, 2000)
screen.ontimer(spawn_shooter, 4000)
screen.ontimer(spawn_miner, 5000)
screen.ontimer(spawn_platform, 1500)
game_loop()

turtle.done()
