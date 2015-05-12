#05 silly_blocks TestFirst.org Ruby

#Reverses a string
def reverser()
  yield.split(' ').each {|word| word.reverse!}.join(' ')
end

#Adds 1 + input
def adder(n=1)
  yield + n
end


#Repeats something n times
def repeater(n=1)
  n.times {yield}
end