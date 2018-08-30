#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Copyright (c) 2018 - SUN Lei <leisun@genetics.ac.cn> 

"""
Translate nucleic_acids to 6 frame proteins from a fasta file with one sequence.
"""

INPUT = r'C:\Users\SUN\Desktop\test.fasta'
OUTPUT = r'C:\Users\SUN\Desktop\test_6_frameprotein.fasta'

import re

Standard_Code = {
'TTT':'F', 'TCT':'S', 'TAT':'Y', 'TGT':'C',  
'TTC':'F', 'TCC':'S', 'TAC':'Y', 'TGC':'C',  
'TTA':'L', 'TCA':'S', 'TAA':'*', 'TGA':'*',  
'TTG':'L', 'TCG':'S', 'TAG':'*', 'TGG':'W',  

'CTT':'L', 'CCT':'P', 'CAT':'H', 'CGT':'R',  
'CTC':'L', 'CCC':'P', 'CAC':'H', 'CGC':'R',  
'CTA':'L', 'CCA':'P', 'CAA':'Q', 'CGA':'R',  
'CTG':'L', 'CCG':'P', 'CAG':'Q', 'CGG':'R',  

'ATT':'I', 'ACT':'T', 'AAT':'N', 'AGT':'S',  
'ATC':'I', 'ACC':'T', 'AAC':'N', 'AGC':'S',  
'ATA':'I', 'ACA':'T', 'AAA':'K', 'AGA':'R',  
'ATG':'M', 'ACG':'T', 'AAG':'K', 'AGG':'R',  

'GTT':'V', 'GCT':'A', 'GAT':'D', 'GGT':'G',  
'GTC':'V', 'GCC':'A', 'GAC':'D', 'GGC':'G',  
'GTA':'V', 'GCA':'A', 'GAA':'E', 'GGA':'G',  
'GTG':'V', 'GCG':'A', 'GAG':'E', 'GGG':'G',


}
# Vertebrate, Yeast, Bacterial, Archaeal, Plant Nuclear, and Plant Mitochondrial, Plastid Code(transl_table=1)

def nucleic_acids_in_one_line(file):
    nucleic_acids = ''
    for line in open(file):
        if line.startswith('>'):
            name = re.sub('>', '', line.strip())
        if not line.startswith('>'): 
            nucleic_acids = nucleic_acids + line.strip()
    return name,nucleic_acids
# read the nucleic acids sequence into a single string

def translate_to_3_frame(nucleic_acids,name,strand,codon_table):
    frame_protein = [
    ["", ""],
    ["", ""],
    ["", ""],
    ]
    for frame in range(3):
        protein = '' 
        frame_out = name + ' ' + strand + str(frame + 1)
        frame_protein[frame][0] = str(frame_out)
        for i in range(frame, len(nucleic_acids), 3):
            codon = nucleic_acids[i:i + 3]
            if codon in codon_table:
                protein = protein + codon_table[codon]
            else:
                protein = protein + '-'
            
        frame_protein[frame][1] = protein
    return frame_protein
# translate one frame at a time

def format_to_blocks(frame,protein):
    i = 0
    protein_out = ''
    protein_out = '>' + frame + '\n'
    while i < len(protein):
        protein_out = protein_out + protein[i:i + 60] + '\n'
        i = i + 60
    return protein_out
# format to blocks of 60 columns

def reverse(squence):
    squence = str(squence)
    return squence[::-1]
# reverse a squence

def to_DNA(squence):
    squence = re.sub('U', 'T', squence)
    squence = re.sub('u', 'T', squence)
    squence = re.sub('t', 'T', squence)
    squence = re.sub('c', 'C', squence)
    squence = re.sub('a', 'A', squence)
    squence = re.sub('g', 'G', squence)
    squence = re.sub('n', 'N', squence)
    return squence
# format to DNA

file = INPUT
f = open(OUTPUT, 'w')
name,nucleic_acids = nucleic_acids_in_one_line(file)
nucleic_acids = to_DNA(nucleic_acids)
nucleic_acids_reverse = reverse(nucleic_acids)
frame_protein = translate_to_3_frame(nucleic_acids,name,'+',Standard_Code)
for i in range(3):
    frame = frame_protein[i][0]
    protein = frame_protein[i][1]
    protein_out = format_to_blocks(frame,protein)
    f.write(protein_out)
frame_protein = translate_to_3_frame(nucleic_acids_reverse,name,'-',Standard_Code)
for i in range(3):
    frame = frame_protein[i][0]
    protein = frame_protein[i][1]
    protein_out = format_to_blocks(frame,protein)
    f.write(protein_out)
f.close()