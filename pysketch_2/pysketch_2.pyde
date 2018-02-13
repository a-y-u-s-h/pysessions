scl = 20
col = 800 / scl
row = 600 / scl

def setup():
  size(800, 600, P3D)

def draw():
  background(0)
  translate(width * 0.5, height * 0.5)
  rotateX(PI/3)
  translate(-width * 0.5, -height * 0.5)
  fill(255)
  stroke(0)
  for y in range(0, row):
    beginShape(TRIANGLE_STRIP)
    for x in range(0, col):
        n = noise(x * scl, y * scl)
        m = noise(x * scl, (y + 1) * scl)
        vertex(x * scl, y * scl, n * 20 * sin(frameCount * 0.1 * n + n * 10))
        vertex(x * scl, (y + 1) * scl, m * 20 * cos(frameCount * 0.1 * n + m * 10))
    endShape()