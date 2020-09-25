#!/usr/bin/python3

import re
import sys
import getopt

def get_seq(path):
	seq = []
	with open(path, 'r') as f1:
		seq = f1.readlines()
	for i in range(0, len(seq)):
		seq[i] = seq[i].rstrip('\n')
	return(seq)

def get_length(generator):
    if hasattr(generator,"__len__"):
        return len(generator)
    else:
        return sum(1 for _ in generator)

def get_cgcc_position(string):
	cG_cC_score = 0
	# Get the max G-run
	matches = re.finditer(r"(G{1,})", str(string), flags=re.IGNORECASE)
	max_len = 0
	for match in matches:
		if len(match.group(1)) > max_len:
			max_len = len(match.group(1))

	cG_score = 0

	for i in range(max_len):
		mes = re.finditer(r"(?=(G{" + str(i+1) + "," + str(i+1) + "}))", str(string), flags=re.IGNORECASE)
		cG_score += (i+1)*10*get_length(mes)

	# Get the max C-run
	matches = re.finditer(r"(C{1,})", str(string), flags=re.IGNORECASE)
	max_len = 0
	for match in matches:
		if len(match.group(1)) > max_len:
			max_len = len(match.group(1))

	cC_score = 0

	for i in range(max_len):
		mes = re.finditer(r"(?=(C{" + str(i+1) + "," + str(i+1) + "}))", str(string), flags=re.IGNORECASE)
		cC_score += (i+1)*10*get_length(mes)

	cG_cC_score = ((cG_score/cC_score) if (cC_score > 0) else cG_score)
	return(cG_cC_score)

def main(argv):
	infile = ''
	outfile = ''
	try:
		opts, args = getopt.getopt(argv,"i:o:h",["ifile=","ofile="])
	except getopt.GetoptError:
		print('cGcC.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('cGcC.py -i <inputfile> -o <outputfile>')
			sys.exit()
		elif opt in ("-i", "--ifile"):
			infile = arg
		elif opt in ("-o", "--ofile"):
			outfile = arg
	seq = get_seq(infile)
	out_open = open(outfile, 'a')
	for i in range(0, len(seq)):
		out_open.write(seq[i] + "\t" + str(get_cgcc_position(seq[i])) + "\n")
	out_open.close()

if __name__ == '__main__':
	main(sys.argv[1:])