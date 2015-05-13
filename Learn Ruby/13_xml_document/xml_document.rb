#13 xml_document test-first Ruby

class XmlDocument
  def initialize indent = false
    @indent = indent
    @indents = 0
  end


  def method_missing(m, *args, &block)
    attributes = args[0] || {}
    xml = ""
    if args[0] == nil
      xml += ("  " * @indents) if @indent
      xml += "<#{m}" #no arguemnts
    else
      xml += ("  " * @indents) if @indent
      xml += "<#{m} "
      attributes.each_pair do |key,value|
        xml += "#{key}=\'#{value}\'" #no arguments class
      end
    end
    
    if block
      xml += ">"
      xml += "\n" if @indent
      @indents += 1
      xml += yield 
      @indents -= 1
      xml << ("  " * @indents) if @indent
      xml += "</#{m}>"
      xml += "\n" if @indent

    else
      xml += "/>"
      xml << "\n" if @indent
    end

    xml
  end

end