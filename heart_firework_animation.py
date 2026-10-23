import turtle as t
import math
import random
import time

# ---------------------------------------------------------
# PINK HEART FIREWORK ANIMATION
# Inspired by the Instagram reel shown in your screenshot.
# Uses only Python's built-in turtle, math, random and time.
# ---------------------------------------------------------

WIDTH = 800
HEIGHT = 800
PARTICLES_PER_BURST = 850
HEART_PARTICLES = 750
FPS_DELAY = 0.015

screen = t.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pink Heart Fireworks")
screen.tracer(0, 0)

drawer = t.Turtle()
drawer.hideturtle()
drawer.speed(0)
drawer.penup()

COLORS = [
    "#ff1493", "#ff2d95", "#ff69b4", "#ff85c1",
    "#ffc0cb", "#ffffff", "#d946ef", "#c71585"
]

def heart_point(angle, scale):
    """Return an (x, y) point on a classic heart curve."""
    x = 16 * math.sin(angle) ** 3
    y = (13 * math.cos(angle)
         - 5 * math.cos(2 * angle)
         - 2 * math.cos(3 * angle)
         - math.cos(4 * angle))
    return x * scale, y * scale

def draw_particle(x, y, size, color):
    drawer.goto(x, y)
    drawer.dot(size, color)

def draw_heart_outline(cx, cy, scale, count=HEART_PARTICLES):
    """Draw a sparkling, slightly irregular heart outline."""
    for _ in range(count):
        angle = random.uniform(0, 2 * math.pi)
        # Points stay near the curve so the heart remains recognizable.
        radius = scale * random.uniform(0.94, 1.04)
        x, y = heart_point(angle, radius)
        x += random.uniform(-3, 3)
        y += random.uniform(-3, 3)
        draw_particle(cx + x, cy + y,
                      random.choice([2, 2, 3, 3, 4]),
                      random.choice(COLORS))

def draw_heart_fill(cx, cy, scale, count=450):
    """Add a few particles inside the heart."""
    for _ in range(count):
        angle = random.uniform(0, 2 * math.pi)
        radius = scale * math.sqrt(random.random())
        x, y = heart_point(angle, radius)
        draw_particle(cx + x, cy + y,
                      random.choice([2, 2, 3]),
                      random.choice(COLORS))

def firework_burst(cx, cy, amount=PARTICLES_PER_BURST, max_radius=280):
    """Animate particles expanding from a central point."""
    particles = []
    for _ in range(amount):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2.0, 8.0)
        particles.append({
            "x": cx, "y": cy,
            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed,
            "life": random.randint(18, 42),
            "size": random.choice([1, 2, 2, 3]),
            "color": random.choice(COLORS)
        })

    for frame in range(43):
        drawer.clear()
        for p in particles:
            if p["life"] <= 0:
                continue
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            # Gravity and drag make the burst fall and slow down.
            p["vy"] -= 0.045
            p["vx"] *= 0.985
            p["vy"] *= 0.985
            p["life"] -= 1
            if math.hypot(p["x"] - cx, p["y"] - cy) < max_radius:
                draw_particle(p["x"], p["y"], p["size"], p["color"])
        screen.update()
        time.sleep(FPS_DELAY)

def heart_burst_animation():
    """Burst outward, then reveal a pink heart made of sparkles."""
    cx, cy = 0, 0

    # First: a central firework that spreads outward.
    firework_burst(cx, cy, amount=PARTICLES_PER_BURST, max_radius=300)

    # Next: heart particles appear in several quick waves.
    for wave in range(5):
        drawer.clear()
        draw_heart_outline(cx, cy, scale=13.5, count=HEART_PARTICLES)
        # Add a little more sparkle around the outside.
        for _ in range(160):
            angle = random.uniform(0, 2 * math.pi)
            radius = random.uniform(14, 19)
            x, y = heart_point(angle, radius)
            draw_particle(x, y, random.choice([1, 2, 3]),
                          random.choice(COLORS))
        screen.update()
        time.sleep(0.18)

    # Add the inner particles and keep the final heart on screen.
    drawer.clear()
    draw_heart_fill(cx, cy, scale=13.5, count=700)
    draw_heart_outline(cx, cy, scale=13.5, count=HEART_PARTICLES)
    screen.update()

    # Gentle twinkling around the heart, similar to the reel's sparkles.
    while True:
        # Add a small batch of sparkles per frame; the heart stays visible.
        for _ in range(18):
            angle = random.uniform(0, 2 * math.pi)
            radius = random.uniform(14, 20)
            x, y = heart_point(angle, radius)
            draw_particle(x, y, random.choice([1, 2, 3]),
                          random.choice(COLORS))
        screen.update()
        time.sleep(0.08)

try:
    heart_burst_animation()
except t.Terminator:
    pass
