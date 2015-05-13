#Lesson 11 Dictionary TestFirst Ruby


class Dictionary
  def initialize
    @d = Hash.new
  end

  def entries
    return @d
  end

  def add name,value = nil
    @d[name] = value
  end

  #Sorted alphabetically
  def keywords
    @d.keys.sort
  end

  #Checks if the dictionary includes work
  def include? word
    @d.include? word
  end

  #Finds partial or full matches in the key and return key/value
  def find word
    result = {}
    @d.each_pair do|key, value|
      if key =~ /^#{word}/
        result[key] = value
      end
    end
      result
  end

  #Prints out a sorted key/value list
  def printable
    result = ""

    @d.keys.sort.each do|key|
      result += "[#{key}] \"#{@d[key]}\"\n"
    end
    result = result[0..-2]
  end

end