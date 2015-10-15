# Given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

class Leapfrog
  attr_accessor :x, :y, :d, :jumps

  #Contrstuctor
  def initialize(x1, y1, d1)
    self.x = x1
    self.y = y1
    self.d = d1
    self.jumps = 0
  end

  #Calculates minimal number of jumps from x to y
  def calc_jumps
    if self.x < self.y
      self.jumps = ((self.y-self.x).to_f/self.d).ceil
    end
    self.jumps
  end
end
