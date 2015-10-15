require_relative "count_word"

text = 'AGGGCGCGTCTGGGCGCGGGGCGCGGGG'
pat = "^GGGC"

solution = CountWords.new(text,pat)
puts solution.count_pat
