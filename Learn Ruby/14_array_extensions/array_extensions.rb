#14 Array_extensions Testfirst Ruby

class Array
  def sum
    total = 0
    self.each do |x|
      total += x
    end
    total
  end

  def square
    map{|x| x ** 2}
  end

  def square!
    map!{|x| x **2} #! modifys methods to original
  end
end