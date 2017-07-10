
# Import
import os
import sys
from glob import glob

# Parameters
rootLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/"
inLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/results_match/"
outLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/results_enrich/nev/"
csFileName = "/hpcwork/izkf/projects/TfbsPrediction/Data/HG19/hg19.chrom.sizes.filtered.increased.10e6.ForBw"

# Iterating on peak files
peakList = ["dnase", "faire", "h3k4me1", "hnf6", "promoters"]
for peakName in peakList:

  if(peakName == "promoters"): origLoc = rootLoc+peakName+"/"
  else: origLoc = rootLoc+"ngs_data/"+peakName+"/"

  # Iterting on down / up condition
  enList = ["up", "down"]
  for en in enList:

    # Iterating on conditions
    condList = ["DE_Day0_hetvsWT", "DE_Day10_hetvsWT", "DE_Day14_hetvsWT"]
    for cond in condList:

      # Iterating on ext list
      promExtList = ["250","500","1000"]
      for pExt in promExtList:

        ol = outLoc+peakName+"/"+en+"/"+cond+"_"+pExt+"/Match/"
        os.system("mkdir -p "+ol)
        
        evFileName = inLoc+peakName+"_"+en+"/Match/"+cond+"_ev_"+pExt+"_mpbs.bb"
        nevFileName = inLoc+peakName+"_"+en+"/Match/"+cond+"_nev_"+pExt+"_mpbs.bb"
        os.system("cp "+evFileName+" "+ol)
        os.system("cp "+nevFileName+" "+ol+"random_regions_mpbs.bb")

        origNevFileName = origLoc+en+"/"+cond+"_nev_"+pExt+".bed"
        origNevFileNameT = origLoc+en+"/"+cond+"_nev_"+pExt+".bedT"
        os.system("sort -k1,1 -k2,2n "+origNevFileName+" | grep -E -v 'random|chrY|chrM|ctg|hap|chrUn' | cut -f 1,2,3 > "+origNevFileNameT)
        os.system("bedToBigBed "+origNevFileNameT+" "+csFileName+" "+ol+"random_regions.bb -verbose=0")
        os.system("rm "+origNevFileNameT)


