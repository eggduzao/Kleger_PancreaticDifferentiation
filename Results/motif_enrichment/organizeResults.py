
# Import
import os
import sys
from glob import glob

# Parameters
backLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/results_enrich/background/"
nevLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/results_enrich/nev/"
outLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/results_organized/"

# Iterating on peak files
peakList = ["dnase", "faire", "h3k4me1", "hnf6", "promoters"]
for peakName in peakList:

  # Iterting on down / up condition
  enList = ["up", "down"]
  for en in enList:

    # Iterating on conditions
    condList = ["DE_Day0_hetvsWT", "DE_Day10_hetvsWT", "DE_Day14_hetvsWT"]
    for cond in condList:

      # Iterating on ext list
      if(peakName == "promoters"): promExtList = ["250","500","1000"]
      else: promExtList = ["1000"]
      for pExt in promExtList:

        currBackLoc = backLoc+peakName+"_"+en+"/"+cond+"_ev_"+pExt+"/"
        newBackLoc = outLoc+"random_background/"+peakName+"_"+en+"/"+cond+"_"+pExt+"/"
        os.system("mkdir -p "+newBackLoc)
        os.system("cp "+currBackLoc+"*.html "+currBackLoc+"*.txt "+newBackLoc)

        if(peakName == "hnf6"): os.system("cp "+currBackLoc+"*.bb "+newBackLoc)

        currNevLoc = nevLoc+peakName+"/"+en+"/"+cond+"_"+pExt+"/"+cond+"_ev_"+pExt+"/"
        newNevLoc = outLoc+"nev_background/"+peakName+"_"+en+"/"+cond+"_"+pExt+"/"
        os.system("mkdir -p "+newNevLoc)
        os.system("cp "+currNevLoc+"*.html "+currNevLoc+"*.txt "+newNevLoc)


        


