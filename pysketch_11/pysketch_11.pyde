n = 10

def setup ():
    size(800, 600, P3D)
    rectMode(CENTER)
    noStroke()
    ellipseMode(CENTER)
    noFill()

def draw ():
    background(0)
    translate(width * 0.5, height * 0.5)
    ortho()
    rotateY(radians(45))
    rotateX(radians(-15))
    # rotateY(radians(frameCount * 0.1))
    for x in range(-20, 20):
      for y in range(-20, 20):
        c = color(noise(x, y) * 127.5 + 127.5, noise(x, y) * 127.5 + 127.5, noise(x, y) * 127.5 + 127.5)    
        fill(c)
        d = dist(x, y, 0, 0)
        pushMatrix()
        translate(x * 10, y * 10 + d * noise(x, y), 200 * sin(radians(frameCount + d * 2)) + noise(x, y) * d * tan(radians(frameCount * d * 0.05 +  2 * d)))
        rotateX(radians(frameCount *2 + d * 10))
        rect(0, 0, 10, 10)
        popMatrix()

