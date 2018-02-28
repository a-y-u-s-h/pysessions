def setup():
  size(800, 600, P3D)
  rectMode(CENTER)
  ellipseMode(CENTER)
  colorMode(HSB, 100);

def draw():
  background(0)
  translate(width * 0.5, height * 0.5)
  for x in xrange(-40,40):
    fill(map(x, -40, 40, 0, 100), 100, 50)
    rotateY(radians(frameCount * 0.01 + 10 * sin(x * 0.02 + frameCount * 0.02)))
    rect(0, x * 10, 300 * noise(0, x * 10 + 100 * sin(radians(frameCount * 0.01) )), 10)
    

