#!/usr/bin/python

import sys
from Bio import SeqIO
import pandas as pd
from optparse import OptionParser


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# defining the arguments which can be passed to the script

arguments = OptionParser()

arguments.add_option('-t', '--table', dest='table', help='table file from NCRF')
arguments.add_option('-n','--num', dest='num', help='cut size')
arguments.add_option('-f', '--fasta', dest='fasta', help='fasta file')


(options, args) = arguments.parse_args() 
if options.table is None or options.num is None or options.fasta is None: # if one of the arguments is not provided
	print('\n-----> A mandatory option is missing! <-----\n') #Error message
	arguments.print_help() #Print Help
	exit(-1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


data = pd.read_csv(options.table, sep='\t') #Open table with pandas 

seq_dic = {} #create a dictionary

g_data = SeqIO.parse(open(options.fasta),'fasta') #open fasta file
for g in g_data:
	seq_dic[str(g.id)] = str(g.seq) #add seq and reads name in dictionary

outp_list = []

count = 0 
seq = 0	
for i in data['seq']:
	count += 1
	for j,k in seq_dic.items():
		if i == j:
			start = int(data['start'][count-1]) - int(options.num)
			end = int(data['end'][count-1]) + int(options.num)
			if start < 0:
				start =0
			if end > len(k):
				end = len(k)
			start_seq = k[start:data['start'][count-1]]
			end_seq = k[data['end'][count-1]:end]
			outp = open(str(options.fasta.replace('.fasta',''))+"_out.fasta",'w')
			outp_list.append('>'+j+'\n' +str(start_seq)+'r'+str(end_seq)+'\n')
			seq += 1

#writing results
for i in outp_list:
	outp.write(i)

print("\n It's Done....\n")					

