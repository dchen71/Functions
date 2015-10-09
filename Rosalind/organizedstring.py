#Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
#Return: All strings of length n that can be formed from the alphabet, ordered lexicographically.

import itertools

def organizedstring(string, length):
	#break down string and remove the spaces between char
	nucleotides = string.replace(" ", "")
	answer = []

	#pool = tuple(nucleotides) #tuples are immutable list, required if going yield route
	n = len(nucleotides)
	r = length
	for indices in itertools.product(range(n), repeat = r): #product(size of list, length of returned product)
		kmer = ""
		for i in indices: #uses the indicecs to build the kmer to add to answer
			kmer += nucleotides[i]
		answer.append(kmer)

	for i in answer: #prints each answer out
		print(i)

	return answer #returns the array in case


sample = "E N O F C V D L"
k = 3
assert(organizedstring(sample,k)) == ['EEE', 'EEN', 'EEO', 'EEF', 'EEC', 'EEV', 'EED', 'EEL', 'ENE', 'ENN', 'ENO', 'ENF', 'ENC', 'ENV', 'END', 'ENL', 'EOE', 'EON', 'EOO', 'EOF', 'EOC', 'EOV', 'EOD', 'EOL', 'EFE', 'EFN', 'EFO', 'EFF', 'EFC', 'EFV', 'EFD', 'EFL', 'ECE', 'ECN', 'ECO', 'ECF', 'ECC', 'ECV', 'ECD', 'ECL', 'EVE', 'EVN', 'EVO', 'EVF', 'EVC', 'EVV', 'EVD', 'EVL', 'EDE', 'EDN', 'EDO', 'EDF', 'EDC', 'EDV', 'EDD', 'EDL', 'ELE', 'ELN', 'ELO', 'ELF', 'ELC', 'ELV', 'ELD', 'ELL', 'NEE', 'NEN', 'NEO', 'NEF', 'NEC', 'NEV', 'NED', 'NEL', 'NNE', 'NNN', 'NNO', 'NNF', 'NNC', 'NNV', 'NND', 'NNL', 'NOE', 'NON', 'NOO', 'NOF', 'NOC', 'NOV', 'NOD', 'NOL', 'NFE', 'NFN', 'NFO', 'NFF', 'NFC', 'NFV', 'NFD', 'NFL', 'NCE', 'NCN', 'NCO', 'NCF', 'NCC', 'NCV', 'NCD', 'NCL', 'NVE', 'NVN', 'NVO', 'NVF', 'NVC', 'NVV', 'NVD', 'NVL', 'NDE', 'NDN', 'NDO', 'NDF', 'NDC', 'NDV', 'NDD', 'NDL', 'NLE', 'NLN', 'NLO', 'NLF', 'NLC', 'NLV', 'NLD', 'NLL', 'OEE', 'OEN', 'OEO', 'OEF', 'OEC', 'OEV', 'OED', 'OEL', 'ONE', 'ONN', 'ONO', 'ONF', 'ONC', 'ONV', 'OND', 'ONL', 'OOE', 'OON', 'OOO', 'OOF', 'OOC', 'OOV', 'OOD', 'OOL', 'OFE', 'OFN', 'OFO', 'OFF', 'OFC', 'OFV', 'OFD', 'OFL', 'OCE', 'OCN', 'OCO', 'OCF', 'OCC', 'OCV', 'OCD', 'OCL', 'OVE', 'OVN', 'OVO', 'OVF', 'OVC', 'OVV', 'OVD', 'OVL', 'ODE', 'ODN', 'ODO', 'ODF', 'ODC', 'ODV', 'ODD', 'ODL', 'OLE', 'OLN', 'OLO', 'OLF', 'OLC', 'OLV', 'OLD', 'OLL', 'FEE', 'FEN', 'FEO', 'FEF', 'FEC', 'FEV', 'FED', 'FEL', 'FNE', 'FNN', 'FNO', 'FNF', 'FNC', 'FNV', 'FND', 'FNL', 'FOE', 'FON', 'FOO', 'FOF', 'FOC', 'FOV', 'FOD', 'FOL', 'FFE', 'FFN', 'FFO', 'FFF', 'FFC', 'FFV', 'FFD', 'FFL', 'FCE', 'FCN', 'FCO', 'FCF', 'FCC', 'FCV', 'FCD', 'FCL', 'FVE', 'FVN', 'FVO', 'FVF', 'FVC', 'FVV', 'FVD', 'FVL', 'FDE', 'FDN', 'FDO', 'FDF', 'FDC', 'FDV', 'FDD', 'FDL', 'FLE', 'FLN', 'FLO', 'FLF', 'FLC', 'FLV', 'FLD', 'FLL', 'CEE', 'CEN', 'CEO', 'CEF', 'CEC', 'CEV', 'CED', 'CEL', 'CNE', 'CNN', 'CNO', 'CNF', 'CNC', 'CNV', 'CND', 'CNL', 'COE', 'CON', 'COO', 'COF', 'COC', 'COV', 'COD', 'COL', 'CFE', 'CFN', 'CFO', 'CFF', 'CFC', 'CFV', 'CFD', 'CFL', 'CCE', 'CCN', 'CCO', 'CCF', 'CCC', 'CCV', 'CCD', 'CCL', 'CVE', 'CVN', 'CVO', 'CVF', 'CVC', 'CVV', 'CVD', 'CVL', 'CDE', 'CDN', 'CDO', 'CDF', 'CDC', 'CDV', 'CDD', 'CDL', 'CLE', 'CLN', 'CLO', 'CLF', 'CLC', 'CLV', 'CLD', 'CLL', 'VEE', 'VEN', 'VEO', 'VEF', 'VEC', 'VEV', 'VED', 'VEL', 'VNE', 'VNN', 'VNO', 'VNF', 'VNC', 'VNV', 'VND', 'VNL', 'VOE', 'VON', 'VOO', 'VOF', 'VOC', 'VOV', 'VOD', 'VOL', 'VFE', 'VFN', 'VFO', 'VFF', 'VFC', 'VFV', 'VFD', 'VFL', 'VCE', 'VCN', 'VCO', 'VCF', 'VCC', 'VCV', 'VCD', 'VCL', 'VVE', 'VVN', 'VVO', 'VVF', 'VVC', 'VVV', 'VVD', 'VVL', 'VDE', 'VDN', 'VDO', 'VDF', 'VDC', 'VDV', 'VDD', 'VDL', 'VLE', 'VLN', 'VLO', 'VLF', 'VLC', 'VLV', 'VLD', 'VLL', 'DEE', 'DEN', 'DEO', 'DEF', 'DEC', 'DEV', 'DED', 'DEL', 'DNE', 'DNN', 'DNO', 'DNF', 'DNC', 'DNV', 'DND', 'DNL', 'DOE', 'DON', 'DOO', 'DOF', 'DOC', 'DOV', 'DOD', 'DOL', 'DFE', 'DFN', 'DFO', 'DFF', 'DFC', 'DFV', 'DFD', 'DFL', 'DCE', 'DCN', 'DCO', 'DCF', 'DCC', 'DCV', 'DCD', 'DCL', 'DVE', 'DVN', 'DVO', 'DVF', 'DVC', 'DVV', 'DVD', 'DVL', 'DDE', 'DDN', 'DDO', 'DDF', 'DDC', 'DDV', 'DDD', 'DDL', 'DLE', 'DLN', 'DLO', 'DLF', 'DLC', 'DLV', 'DLD', 'DLL', 'LEE', 'LEN', 'LEO', 'LEF', 'LEC', 'LEV', 'LED', 'LEL', 'LNE', 'LNN', 'LNO', 'LNF', 'LNC', 'LNV', 'LND', 'LNL', 'LOE', 'LON', 'LOO', 'LOF', 'LOC', 'LOV', 'LOD', 'LOL', 'LFE', 'LFN', 'LFO', 'LFF', 'LFC', 'LFV', 'LFD', 'LFL', 'LCE', 'LCN', 'LCO', 'LCF', 'LCC', 'LCV', 'LCD', 'LCL', 'LVE', 'LVN', 'LVO', 'LVF', 'LVC', 'LVV', 'LVD', 'LVL', 'LDE', 'LDN', 'LDO', 'LDF', 'LDC', 'LDV', 'LDD', 'LDL', 'LLE', 'LLN', 'LLO', 'LLF', 'LLC', 'LLV', 'LLD', 'LLL']