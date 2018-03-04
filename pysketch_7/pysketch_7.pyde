def setup():
  size(600, 600, P3D)
  noStroke()

def draw():
  background(255)
  translate(width * 0.5, height * 0.5)
  directionalLight(102, 102, 102, 0, 0, -1)
  lightSpecular(204, 204, 204)
  ambientLight(20, 20, 20)
  rotateY(radians(frameCount))
  rotateZ(radians(frameCount * 0.1))
  rotateX(radians(frameCount * 0.3))
  specular(255, 255, 255)
  for x in range(-25, 25):
    pushMatrix()
    translate(x * 10 - 2.5, 100 * sin(radians(frameCount * x * 0.1 - x * 10)) - 2.5, 100 *cos(radians(frameCount * x * 0.1 - x * 10) ) - 2.5)
    sphere(5)
    popMatrix()      
  