
# Import
import sys
from Bio import motifs

# Reading input
inputLoc = "./"
outputLoc = "./"
inList = ["HNF6_Hocomoco_M00149","HNF6_homer_motif101","HNF6_MEME_liver1","HNF6_MEME_liver2","HNF6_MEME_pancreas1","HNF6_MEME_pancreas3"]

# Execution
for inFileName in inList:
  inFile = open(inputLoc+inFileName+".pwm","r")
  outFileName = outputLoc+inFileName+".png"
  pwm = motifs.read(inFile, "pfm")
  pwm.weblogo(outFileName, format="png_print", stack_width = "medium", color_scheme = "color_classic")
  inFile.close()


