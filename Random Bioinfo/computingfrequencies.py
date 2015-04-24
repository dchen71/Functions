'''
Sets up genome and matches it and adds to value as found
    ComputingFrequencies(Text , k)
        for i ← 0 to 4k − 1
            FrequencyArray(i) ← 0
        for i ← 0 to |Text| − k
            Pattern ← Text(i, k)
            j ← PatternToNumber(Pattern)
            FrequencyArray(j) ← FrequencyArray(j) + 1
        return FrequencyArray
'''