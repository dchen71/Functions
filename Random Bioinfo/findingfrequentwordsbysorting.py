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

#Need to build numbertopattern and to test
def FindingFrequentWordsBySorting(Text, k):
    FrequentPatterns = set()
    for i in range(len(Text) - k):
        Pattern = Text[i:i +k]
        Index[i] = PatternToNumber(Pattern)
        Count[i] = 1
    SortedIndex = sorted(Index)
    for i = 1 in range(len(text) - k):
        if SortedIndex[i] == SortedIndex[i - 1]:
            count[i] = count[i - 1] + 1
    maxCount = max(count)
    for i in range(len(text) - k):
        if count[i] == maxCount:
            Pattern = NumberToPattern(SortedIndex[i], k)
            FrequentPatterns.add(Pattern)
    return FrequentPatterns