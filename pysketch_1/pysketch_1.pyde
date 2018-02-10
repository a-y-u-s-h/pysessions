rscale = 300

def setup():
  size(800, 600, P3D)


def draw():
    background(0)
    translate(width * 0.5, height * 0.5)
    rotateY(frameCount * 0.01)
    rotateX(frameCount * 0.005)
    beta = 0
    noFill()
    stroke(255)
    beginShape()
    while beta < PI:
      r = (0.8 + 1.6 * sin(6 * beta)) * rscale
      theta = 2 * beta
      phi = 0.6 * PI * sin(12 * beta)
      x = r * cos(phi) * cos(theta)
      y = r * cos(phi) * sin(theta)
      z = r * sin(phi)
      vertex(x, y, z)
      beta += 0.001
    endShape()