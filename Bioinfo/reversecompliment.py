#Finds the reverse compliment of a DNA string
def reverse(dna):
	comp = ""
	dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

	#Builds complimentary pairing
	for i in dna:
		comp = dict[i] + comp
	
	#Return 3' to 5'
	return(comp)

assert reverse('AAAACCCGGT') == "ACCGGGTTTT"
assert reverse("AAGAGAGTGGTGACGCCGGAGTGTCTCTCGAAATTTGCGCTTGGAAAGTCTTCGCACGCAAGGACGAGGATTTGACTTAGGGCAACACCGAATGGATCCTTCAAATGATGGTGAGCTTTATTGCAAGGGGCGCCCTGGTTGCCGCATAATTGTAATCTTATCTGCTGAGGCGGTGATCCGTGGGAGCATCGCCATGTACATACGACTGTTTGTGAAGACAGTAAACCCCAGTACCAACATTCCATAGTTTGTGCATTGAGGCACCCAGCAGCCGACCGAGACTGCGCGACGCAAAGCGAGCCATAAGGCCCTGGCCATGTACAGGGTCTTTCAAGAGCGACCTCTGACCCCAGAGCAGTATGTCCTCACGACTATCTCTCCCTCTGTGAGTTATGCATGAAGGATGATGGCATCCCCGGCCTGCGCGCCTCCAGAGGGCAGTTTTAAATGCGCTGGCTAGCCTGTGACAGCCATTTTTTAGTCGGGGTCATAGAGCCCCCAAGTATCCTGTCAGACCTCACACGTGATGACATTTCGGCCGTGTCTCTACGTCGCTAGATGAGTTTGGACATATTTACTAGATCTGTGTTTTACGATCACGCAGAGGCTTGGGTTTCACATCGGACCGCGGTGCAAGTATATCCGTGGTGTTGTGCCATGTCGCATGGGATGACATAGCTAACCGCTACCGTTGGATTAGCGGATTGACAAATCGTCTCAAGCCTTGGAGGCAGGAATTGTGTCAAGTCAGCTCGGACTAGCTCTAGGACTCCGTATGCAATAGAACGCGAAGGCCCAGTTACCATCAGCTCGCGCGTTGACTGCTGGGTAGACACTGCTTGCTCCTAACGAGGAGTAGGTCATCCATCGGCGAACATCATTGATTGGGCACATCGTTAACTACTGTGCTATGCGACAATGCTGCTACGTCCTTAATAACCGTGATAAGCAACGTGGCACTGATCGGGATAACAAGGGCTTAGACGGATGGTACTTAGTTACGCCTGGGATCCGTATCGGGGTCAAATTGCACCCACTTTAGAGCCCTGACAGGTCCCTAGAAGTACGCTTAAAAGGCGCAACCAAAACCGCCTCATGTCAAGACCTTTTCCAGATCAGAGTCGGTCTGTCCGTTTCGATAATTTTACCGCTGGTACTCCACATCAGGCCCTTGCGGAAAGAACCGATCGTGGGCGGCGTAGAACGGTGTGATGACCCTAGAATTTGTGAGGTCTTTACTTTCTATGAGATTATCAATTTGACGAAACTTAGTGAAGCAAAATAGCGTCCGTAGGATGGCGTGCAGGTCGATGTGGTACCGATACAAACGCGAAGATACTCGCCTGCACGCATCACTTACGTATAACAGACCGATCATGTATGAAAACGGGGGTTGCAGCGTCCTACACAACAGTTAGTTGGCGCCAGGTTCGGCGCAGCACGCAACATCGTGAACTGAATACAACTTAGAGGTGCGTTTTGACGTACCTTTCGATGCCTGAATAAACAAGATCGCCCCACAGACGCGAGTCGTCTCTCGAAATTAAACTACTCGCTATATCTCGTTACTAATAGGCAACTCACCTCAGTGAACTACTTTCATTAAATTCAATATACCCCCCGGAATTAGCAACTCCACACGAAACCAGCTGACGGCACGCCGGCAATTGGGAGAGATAAGCGAAATCAATTAGCAATATCTTAACAGTCATTTCTTCGGACAACAGCTATCATTGGCTACCCCTAGCTAATAGTATATAATGATATGTTACGCGTATCAATTTCGATCCCAAGGGGAATCATGGTGCACCTGGTCGGAACGCAATGATCTCGTATCAGCTTCGCGGTTGTTCAGTTCTGATTCTGCAGTAGAACCGTTCATTTTTTCAATGGGAGGTAACTGATACCAAAAAGGAACTAGGGTCGTGACTTTCACAACTTCACATTCACCCAGTGTACCAATCAGGGGATGAATGCTGAAAGAATAATCTGCTGCGAGACCGAGTTGGTAGTCACTTACGTCCAGCTGAGCCAAAAAGCATTGTCCGGTAATTCGGTCAAATAAAGTTACTGCAGCAAAGCGGGCTACTAAGCTTCTTCAATCTAGCCTTAGGGCGGCGCGGCGCCGCGAGGACGCAGACGCTGGTGTTCAATCCCAGAATCTTCAATCCAAGGTGAGATATATCCTGCCTCGAAGACTTCGTGCCTTCAGATCGGATGTAGTTGCACTGTGATGGGGACAGTTAATTGGTCATCTCATTCCAATACGTAGACCGCTCATAGGGGGGGTCCTTAATGGGCGTCGACAGCACCCACTTGGCATAACGCAACTTTCTCCGGCCGTGTGACATAGCTCTATGCAAGCTTCGATCTTTGGGCATCAACCAGAGAACGAAACGTGCGAGGCATTAACCTCTTCAGCCTATTTATCTACGAAGGAAACACATCTACGATACATGATATAAAGATGAAACACAGTGTATTCTACGCTGTTCATAACCTATCCAAGTCGCGTTAGTTTGAGGCGCGACATATGCTTGAAGATATAGCACAGCTTGATCTGAGTGTGGCAAGCCTTTCGAACGTGACTCCTCCCGACATGGTGAAACCTGAAGGAGCGTGTATTTTTGCGTTCAACCTCCGGTTGTTTCGGACTACCTTTGCACGGAGCACGCTCTCGAATCGCTGATAGGCGACAACGGGGGCCGTTGGCGGTTTCTACATGTTGTCAAAGCGTTAATACAATCTCGCTGACGCGGGGGGGAACTTGTGCCCCCATATTCACGGATAACAGTCCGGTGTATTAGTCTTGGTTTGCATGAGCGGGGCCATTGTATAGAACTGCTCTCTTTAGGTCCATTTGATGAACGACTGCGCTGCTTGGCCCTCAGATATCTTTTTATCTCCATGCTGATGAGTCTGCTCGCGTCCCAGCAGGGTGCAGTACATAATCACCTAGCTGGCCCAAAATATGCCCGGCAAGCATCTATTATAAAATGAGATGGCAGGTGTTACTTAAGTGTGATTCGCGGATTTAGGCGGTATGACATGAAACGGCTCTTCTATTCTCAGCTCATGAGGACATCGCGACGATGTACACTAGTCGATTAGTTTGGTTATCAGCTATCGCGATCGCCAAACTAGTATGGTCACTCTGTAACGAGACATGACGACCTATTGGTAACGGTTCTGGGGGCGATATATTGTACTTTGCAGATGCGGCTTCTGGTGTGGCAAGGTTGTGATTACTAAAAATCTACGGCAGCTTTGCGCGCCGTTGTTTAGGAACATCCTCATCCAGTTCGGCCAGATGTCCCCCGTAATCGCGGATTAAGTAGGCGACCACGATTCGTCGGCACCACACCCGCTTAAAAACATGGAATTATTCTATCCGCTAATGGCTGTCTTAGTGAGATGCCTCCGGGTTTGCAGCATCACTAGTGGCAGCATGAGGGATGGGCCATCCTGAAGGTCCGGACACGCGCTTCGTCTGACAAAATTCAATTTATACCTTCTCCTACTAGAGATTATGGAGAGAGACTGTTCTTGTCAGGAGTCAACCCTGGTTTAAGATCCAGTCACTGACCACGAGCCCCGGGGGTCATGTTGATTTTAACCGCCAGTTTGGTGACTTGTAGCTGGCGCTCACATGGTATCACTGCGCGCTTACAAAGCGCCAAAAGGATCGTAGGGAGTGTCACCTCCACTTAGAATCGGAACGCCGAGTAAAGCTCGTGGTGCACTACGCATTGTCGCAGACGTTTGATCCTGCGCGCCGGGCGCTAGTGTTCTGCCTTAGACCTAACCTCGGGCTGAAGAACGGGCAAATGGTCACCGAATGCAAACAATGACAGACAGTGTGCCTCGAAAGTTTAGAGCGTATTGGCAAGTTCAATGGTGGTAGAGAGGTTCTTCGCGACTCCATGTCCTGAGTGTGGTTAAGGCAGTTGCACCGTGAAGTTGATAACCTCAAATCTAGCTTAGTAAAGCTGCGGCTCAATTCTTGTCCACGTGGCAAACTACCGCTGTTTGGCACATACGCTCACGCTATATTGATCCGAGGAGTTCCGTTACCCGCAATTCCAACTAGACACATTGTGTCCACACCCCCTAACGGATATCTGCAGTGAAAGTGGCGTCTAACGAATACAATAATTGTGCGACTTTCAGACCTCTTTTCTTAGTGGGTCCGACAATGACCAAGTTTGCAAACAGTCGAAGGGCAATGCTAAACAAGGCGCACAAGCTGGGGTCCTTTGACTGAGCCGGAATGTGTACTGTGCCATACTGGTACGTGGTCCGGACACGGTTCCCGCGATAGGTTGCTGCTGTCAGTATGTCTTTGTATAAGTCATATGGCCATCCTCGCGACGTCGAGTCCATGGGGCGCATCGGTCGAATGGAGTTCAAACCCTAGGGAGCGGGCCCGAGACCTATTGGGCCAGTTGTGGTCCGTTGTGTACAACGCGCCGGCCATGAGCTCAAGACTAATATGCAGAAATGAGTAGCACCGTGCGCTAGAATAAAATGAAAGCGGAGGGATCAATTTTGGAATTCGTACCCGAACCTTGAATCGCAGAAAATTCGACTGTTGTGGTCTTAACTTGAGCTCAATGGGGACTGGCGAGTAGGGATCCCACGGGGACTATCATACACCGGTCCGCCCACATAGCTAACGAAGAAGCAAACAGGTTAATACTGGTTCCCATGAATTTTTGTATTCGTGACTTGCTGTTCTGAGCGATGCTCTTCCCTGTGTCGTAACTAACATCGGGTTTATCCTACCTTAAGGCTGGGTCGGCATATCGAACCCTGATGGGCGGGACAGTCCTTCAAGGCGTGACCAACCATTCTTGAGGACAATGCGCAGGCGCTAGTCTCTAAGTGCCTCCGGTGTCAGAAGGGTTGCATAAACAGTTAGGCGACTGCAAGCCATAGGACTTGATGCCTACTTACACTCAGGGTTGGCTTACTCCTAGTCTATAAAGTCAGCGCGCGGTGGCGCGGTAACACTTATTCCAGTTCGCCGAGAGTACGCGCCGCTTATCAGGGACGTATGTGGCAGATACGTGCAGACAACCTATGTAGTTATATCCTACCCGTTAAACTCACGCAAAATCAGCAACCCAGTCTTACGCCCTGGAACGGAAACACTTTTCCGGCGCGACCTCTCGCCATGCCACACATGCGATGATCGATCCCTTGGAAGTGTGGGACAACGTTCTATAATCTACGACGGCTCTACTGACGCGGTAATGTATGCTGGCCCATTCGTAAACAGCAGATAGATGTAAGACCTTCGCGTTGATTAGGCTTCAACCGACCTCAACAATATCTCCCTAGCCTTGTATACAAATGACTCCCTCTGTGTGTGTATGTAAAGGCTACATGTATGGGCGGGCGGGTCCGTCAAAATAGAACGCCTTAGACATCCAGGATGTTCTCTTATATACGTCGTCAGACATTTCGCTAAGGTTACCAGACGTAGGCTACTAGACGCTAGGTTCGAACGGACGCAGATCTTGATGACGCGATATCCAGCCGACTATCCAGATGGTTGTCACACACCTCACCATACGTTTGACCACAACACTTATCATCCCGCGCTCGTTATTTTTTCAGCGGTTCCACAACAATTCGGTGCCAATCCTTACGATACTGCTTGGCTATCTGGTGATACAAAGGGCAATTAACCGGCAGGCAATCTATTCGTATTGCGTCGCTTTCATGTTTATTTTTGTCATACAGATCCACCATAGCCGCGTATTGCCGACTTTCATGAGAGAGTCGGATCGTTTTCGCCTATGATTCTAACATAGGCACAACTCATTACTACGTTCACTTACGGTGCTCCCGCTCCTAAGGGCAAATATTAACGTCCACCGTATTTTCAGGAGAAAAGGTAGGTGCGATGTACAAGTGTCTCGCTTGGGGGGCCGTAAGTAGAAGGGTGGATGACCTTGCTAGTGTCAAACGTATCAACACAGCACTCTAGTGGCCGTACTCCGTAGACATGGGTTGAGCCCAAAAGACCATACGTAACGCGAAGGTCCCACTATCGGAGCGGGGTTACTTAGCTGGTGGATGTCCTACGGCTTTGACAGTCGTTCGTGATCAGGTCTGGGCAACGGGCTATGTCAATCAAGGCTACCCACAGTAGATGTTAAAAGGGGAAGGTGGTATTAATTTTAACATTGAGAGGGAAGACGCATCCTTGAAGTTAACGCTGATGCCCCAGGAAAATGTCAGCTCCCCCATCGATGGGCACAGCAAACACATACCCTGAAGTCAGGTTGCATACCCGTGCATCGGCCCAAGCATGGGATCGTCTGGTGGAAAACCGAAGACTTCGAGCTGATAGAGGCCTTCCTCCATTCTGAGCTGTCTCAGGCTCCACGATCGGGCCTTAGGATAAGCTGGTGGACTATTAAGAATCCTCTCATATCGTTATGATACTGGCGACGTTACATATTGACGGTAAGGAGCTATTTTTGGCTCTGTTTTCGGGCCATATTACCACCTTGATGATAGTAGCCGTAATAAACCCGGGGCATTTCAGCGGTGTACGGTTCAGCGCGCTAGCTACGCTATGTTTCTAGACTAAACCGGTCCTTCGACGAGTCCACCAGGGCTGATGTCGCCACTATTCTTGCCGTCCAGACTTACGTCGACAAAACTCGCATGTGGCCTCTGGCGCGCCAGAATGAACCATGTATCCTACCTAGGGGCTTTATGTGAATTCGTGATAGGATCACCAACAAATCCTTAAGTTGTTCCAGAATTAGTCAGAGTTGCTTGGACTGACCAACGCAATTGAAGTAATGTAACATTCATATTGAAAGTTGTACTTGAGAGCAAGGCCTGATAGAGAGCACGCCGGACTCCGAGCGGTCATGGCATATCTGCCAACCTAGTCGCCACGCACCCTTTGATCGATGAGTCGGGCGCTCACACAGATAAGTTCTCCAAGCGGATGGTATATATCTGAGACAAATGTGCTAAGCTCTTCAGGTCAAAAGGTATTATCGACGCAGTCCTGCACTAAGACGAACCCATAGTGTCTCAAGGTATTTCGACATAAGCTTATTTTACTTAGACGTGCACCGGTCCCCAGTAAATGGTCCGTCGTGACGTTGACCTTAGACCAGTTGATAGCACAATACCACATTATGTACAGGAAGATCTCTATGTAGGACAGTAGCAGATAAAGTTCACGCTGGACGCCAGCCGCAAACGATGTAATATATGGTGTAAGATCTATTTCCCCGCTCGTGCCCGGGCAGGAACGACGCGGTCCAGTTAACCGAACTTCTATCAGAAACTGCCAGGCTGCTGAAGATCATGCCTCAAAATTACTCACCTACAACTGCCGGCGTCTTACTCCGATGGACTCGGACCCTAGTCATACATAGAAAGGCCGTTGCTTAAGACGGTTCCACATCCAAACTGGACAGCACCGTTTACTGTCTAAGTTTTACTGTGCATATGCCTTCGGAGTGTGCTTGATTCTGACCGGCCAAGAGGATGCCTGACATGATATCAGAATCCGTGTTTCTTCAGTGCACCCAGAGTACCCTAATTGCGTATGACGAGAGGCGGATCCAAGGTCTTCTCGACACGCCCCGCAGTGCTTACATTTTTTACGTATACAATTAGAGTAAGAGTCAGATTCACAACTCGCAACGAACACGACCAAGCTGAAGTTATTTCCGTTGTCTACTCGAGAGCCGGGTGCTTATTGTAGAGAGTGAAAGATTAAGGACTCACTGCGTCGCGCAGGGTGGATTGCTAATAATGCGTTCAGGCCCGCTTGGGAAAGACGCAGCGCCGAGCGGAGAGGTTAAAACGGTAACGCTACTCTATTGAGTGAGGACCTGTCTGGCGCTTGACTACCATGTTAACAGCAATTCGCGTGCTGTCTAGGTCTTAAGTTAACGGCATGGTTTCGACTTTTGACACAATAATCTCGTTCATTGATAAACAAAGTTGGGTCCAGAAGAGTACAGGCAACTAAACAAGCCAAGAGACTTAAATCTAGCTATGTAGTGAAGTAATGTTATCATTCATCATCTAAACTGTTCACAGCCCCGGTCTTTTCAGCGGCACACTGGGAACGCAATTCAGGGCAATATCTACGTCGGGTACTACGGCTGTGCATATCAACGACTCTAAGGCTCATAAAAGTTAGCGTTGCACTCGCAGATCTACGTCTATAGCGTGTGATCGTTTTTCTGGAGTTAGAAAACAGACTCATTCGATTGGTGTCTCGTGACTGCCGCCCTTCAGGTCCCGAGGACCGTGATGTGGTCCCACCGCGGGGTCAGAGCCTCGGGCATGCCACGCGGCCAGGTTCATCGTTCACGAGCTCGCCAACGGCAATTACCAAAAGTGTGAGCTTGTCGATCGTGTTTTCATTTTTTAACGTCACCCCTAGCATAGATGGAGCCTTCGTAAAAAACTGCAGCATAAAGGGGCCAGGATTGTTCAAAAGACTTCTTGTAAACCGCGAGCACTGGGTGAGAATGGGTCATCCGTCTCCTCCTTGGATCCTCTGGTCTACAATAAAGAGTGAATGAGCAACGTTTTGGACTCGCTCTGCGACTAGCCATTTAAGAATCGAAATGGGAGCCAGCCGTACTCGTTAAGTTGGAGAGTTCTACGTTCAGTTGAACGTAGCAGGGAGTGACTACGGGCTCGGATGCTCCCCAGATCGCACTCGCAGAGTCTTTAACTCGCCCTTAAGTCGCGCACCATGATGACCGCGATCAAATTAACGGGGTGGCTATATCTCCGAAACCTTGAATCTCCTTGCCCCCAGTCTGGTGGGTTTTATGCTTCGATAACGAAGGGCAGGTTATATGGTTACTGGGTAGGGGCTCTCGAGTTGCCTGGGAAGGGACGCCGGCTTTGAGAACAGAGTTTCAATTAGGATCGCGCAGGCCCTGTGACACGAAACTACTCCTTCAAGGTTACCTACCTATATCTATGGTTATAAAACGGAATCGGCACGCACAAGAATTCGGTATCTCGTCTAAAATAAAATGTTTCATTCGGCTTAGACGCGTGACTCTAGAGTTCATACGGCATACTTAGGTTACTATGACAGCTTGCGCGAGTTTTAGTAAAGCTTAGCCTGGTAACGTGTGTCCAGAGTTCTTTGACCTAGTGGAGCGCTTACAGGTAATAACATCGGCCATGCACCGAACGCCCATGGTACGTACGGTATATCTGTGGTACGGATGCATAGGCTTCAGACCCAGTATACTTCCTATTACGGTCAACACCGTATGTGGAATGCAAACGTAAGCGTCTGAACATCAAACGCCTTGGCCTATCGGCTAGCGCGGGAGGATGATCTGACTGTGGAGGCAAAGTGTAGAAAGAATTGTACAAGGGTTAAGG") == 'CCTTAACCCTTGTACAATTCTTTCTACACTTTGCCTCCACAGTCAGATCATCCTCCCGCGCTAGCCGATAGGCCAAGGCGTTTGATGTTCAGACGCTTACGTTTGCATTCCACATACGGTGTTGACCGTAATAGGAAGTATACTGGGTCTGAAGCCTATGCATCCGTACCACAGATATACCGTACGTACCATGGGCGTTCGGTGCATGGCCGATGTTATTACCTGTAAGCGCTCCACTAGGTCAAAGAACTCTGGACACACGTTACCAGGCTAAGCTTTACTAAAACTCGCGCAAGCTGTCATAGTAACCTAAGTATGCCGTATGAACTCTAGAGTCACGCGTCTAAGCCGAATGAAACATTTTATTTTAGACGAGATACCGAATTCTTGTGCGTGCCGATTCCGTTTTATAACCATAGATATAGGTAGGTAACCTTGAAGGAGTAGTTTCGTGTCACAGGGCCTGCGCGATCCTAATTGAAACTCTGTTCTCAAAGCCGGCGTCCCTTCCCAGGCAACTCGAGAGCCCCTACCCAGTAACCATATAACCTGCCCTTCGTTATCGAAGCATAAAACCCACCAGACTGGGGGCAAGGAGATTCAAGGTTTCGGAGATATAGCCACCCCGTTAATTTGATCGCGGTCATCATGGTGCGCGACTTAAGGGCGAGTTAAAGACTCTGCGAGTGCGATCTGGGGAGCATCCGAGCCCGTAGTCACTCCCTGCTACGTTCAACTGAACGTAGAACTCTCCAACTTAACGAGTACGGCTGGCTCCCATTTCGATTCTTAAATGGCTAGTCGCAGAGCGAGTCCAAAACGTTGCTCATTCACTCTTTATTGTAGACCAGAGGATCCAAGGAGGAGACGGATGACCCATTCTCACCCAGTGCTCGCGGTTTACAAGAAGTCTTTTGAACAATCCTGGCCCCTTTATGCTGCAGTTTTTTACGAAGGCTCCATCTATGCTAGGGGTGACGTTAAAAAATGAAAACACGATCGACAAGCTCACACTTTTGGTAATTGCCGTTGGCGAGCTCGTGAACGATGAACCTGGCCGCGTGGCATGCCCGAGGCTCTGACCCCGCGGTGGGACCACATCACGGTCCTCGGGACCTGAAGGGCGGCAGTCACGAGACACCAATCGAATGAGTCTGTTTTCTAACTCCAGAAAAACGATCACACGCTATAGACGTAGATCTGCGAGTGCAACGCTAACTTTTATGAGCCTTAGAGTCGTTGATATGCACAGCCGTAGTACCCGACGTAGATATTGCCCTGAATTGCGTTCCCAGTGTGCCGCTGAAAAGACCGGGGCTGTGAACAGTTTAGATGATGAATGATAACATTACTTCACTACATAGCTAGATTTAAGTCTCTTGGCTTGTTTAGTTGCCTGTACTCTTCTGGACCCAACTTTGTTTATCAATGAACGAGATTATTGTGTCAAAAGTCGAAACCATGCCGTTAACTTAAGACCTAGACAGCACGCGAATTGCTGTTAACATGGTAGTCAAGCGCCAGACAGGTCCTCACTCAATAGAGTAGCGTTACCGTTTTAACCTCTCCGCTCGGCGCTGCGTCTTTCCCAAGCGGGCCTGAACGCATTATTAGCAATCCACCCTGCGCGACGCAGTGAGTCCTTAATCTTTCACTCTCTACAATAAGCACCCGGCTCTCGAGTAGACAACGGAAATAACTTCAGCTTGGTCGTGTTCGTTGCGAGTTGTGAATCTGACTCTTACTCTAATTGTATACGTAAAAAATGTAAGCACTGCGGGGCGTGTCGAGAAGACCTTGGATCCGCCTCTCGTCATACGCAATTAGGGTACTCTGGGTGCACTGAAGAAACACGGATTCTGATATCATGTCAGGCATCCTCTTGGCCGGTCAGAATCAAGCACACTCCGAAGGCATATGCACAGTAAAACTTAGACAGTAAACGGTGCTGTCCAGTTTGGATGTGGAACCGTCTTAAGCAACGGCCTTTCTATGTATGACTAGGGTCCGAGTCCATCGGAGTAAGACGCCGGCAGTTGTAGGTGAGTAATTTTGAGGCATGATCTTCAGCAGCCTGGCAGTTTCTGATAGAAGTTCGGTTAACTGGACCGCGTCGTTCCTGCCCGGGCACGAGCGGGGAAATAGATCTTACACCATATATTACATCGTTTGCGGCTGGCGTCCAGCGTGAACTTTATCTGCTACTGTCCTACATAGAGATCTTCCTGTACATAATGTGGTATTGTGCTATCAACTGGTCTAAGGTCAACGTCACGACGGACCATTTACTGGGGACCGGTGCACGTCTAAGTAAAATAAGCTTATGTCGAAATACCTTGAGACACTATGGGTTCGTCTTAGTGCAGGACTGCGTCGATAATACCTTTTGACCTGAAGAGCTTAGCACATTTGTCTCAGATATATACCATCCGCTTGGAGAACTTATCTGTGTGAGCGCCCGACTCATCGATCAAAGGGTGCGTGGCGACTAGGTTGGCAGATATGCCATGACCGCTCGGAGTCCGGCGTGCTCTCTATCAGGCCTTGCTCTCAAGTACAACTTTCAATATGAATGTTACATTACTTCAATTGCGTTGGTCAGTCCAAGCAACTCTGACTAATTCTGGAACAACTTAAGGATTTGTTGGTGATCCTATCACGAATTCACATAAAGCCCCTAGGTAGGATACATGGTTCATTCTGGCGCGCCAGAGGCCACATGCGAGTTTTGTCGACGTAAGTCTGGACGGCAAGAATAGTGGCGACATCAGCCCTGGTGGACTCGTCGAAGGACCGGTTTAGTCTAGAAACATAGCGTAGCTAGCGCGCTGAACCGTACACCGCTGAAATGCCCCGGGTTTATTACGGCTACTATCATCAAGGTGGTAATATGGCCCGAAAACAGAGCCAAAAATAGCTCCTTACCGTCAATATGTAACGTCGCCAGTATCATAACGATATGAGAGGATTCTTAATAGTCCACCAGCTTATCCTAAGGCCCGATCGTGGAGCCTGAGACAGCTCAGAATGGAGGAAGGCCTCTATCAGCTCGAAGTCTTCGGTTTTCCACCAGACGATCCCATGCTTGGGCCGATGCACGGGTATGCAACCTGACTTCAGGGTATGTGTTTGCTGTGCCCATCGATGGGGGAGCTGACATTTTCCTGGGGCATCAGCGTTAACTTCAAGGATGCGTCTTCCCTCTCAATGTTAAAATTAATACCACCTTCCCCTTTTAACATCTACTGTGGGTAGCCTTGATTGACATAGCCCGTTGCCCAGACCTGATCACGAACGACTGTCAAAGCCGTAGGACATCCACCAGCTAAGTAACCCCGCTCCGATAGTGGGACCTTCGCGTTACGTATGGTCTTTTGGGCTCAACCCATGTCTACGGAGTACGGCCACTAGAGTGCTGTGTTGATACGTTTGACACTAGCAAGGTCATCCACCCTTCTACTTACGGCCCCCCAAGCGAGACACTTGTACATCGCACCTACCTTTTCTCCTGAAAATACGGTGGACGTTAATATTTGCCCTTAGGAGCGGGAGCACCGTAAGTGAACGTAGTAATGAGTTGTGCCTATGTTAGAATCATAGGCGAAAACGATCCGACTCTCTCATGAAAGTCGGCAATACGCGGCTATGGTGGATCTGTATGACAAAAATAAACATGAAAGCGACGCAATACGAATAGATTGCCTGCCGGTTAATTGCCCTTTGTATCACCAGATAGCCAAGCAGTATCGTAAGGATTGGCACCGAATTGTTGTGGAACCGCTGAAAAAATAACGAGCGCGGGATGATAAGTGTTGTGGTCAAACGTATGGTGAGGTGTGTGACAACCATCTGGATAGTCGGCTGGATATCGCGTCATCAAGATCTGCGTCCGTTCGAACCTAGCGTCTAGTAGCCTACGTCTGGTAACCTTAGCGAAATGTCTGACGACGTATATAAGAGAACATCCTGGATGTCTAAGGCGTTCTATTTTGACGGACCCGCCCGCCCATACATGTAGCCTTTACATACACACACAGAGGGAGTCATTTGTATACAAGGCTAGGGAGATATTGTTGAGGTCGGTTGAAGCCTAATCAACGCGAAGGTCTTACATCTATCTGCTGTTTACGAATGGGCCAGCATACATTACCGCGTCAGTAGAGCCGTCGTAGATTATAGAACGTTGTCCCACACTTCCAAGGGATCGATCATCGCATGTGTGGCATGGCGAGAGGTCGCGCCGGAAAAGTGTTTCCGTTCCAGGGCGTAAGACTGGGTTGCTGATTTTGCGTGAGTTTAACGGGTAGGATATAACTACATAGGTTGTCTGCACGTATCTGCCACATACGTCCCTGATAAGCGGCGCGTACTCTCGGCGAACTGGAATAAGTGTTACCGCGCCACCGCGCGCTGACTTTATAGACTAGGAGTAAGCCAACCCTGAGTGTAAGTAGGCATCAAGTCCTATGGCTTGCAGTCGCCTAACTGTTTATGCAACCCTTCTGACACCGGAGGCACTTAGAGACTAGCGCCTGCGCATTGTCCTCAAGAATGGTTGGTCACGCCTTGAAGGACTGTCCCGCCCATCAGGGTTCGATATGCCGACCCAGCCTTAAGGTAGGATAAACCCGATGTTAGTTACGACACAGGGAAGAGCATCGCTCAGAACAGCAAGTCACGAATACAAAAATTCATGGGAACCAGTATTAACCTGTTTGCTTCTTCGTTAGCTATGTGGGCGGACCGGTGTATGATAGTCCCCGTGGGATCCCTACTCGCCAGTCCCCATTGAGCTCAAGTTAAGACCACAACAGTCGAATTTTCTGCGATTCAAGGTTCGGGTACGAATTCCAAAATTGATCCCTCCGCTTTCATTTTATTCTAGCGCACGGTGCTACTCATTTCTGCATATTAGTCTTGAGCTCATGGCCGGCGCGTTGTACACAACGGACCACAACTGGCCCAATAGGTCTCGGGCCCGCTCCCTAGGGTTTGAACTCCATTCGACCGATGCGCCCCATGGACTCGACGTCGCGAGGATGGCCATATGACTTATACAAAGACATACTGACAGCAGCAACCTATCGCGGGAACCGTGTCCGGACCACGTACCAGTATGGCACAGTACACATTCCGGCTCAGTCAAAGGACCCCAGCTTGTGCGCCTTGTTTAGCATTGCCCTTCGACTGTTTGCAAACTTGGTCATTGTCGGACCCACTAAGAAAAGAGGTCTGAAAGTCGCACAATTATTGTATTCGTTAGACGCCACTTTCACTGCAGATATCCGTTAGGGGGTGTGGACACAATGTGTCTAGTTGGAATTGCGGGTAACGGAACTCCTCGGATCAATATAGCGTGAGCGTATGTGCCAAACAGCGGTAGTTTGCCACGTGGACAAGAATTGAGCCGCAGCTTTACTAAGCTAGATTTGAGGTTATCAACTTCACGGTGCAACTGCCTTAACCACACTCAGGACATGGAGTCGCGAAGAACCTCTCTACCACCATTGAACTTGCCAATACGCTCTAAACTTTCGAGGCACACTGTCTGTCATTGTTTGCATTCGGTGACCATTTGCCCGTTCTTCAGCCCGAGGTTAGGTCTAAGGCAGAACACTAGCGCCCGGCGCGCAGGATCAAACGTCTGCGACAATGCGTAGTGCACCACGAGCTTTACTCGGCGTTCCGATTCTAAGTGGAGGTGACACTCCCTACGATCCTTTTGGCGCTTTGTAAGCGCGCAGTGATACCATGTGAGCGCCAGCTACAAGTCACCAAACTGGCGGTTAAAATCAACATGACCCCCGGGGCTCGTGGTCAGTGACTGGATCTTAAACCAGGGTTGACTCCTGACAAGAACAGTCTCTCTCCATAATCTCTAGTAGGAGAAGGTATAAATTGAATTTTGTCAGACGAAGCGCGTGTCCGGACCTTCAGGATGGCCCATCCCTCATGCTGCCACTAGTGATGCTGCAAACCCGGAGGCATCTCACTAAGACAGCCATTAGCGGATAGAATAATTCCATGTTTTTAAGCGGGTGTGGTGCCGACGAATCGTGGTCGCCTACTTAATCCGCGATTACGGGGGACATCTGGCCGAACTGGATGAGGATGTTCCTAAACAACGGCGCGCAAAGCTGCCGTAGATTTTTAGTAATCACAACCTTGCCACACCAGAAGCCGCATCTGCAAAGTACAATATATCGCCCCCAGAACCGTTACCAATAGGTCGTCATGTCTCGTTACAGAGTGACCATACTAGTTTGGCGATCGCGATAGCTGATAACCAAACTAATCGACTAGTGTACATCGTCGCGATGTCCTCATGAGCTGAGAATAGAAGAGCCGTTTCATGTCATACCGCCTAAATCCGCGAATCACACTTAAGTAACACCTGCCATCTCATTTTATAATAGATGCTTGCCGGGCATATTTTGGGCCAGCTAGGTGATTATGTACTGCACCCTGCTGGGACGCGAGCAGACTCATCAGCATGGAGATAAAAAGATATCTGAGGGCCAAGCAGCGCAGTCGTTCATCAAATGGACCTAAAGAGAGCAGTTCTATACAATGGCCCCGCTCATGCAAACCAAGACTAATACACCGGACTGTTATCCGTGAATATGGGGGCACAAGTTCCCCCCCGCGTCAGCGAGATTGTATTAACGCTTTGACAACATGTAGAAACCGCCAACGGCCCCCGTTGTCGCCTATCAGCGATTCGAGAGCGTGCTCCGTGCAAAGGTAGTCCGAAACAACCGGAGGTTGAACGCAAAAATACACGCTCCTTCAGGTTTCACCATGTCGGGAGGAGTCACGTTCGAAAGGCTTGCCACACTCAGATCAAGCTGTGCTATATCTTCAAGCATATGTCGCGCCTCAAACTAACGCGACTTGGATAGGTTATGAACAGCGTAGAATACACTGTGTTTCATCTTTATATCATGTATCGTAGATGTGTTTCCTTCGTAGATAAATAGGCTGAAGAGGTTAATGCCTCGCACGTTTCGTTCTCTGGTTGATGCCCAAAGATCGAAGCTTGCATAGAGCTATGTCACACGGCCGGAGAAAGTTGCGTTATGCCAAGTGGGTGCTGTCGACGCCCATTAAGGACCCCCCCTATGAGCGGTCTACGTATTGGAATGAGATGACCAATTAACTGTCCCCATCACAGTGCAACTACATCCGATCTGAAGGCACGAAGTCTTCGAGGCAGGATATATCTCACCTTGGATTGAAGATTCTGGGATTGAACACCAGCGTCTGCGTCCTCGCGGCGCCGCGCCGCCCTAAGGCTAGATTGAAGAAGCTTAGTAGCCCGCTTTGCTGCAGTAACTTTATTTGACCGAATTACCGGACAATGCTTTTTGGCTCAGCTGGACGTAAGTGACTACCAACTCGGTCTCGCAGCAGATTATTCTTTCAGCATTCATCCCCTGATTGGTACACTGGGTGAATGTGAAGTTGTGAAAGTCACGACCCTAGTTCCTTTTTGGTATCAGTTACCTCCCATTGAAAAAATGAACGGTTCTACTGCAGAATCAGAACTGAACAACCGCGAAGCTGATACGAGATCATTGCGTTCCGACCAGGTGCACCATGATTCCCCTTGGGATCGAAATTGATACGCGTAACATATCATTATATACTATTAGCTAGGGGTAGCCAATGATAGCTGTTGTCCGAAGAAATGACTGTTAAGATATTGCTAATTGATTTCGCTTATCTCTCCCAATTGCCGGCGTGCCGTCAGCTGGTTTCGTGTGGAGTTGCTAATTCCGGGGGGTATATTGAATTTAATGAAAGTAGTTCACTGAGGTGAGTTGCCTATTAGTAACGAGATATAGCGAGTAGTTTAATTTCGAGAGACGACTCGCGTCTGTGGGGCGATCTTGTTTATTCAGGCATCGAAAGGTACGTCAAAACGCACCTCTAAGTTGTATTCAGTTCACGATGTTGCGTGCTGCGCCGAACCTGGCGCCAACTAACTGTTGTGTAGGACGCTGCAACCCCCGTTTTCATACATGATCGGTCTGTTATACGTAAGTGATGCGTGCAGGCGAGTATCTTCGCGTTTGTATCGGTACCACATCGACCTGCACGCCATCCTACGGACGCTATTTTGCTTCACTAAGTTTCGTCAAATTGATAATCTCATAGAAAGTAAAGACCTCACAAATTCTAGGGTCATCACACCGTTCTACGCCGCCCACGATCGGTTCTTTCCGCAAGGGCCTGATGTGGAGTACCAGCGGTAAAATTATCGAAACGGACAGACCGACTCTGATCTGGAAAAGGTCTTGACATGAGGCGGTTTTGGTTGCGCCTTTTAAGCGTACTTCTAGGGACCTGTCAGGGCTCTAAAGTGGGTGCAATTTGACCCCGATACGGATCCCAGGCGTAACTAAGTACCATCCGTCTAAGCCCTTGTTATCCCGATCAGTGCCACGTTGCTTATCACGGTTATTAAGGACGTAGCAGCATTGTCGCATAGCACAGTAGTTAACGATGTGCCCAATCAATGATGTTCGCCGATGGATGACCTACTCCTCGTTAGGAGCAAGCAGTGTCTACCCAGCAGTCAACGCGCGAGCTGATGGTAACTGGGCCTTCGCGTTCTATTGCATACGGAGTCCTAGAGCTAGTCCGAGCTGACTTGACACAATTCCTGCCTCCAAGGCTTGAGACGATTTGTCAATCCGCTAATCCAACGGTAGCGGTTAGCTATGTCATCCCATGCGACATGGCACAACACCACGGATATACTTGCACCGCGGTCCGATGTGAAACCCAAGCCTCTGCGTGATCGTAAAACACAGATCTAGTAAATATGTCCAAACTCATCTAGCGACGTAGAGACACGGCCGAAATGTCATCACGTGTGAGGTCTGACAGGATACTTGGGGGCTCTATGACCCCGACTAAAAAATGGCTGTCACAGGCTAGCCAGCGCATTTAAAACTGCCCTCTGGAGGCGCGCAGGCCGGGGATGCCATCATCCTTCATGCATAACTCACAGAGGGAGAGATAGTCGTGAGGACATACTGCTCTGGGGTCAGAGGTCGCTCTTGAAAGACCCTGTACATGGCCAGGGCCTTATGGCTCGCTTTGCGTCGCGCAGTCTCGGTCGGCTGCTGGGTGCCTCAATGCACAAACTATGGAATGTTGGTACTGGGGTTTACTGTCTTCACAAACAGTCGTATGTACATGGCGATGCTCCCACGGATCACCGCCTCAGCAGATAAGATTACAATTATGCGGCAACCAGGGCGCCCCTTGCAATAAAGCTCACCATCATTTGAAGGATCCATTCGGTGTTGCCCTAAGTCAAATCCTCGTCCTTGCGTGCGAAGACTTTCCAAGCGCAAATTTCGAGAGACACTCCGGCGTCACCACTCTCTT'
