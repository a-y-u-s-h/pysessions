n = 10

def setup ():
    size(800, 600, P3D)
    rectMode(CENTER)
    noStroke()
    ellipseMode(CENTER)
    noFill()
    textSize(20)

def draw ():
    background(0)
    translate(width * 0.5, height * 0.5)
    ortho()
    rotateY(radians(45))
    rotateX(radians(-15))
    for x in range(-15, 15):
      for y in range(-15, 15):
        c = color(noise(x, y) * 127.5 + 127.5, noise(x, y) * 127.5 + 127.5, noise(x, y) * 127.5 + 127.5)    
        fill(c)
        d = dist(x, y, 0, 0)
        pushMatrix()
        translate(x * 10, y * 10 + d * noise(x, y), 200 * sin(radians(frameCount + d * 2)) + noise(x, y) * d * tan(radians(frameCount * d * 0.05 +  2 * d)))
        rotateX(radians(frameCount *2 + d * 10))
        if noise(x, y) < 0.5:
          text("o", 0, 0)
        else:
          text("1", 0, 0)  
        popMatrix()

