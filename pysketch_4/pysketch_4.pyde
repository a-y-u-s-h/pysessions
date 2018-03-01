def setup():
  size(800, 600, P3D)
  rectMode(CENTER)
  ellipseMode(CENTER)

def draw():
  background(0)
  ambientLight(255, 255, 255)
  fill(0, 51, 102)
  ambientLight(102, 102, 102)
  lightSpecular(204, 204, 204)
  directionalLight(102, 102, 102, 0, 0, -1)
  specular(255)
  shininess(1.0)
  translate(width * 0.5, height * 0.15)
  scale(0.4)
  sphereDetail(1)
  fractal(100)


def fractal(size):
  rotateY(radians(frameCount))
  sphere(size)
  if size > 10:
    translate(size, size, size)
    fractal(size * 0.9)
