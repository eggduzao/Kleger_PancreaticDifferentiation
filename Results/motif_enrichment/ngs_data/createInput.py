
# Import
import os
import sys
from glob import glob

# Parameters
peakHalfExt = 50
inLoc = "/home/egg/Projects/PancreaticDifferentiation/Results/motif_enrichment/genes/"
promLoc = "/home/egg/Projects/PancreaticDifferentiation/Results/motif_enrichment/promoters/"
outLoc = "/home/egg/Projects/PancreaticDifferentiation/Results/motif_enrichment/ngs_data/"

# Iterating on peak files
peakLoc = "/home/egg/Projects/PancreaticDifferentiation/Results/motif_enrichment/ngs_data/"
peakList = ["dnase/Pancreatic_isletsDukeDNaseSeq", "faire/Pancreatic_isletsUncFAIREseq", "h3k4me1/PP2_H3K4me1_1", "hnf6/PP2_Hnf6_summits_10"]
for peakName in peakList:

  # Initialization
  peakFileName = peakLoc+peakName+".bed"
  folderName = peakName.split("/")[0]
  to_remove = []  

  # Extract from summits
  if(peakName == "hnf6/PP2_Hnf6_summits_10"):
    newPeakFileName = peakLoc+peakName+".bedT"
    to_remove.append(peakLoc+peakName+".bedT")
    peakFile = open(peakFileName,"r")
    newPeakFile = open(newPeakFileName,"w")
    for line in peakFile:
      ll = line.strip().split("\t")
      mid = (int(ll[1]) + int(ll[2])) / 2
      p1 = str(mid-peakHalfExt); p2 = str(mid+peakHalfExt)
      newPeakFile.write("\t".join([ll[0],p1,p2])+"\n")
    peakFile.close()
    newPeakFile.close()
    peakFileName = newPeakFileName

  # Iterting on down / up condition
  enList = ["up", "down"]
  for en in enList:

    # Iterating on conditions
    condList = ["DE_Day0_hetvsWT", "DE_Day10_hetvsWT", "DE_Day14_hetvsWT"]
    for cond in condList:

      # Iterating on ext list
      promExtList = ["250","500","1000"]
      for pExt in promExtList:

        # Files
        evFileName = inLoc+en+"/"+cond+"_ev.bed"
        nevFileName = inLoc+en+"/"+cond+"_nev.bed"
        promEvFileName = promLoc+en+"/"+cond+"_ev_"+pExt+".bed"
        promNevFileName = promLoc+en+"/"+cond+"_nev_"+pExt+".bed"
        evMgd = promLoc+en+"/"+cond+"_ev_"+pExt+"M.bed"
        nevMgd = promLoc+en+"/"+cond+"_nev_"+pExt+"M.bed"
        evName = promLoc+en+"/"+cond+"_ev_"+pExt+"T.bed"
        nevName = promLoc+en+"/"+cond+"_nev_"+pExt+"T.bed"
        outEvFileName = outLoc+folderName+"/"+en+"/"+cond+"_ev_"+pExt+".bed"
        outNevFileName = outLoc+folderName+"/"+en+"/"+cond+"_nev_"+pExt+".bed"

        # Merging input files
        os.system("cat "+evFileName+" "+promEvFileName+" | cut -f 1,2,3 | sort -k1,1 -k2,2n > "+evMgd)
        os.system("mergeBed -i "+evMgd+" > "+evName)
        os.system("cat "+nevFileName+" "+promNevFileName+" | cut -f 1,2,3 | sort -k1,1 -k2,2n > "+nevMgd)
        os.system("mergeBed -i "+nevMgd+" > "+nevName)
      
        # Intersections
        os.system("intersectBed -u -wa -a "+peakFileName+" -b "+evName+" > "+outEvFileName)
        os.system("intersectBed -u -wa -a "+peakFileName+" -b "+nevName+" > "+outNevFileName)

        # Termination
        os.system("rm "+evName+" "+nevName+" "+evMgd+" "+nevMgd)


