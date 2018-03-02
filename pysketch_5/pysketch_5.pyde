data =  {
  "sketch" : "#111111",
  "fractal" : {
    "limit": 5,
    "size": 200
  }
}

def setup():
  size(800, 600, P3D)
  ellipseMode(CENTER)
  rectMode(CENTER)
  colorMode(HSB, 100)

def draw():
  background(data["sketch"])
  translate(width * 0.5, height * 0.5)
  rotateY(radians(frameCount))
  fractal(data["fractal"]["size"])

def fractal(size):
  rect(0, 0, size, size)
  rotateX(radians(frameCount + 2 * size / data["fractal"]["size"]))
  if size > data["fractal"]["size"] * 0.01 * data["fractal"]["limit"]:
    pushMatrix()
    translate(size * 0.75 , size * 0.75)
    fractal(size * 0.5)    
    popMatrix()

    pushMatrix()
    translate(size * 0.75 , -size * 0.75)
    fractal(size * 0.5)    
    popMatrix()

    pushMatrix()
    translate(-size * 0.75, -size * 0.75)
    fractal(size * 0.5)    
    popMatrix()

    pushMatrix()
    translate(-size * 0.75, size * 0.75)
    fractal(size * 0.5)    
    popMatrix()
