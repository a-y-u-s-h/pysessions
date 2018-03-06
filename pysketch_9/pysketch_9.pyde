data =  {
  "fractal": {
    "size": 100,
    "limit": 10,
    "multiplier": 0.7
  }
}

def setup():
  size(800, 600, P3D)
  rectMode(CENTER)
  noStroke()

def draw():
  background(0)
  translate(width * 0.5, height * 0.5)
  scale(0.5)
  directionalLight(102, 102, 102, 0, 0, -1)
  lightSpecular(204, 204, 204)
  ambientLight(50, 50, 50)
  directionalLight(102, 102, 102, 0, 1, -1)
  lightSpecular(102, 102, 102)
  specular(50, 50, 50)

  sphere(data["fractal"]["size"])
  fractal(data["fractal"]["size"])

  pushMatrix()
  rotateZ(radians(72))
  fractal(data["fractal"]["size"])
  popMatrix()

  pushMatrix()
  rotateZ(radians(-72))
  fractal(data["fractal"]["size"])
  popMatrix()

  pushMatrix()
  rotateZ(radians(2 * 72))
  fractal(data["fractal"]["size"])
  popMatrix()

  pushMatrix()
  rotateZ(radians(2 * -72))
  fractal(data["fractal"]["size"])
  popMatrix()

def fractal(size):
  pushMatrix()
  generation = log(data["fractal"]["size"]) / log(size)
  x = (size + size * data["fractal"]["multiplier"]) * cos(radians(frameCount * 0.1)) + 30 * cos(radians(frameCount * generation))
  y = (size + size * data["fractal"]["multiplier"]) * sin(radians(frameCount * 0.1)) + 30 * sin(radians(frameCount * generation))
  translate(x, y)
  pushMatrix()
  scale(1 + 0.2 *sin(radians(frameCount + map(generation, 0, 10, 0, 360)) ))
  sphere(size)
  popMatrix()
  if size > 0.01 * data["fractal"]["limit"] * data["fractal"]["size"]:
    fractal(size * data["fractal"]["multiplier"])
  popMatrix()
