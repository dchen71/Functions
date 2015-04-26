'''
   Converts a pattern into integer pattern
   PatternToNumber(AGT) = 4 · PatternToNumber(AG) + SymbolToNumber(T) = 8 + 3 = 11
   
   PatternToNumber(Pattern)
        if Pattern contains no symbols
            return 0
        symbol ← LastSymbol(Pattern)
        remove LastSymbol(Pattern) from Pattern
        return 4 · PatternToNumber(Pattern) + SymbolToNumber(symbol)
 '''