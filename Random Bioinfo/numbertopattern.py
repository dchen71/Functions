'''
    NumberToPattern(index, k)
        if k = 1
            return NumberToSymbol(index)
        prefixIndex ← Quotient(index, 4)
        r ← Remainder(index, 4)
        PrefixPattern ← NumberToPattern(prefixIndex, k − 1)
        symbol ← NumberToSymbol(r)
        return concatenation of PrefixPattern with symbol
'''
    