

def setup():
  size(800, 600, P3D)
  rectMode(CENTER)
  ellipseMode(CENTER)  
  noStroke()
  textSize(20)
  textAlign(CENTER, CENTER)
  textMode(MODEL)

def draw():
  background(255)
  translate(width * 0.5, height * 0.5)
  # rotateY(radians(frameCount * 0.1))
  scale(0.3)
  for x in range(-15, 15):
    for y in range(-15, 15):
      d = dist(x, y, 0, 0)
      pushMatrix()
      translate(x * 20 + 2 * d * sin(radians(frameCount + d * 100 *sin(radians(frameCount * 0.3)))), y * 20 + 2 * d * cos(radians(frameCount + d * 100 *sin(radians(frameCount * 0.3)))), d * 100 *sin(radians(frameCount * 0.3)))
      # fill(0, 50)
      # ellipse(0 ,0, 20, 20)
      fill(0)
      if noise(x, y) < 0.5:
        text("0", 0, 0)
      else:
        text("1", 0, 0)        
      popMatrix()
      