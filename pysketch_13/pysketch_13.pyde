data = {
  "fractal" : {
    "size" : 300,
    "limit": 5
  }
}

def setup():
  size(800, 600, P3D)
  rectMode(CENTER)
  ellipseMode(CENTER)
  stroke(0)
  strokeWeight(3)

def draw():
  background(50)
  translate(width * 0.5, height * 0.5)
  scale(0.6)
  rotateY(radians(frameCount * 0.3))
  rotateX(radians(frameCount * 0.1))
  fractal(data["fractal"]["size"])
  rotateX(radians(180))
  fractal(data["fractal"]["size"])

def fractal(size):
  ellipse(0, 0, size, size)
  if size > data["fractal"]["size"] * data["fractal"]["limit"] * 0.01:
    pushMatrix()
    translate(0, 0, (15 + 7.5 * sin(radians(frameCount))) )
    fractal(size * 0.9)
    popMatrix()
