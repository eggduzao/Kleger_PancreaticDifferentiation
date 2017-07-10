
# Import
import os
import sys
from glob import glob

# Parameters
outLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/exp_mat/background/"

# Iterating on peak files
peakList = ["dnase", "faire", "h3k4me1", "hnf6", "promoters"]
for peakName in peakList:

  if(peakName == "promoters"): loc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/"
  else: loc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/ngs_data/"

  # Iterting on down / up condition
  enList = ["up", "down"]
  for en in enList:

    inFileName = outLoc+peakName+"_"+en+".txt"
    inFile = open(inFileName,"w")
    inFile.write("\t".join(["name","type","file"])+"\n")

    # Iterating on conditions
    condList = ["DE_Day0_hetvsWT", "DE_Day10_hetvsWT", "DE_Day14_hetvsWT"]
    for cond in condList:

      # Iterating on ext list
      promExtList = ["250","500","1000"]
      for pExt in promExtList:
        
        name = cond+"_ev_"+pExt
        fName = loc+peakName+"/"+en+"/"+name+".bed"
        inFile.write("\t".join([name,"regions",fName])+"\n")

    inFile.close()


