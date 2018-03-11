def setup():
  size(800, 600, P3D)
  rectMode(CENTER)

def draw():
  background(0, 10)
  translate(width * 0.5, height * 0.5)
  scale(0.2)
  rotateZ(radians(90))
  rotateX(radians(frameCount * 0.2))
  rotateY(radians(- frameCount * 0.2))
  for x in range(-25, 25):
    pushMatrix()
    rotateX(radians(frameCount  * 2 + x * 10))
    rotateX(radians(90))
    rect(x * 60, 0, 5, 600)
    ellipse(x * 60, 300, 30, 30)
    ellipse(x * 60, -300, 30, 30)
    popMatrix()