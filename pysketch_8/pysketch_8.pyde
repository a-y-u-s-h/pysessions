data = {
  "scaleX" : 10,
  "scaleY" : 10
}

def setup():
  size(1000, 600, P3D)
  rectMode(CENTER)
  colorMode(HSB, 100)

def draw():
  background(30)
  translate(width * 0.5, height * 0.5)
  rotateX(radians(-45))
  rotateY(radians(30+ frameCount * 0.1))
  rotateX(radians(90))
  rotateX(radians(10))
  ortho()
  pushMatrix()
  translate(0, -width * 0.25, 0)
  for x in range(-20, 20):
    for y in range(-20, 20):
      d = dist(x, y, 0, 0)
      pushMatrix()
      translate(x * data["scaleX"], y * data["scaleY"], 0)
      rotateY(radians(frameCount * 5 + d * 15))
      rect(0, 0, data["scaleX"], data["scaleY"])
      popMatrix()
  popMatrix()

  pushMatrix()
  translate(0, width * 0.25, 0)
  for x in range(-20, 20):
    for y in range(-20, 20):
      d = dist(x, y, 0, 0)
      pushMatrix()
      translate(x * data["scaleX"], y * data["scaleY"], 30 * sin( radians(frameCount * 5 + d * 15) ) )
      # rotateY(radians(frameCount * 5 + d * 15))
      rect(0, 0, data["scaleX"], data["scaleY"])
      popMatrix()
  popMatrix()