#Implement all parts of this assignment within (this) module2_assignment2.rb file

#Implement a class called LineAnalyzer.
  #Implement the following read-only attributes in the LineAnalyzer class. 
  #* highest_wf_count - a number with maximum number of occurrences for a single word (calculated)
  #* highest_wf_words - an array of words with the maximum number of occurrences (calculated)
  #* content,         - the string analyzed (provided)
  #* line_number      - the line number analyzed (provided)
class LineAnalyzer
  attr_accessor :highest_wf_count, :highest_wf_words, :content, :line_number

  #Implement the initialize() method to:
  #* take in a line of text and line number
  #* initialize the content and line_number attributes
  #* call the calculate_word_frequency() method.
  def initialize(content, line_number)
    self.content ||= "test"
    self.content = content
    self.line_number = line_number
    
    self.highest_wf_count = 0
    self.highest_wf_words = Array.new
    calculate_word_frequency()
  end

  #Implement the calculate_word_frequency() method to:
  #* calculate the maximum number of times a single word appears within
  #  provided content and store that in the highest_wf_count attribute.
  #* identify the words that were used the maximum number of times and
  #  store that in the highest_wf_words attribute.
  def calculate_word_frequency()
  	#calc the highest freq word and count
  	freq = Hash.new(0)
  	@content.split.each do |word|
  		freq[word.downcase] += 1
  	end

  	@highest_wf_count = freq.values.max
  	freq.each_pair do |key, value|
  		@highest_wf_words.push(key) if value == @highest_wf_count
  	end
  end
end

#  Implement a class called Solution. 
  # Implement the following read-only attributes in the Solution class.
  #* highest_count_across_lines - a number with the value of the highest frequency of a word
  #* highest_count_words_across_lines - an array with the words with the highest frequency
class Solution
  def initialize
    @analyzers = Array.new
  end

  # Implement the analyze_file() method() to:
  #* Read the 'test.txt' file in lines 
  #* Create an array of LineAnalyzers for each line in the file
  def analyze_file()
    if File.exist? 'test.txt'
      @line_number = 0
      File.foreach('test.txt') do |line|
        @line_number += 1
        @analyzers.push(LineAnalyzer.new(line, @line_number))
      end
    end
  end

  # Implement the calculate_line_with_highest_frequency() method to:
  #* calculate the highest number of occurences of a word across all lines
  #and stores this result in the highest_count_across_lines attribute.
  #* identifies the words that were used with the highest number of occurrences
  #and stores them in print_highest_word_frequency_across_lines.
  def calculate_line_with_highest_frequency()
    @highest_count_across_lines = 0
    @highest_count_words_across_lines = Array.new
    @values = Array.new
    
    #Finds the highest count for a word
    @analyzers.each do |line|
      @values.push(line.highest_wf_count)
    end

    @highest_count_across_lines = @values.max

    #Gets the highest value words
    @analyzers.each do |line|
      if line.highest_wf_count == @highest_count_across_lines
        @highest_count_words_across_lines.push(line.line_number)
      end
    end

  end

  #Implement the print_highest_word_frequency_across_lines() method to
  #* print the result in the following format
  def print_highest_word_frequency_across_lines
    puts "The following words have the highest word frequency per line: "
    @highest_count_words_across_lines.each do |line|
      puts "#{@analyzers[line - 1].highest_wf_words} on line #{line}"
    end
  end

  def analyzers
    @analyzers
  end

  #Traditional getters
  def highest_count_words_across_lines
  	@highest_count_words_across_lines
  end

  def highest_count_across_lines
  	@highest_count_across_lines
  end
end
