'''
Psuedocode for a faster clump sorter based on sorting
    FindingFrequentWordsBySorting(Text , k)
        FrequentPatterns ← an empty set
        for i ← 0 to |Text| − k
            Pattern ← Text(i, k)
            Index(i) ← PatternToNumber(Pattern)
            Count(i) ← 1
        SortedIndex ← Sort(Index)
        for i ← 1 to |Text| − k
            if SortedIndex(i) = SortedIndex(i − 1)
                Count(i) = Count(i − 1) + 1
        maxCount ← maximum value in Count
        for i ← 0 to |Text| − k
            if Count(i) = maxCount
                Pattern ← NumberToPattern(SortedIndex(i), k)
                add Pattern to the set FrequentPatterns
        return FrequentPatterns
'''