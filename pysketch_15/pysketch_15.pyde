data =  {
  "fractal" : {
    "size" : 50,
    "limit": 10,
    "multiplier": 0.9
  }
}

def setup():
  size(800, 600, P3D)
  rectMode(CENTER)
  stroke(0)
  strokeWeight(5)

def draw():
  background(200)
  translate(width * 0.5, height * 0.5)
  scale(0.25)
  fractal(data["fractal"]["size"])
  rotateZ(radians(180))
  fractal(data["fractal"]["size"])

def fractal(size):
  rect(0, size, size, size)
  rect(0, -size, size, size)
  rect(size, 0, size, size)
  rect(-size, 0, size, size)
  if size > data["fractal"]["size"] * data["fractal"]["limit"] * 0.01:
    pushMatrix()
    rotateZ(radians(frameCount * 0.9))
    rotateY(radians(frameCount * 0.9))
    rotateX(radians(frameCount * 0.9))
    translate(size * (1 + data["fractal"]["multiplier"]), size * (1 + data["fractal"]["multiplier"]))
    fractal(size * data["fractal"]["multiplier"] )
    popMatrix()
