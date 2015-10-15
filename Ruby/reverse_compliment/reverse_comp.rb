# Given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

class ReverseCompliment
  attr_accessor :orig, :rev

  #Contrstuctor
  def initialize(orig)
    self.orig = orig
    self.rev = ""
    @bases = {'A'=>'T', 'T'=>'A', 'C'=>'G', 'G'=>'C'}
  end

  #Calculates minimal number of jumps from x to y
  def reverse
    self.orig.reverse!.split("").each do |base|
      self.rev += @bases[base]
    end
    self.rev
  end
end
