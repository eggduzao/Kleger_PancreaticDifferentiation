
# Import
import os
import sys
from glob import glob

# Parameters
geneLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/genes/"
peakLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/ngs_data/"
outLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/exp_mat/random_withEnhancer_background/"

# Iterating on peak files
peakList = ["dnase", "faire", "h3k4me1", "hnf6"]
for peakName in peakList:

  # Matching matrices
  inFileName = outLoc+"matching/"+peakName+".txt"
  inFile = open(inFileName,"w")
  inFile.write("\t".join(["name","type","file"])+"\n")
  peakFileName = glob(peakLoc+peakName+"/*_format.bed")[0]
  inFile.write("\t".join([peakName,"regions",peakFileName])+"\n")
  inFile.close()  

  # Iterting on down / up condition
  enList = ["up", "down"]
  for en in enList:

    # Iterating on conditions
    condList = ["DE_Day0_hetvsWT", "DE_Day10_hetvsWT", "DE_Day14_hetvsWT"]
    for cond in condList:

        ol = outLoc+"enrichment/"+peakName+"_"+en+"/"
        os.system("mkdir -p "+ol)
        inFileName = ol+cond+".txt"
        inFile = open(inFileName,"w")
        inFile.write("\t".join(["name","type","file","genegroup"])+"\n")
        inFile.write("\t".join([peakName,"regions",peakFileName,cond])+"\n") 
        geneFileName = geneLoc+en+"/"+cond+"_ev_mygenelist.txt"
        inFile.write("\t".join([cond,"genes",geneFileName,cond])+"\n")
        inFile.close()


