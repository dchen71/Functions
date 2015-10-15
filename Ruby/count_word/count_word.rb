# Given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

class CountWords
  attr_accessor :text, :pat, :counts

  #Contrstuctor
  def initialize(text, pattern)
    self.text = text
    self.pat = pattern
    self.counts = 0
  end

  #Calculates minimal number of jumps from x to y
  def count_pat
    self.counts = self.text.scan(self.pat).length
    self.counts
  end
end
