import Unknown

pokemon = Unknown.Unknown(400, 300, 50)

def setup():
  size(800, 600)
  noFill()

def draw():
  background(255)
  rotateY(radians(frameCount))
  rotateX(radians(frameCount))
  pokemon.show()