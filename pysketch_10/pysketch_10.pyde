def setup ():
    size(800, 600, P3D)
    noStroke()
    rectMode(CENTER)
    
def draw ():
    background(0)
    directionalLight(255, 255, 255, 0, 0, -1)
    lightSpecular(255, 255, 255)
    specular(255, 255, 255)
    translate(width * 0.5, height *0.5)
    scale(0.6)
    ortho()
    rotateY(radians(45))
    rotateX(radians(15))
    rotateY(radians(-35))

    textSize(20)
    for x in range(-35, 35):
      for y in range(-35, 35):
        d = dist(x, y, 0, 0)
        z = noise(x, y) * tan(radians(frameCount + d)) * 200
        pushMatrix()
        translate(x * 20, y * 20, z)
        rect(0, 1, 5, 5)  
        popMatrix()