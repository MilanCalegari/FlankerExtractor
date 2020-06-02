# FlankerExtractor

This script receives a NoiseCancellingRepeatFinder output table and extracts the flanker region from the region of interest

## Pre-Requisite
Biopython
Pandas

## Usage
>flanker_extractor.py -t [NCRF output] -f [fasta file] -n [num of reads to cut for each side]
