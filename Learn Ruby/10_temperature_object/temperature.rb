#10 temperature_object testfirst.org ruby

class Temperature
  def initialize options
    @fahrenheit = options[:f]||options[:c] * (9.0/5.0) + 32 #options based on what is passed to it
  end

  def in_fahrenheit
    @fahrenheit 
  end

  def in_celsius
    (@fahrenheit - 32) * (5.0/9.0)
  end

  def ftoc
    return ((@fahren -32) * 5.0/9.0)
  end

  def ctof
    return (@celsius * 9.0/5.0 + 32)
  end

  def self.from_celsius(num) #self for each object
    new(:c => num)
  end

  def self.from_fahrenheit(num)
    new(:f => num)
  end

end

class Celsius < Temperature #< creates an class using other class
  def initialize(temp)
    super(c: temp) #super has it call initialize in the main class
  end
end

class Fahrenheit < Temperature
  def initialize(temp)
    super(f: temp)
  end
end