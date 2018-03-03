class Unknown():
  def __init__(self, cx, cy, size):
    self.cx = cx
    self.cy = cy
    self.size = size

  def show(self):
    translate(self.cx, self.cy)
    fill("#FFFFFF")

    # Outer Arc's boundary
    pushMatrix()
    stroke("#000000")
    strokeWeight(self.size * 4 / 5)
    arc(0, 0, self.size * 6, self.size * 6, -4 *PI/3 + PI/6, PI/3 - PI/6)
    popMatrix()


    # Connector's Border
    pushMatrix()
    stroke("#000000")
    strokeWeight(self.size * 4 / 5)
    line(0, 0, 0, -self.size * 3)
    popMatrix()

    # Connector itself
    pushMatrix()
    stroke("#3F3B3A")
    strokeWeight(self.size * 3 / 5)
    line(0, 0, 0, -self.size * 3)
    popMatrix()

    # Outer Arc itself
    pushMatrix()
    noFill()
    stroke("#3F3B3A")
    strokeWeight(self.size * 3 / 5)
    arc(0, 0, self.size * 6, self.size * 6, -4 *PI/3 + PI/6, PI/3 - PI/6)
    popMatrix()

    # Inner Arc's boundary
    pushMatrix()
    stroke("#000000")
    strokeWeight(self.size * 5 / 5)
    arc(0, 0, self.size * 2.5, self.size * 2.5,0, 2 * PI)
    popMatrix()

    # Inner Arc itself
    pushMatrix()
    stroke("#3F3B3A")
    strokeWeight(self.size * 4 / 5)
    arc(0, 0, self.size * 2.5, self.size * 2.5,0, 2 * PI)
    popMatrix()

    # Connector itself (continued.. important)
    pushMatrix()
    stroke("#3F3B3A")
    strokeWeight(self.size * 3 / 5)
    line(0, 0, 0, -self.size * 3)
    popMatrix()

    # Eyeball's Boundary
    pushMatrix()
    stroke("#000000")
    strokeWeight(self.size * 0.2)
    arc(0, 0, self.size * 2, self.size * 2,0, 2 * PI)
    popMatrix()

    # Eyeball itself
    pushMatrix()
    fill("#FFFFFF")
    noStroke()
    ellipse(0, 0, self.size * 2, self.size * 2)
    popMatrix()

    # Iris
    pushMatrix()
    fill("#000000")
    noStroke()
    ellipse(0, 0, self.size * 0.8, self.size * 0.8)
    popMatrix()

    # Iris Shine
    pushMatrix()
    fill("#FFFFFF")
    noStroke()
    ellipse(-self.size * 0.1, -self.size * 0.1, self.size * 0.25, self.size * 0.25)
    popMatrix()

    # HORN = LEFT
    pushMatrix()
    rotate(-PI/4)
    translate(0, - self.size)
    # Horn - Left's Border
    pushMatrix()
    stroke("#000000")
    strokeWeight(self.size * 4 / 5)
    line(0, -self.size * 2.5, 0, -self.size * 3)
    popMatrix()

    # Horn - Left itself
    pushMatrix()
    stroke("#3F3B3A")
    strokeWeight(self.size * 3 / 5)
    line(0, -self.size * 2, 0, -self.size * 3)
    popMatrix()

    popMatrix()

    # HORN - RIGHT
    pushMatrix()
    rotate(PI/4)
    translate(0, - self.size)
    # Horn - Left's Border
    pushMatrix()
    stroke("#000000")
    strokeWeight(self.size * 4 / 5)
    line(0, -self.size * 2.5, 0, -self.size * 3)
    popMatrix()

    # Horn - Left itself
    pushMatrix()
    stroke("#3F3B3A")
    strokeWeight(self.size * 3 / 5)
    line(0, -self.size * 2, 0, -self.size * 3)
    popMatrix()

    popMatrix()