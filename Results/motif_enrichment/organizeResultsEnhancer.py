
# Import
import os
import sys
from glob import glob

# Parameters
backLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/results_enrich/with_enhancer/"
outLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/results_organized/random_background_enhancer/"

# Iterating on peak files
peakList = ["dnase", "faire", "h3k4me1", "hnf6"]
for peakName in peakList:

  # Iterting on down / up condition
  enList = ["up", "down"]
  for en in enList:

    # Iterating on conditions
    condList = ["DE_Day0_hetvsWT", "DE_Day10_hetvsWT", "DE_Day14_hetvsWT"]
    for cond in condList:

      currBackLoc = backLoc+peakName+"_"+en+"/"+cond+"/"+peakName+"__"+cond+"/"
      newBackLoc = outLoc+peakName+"_"+en+"/"+cond+"/"
      os.system("mkdir -p "+newBackLoc)
      os.system("cp "+currBackLoc+"randtest_statistics.html "+currBackLoc+"randtest_statistics.txt "+currBackLoc+"mpbs_ev.bb "+newBackLoc)


