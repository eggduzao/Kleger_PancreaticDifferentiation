import os
import sys
peakHalfExt = 50
peakFileName = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/ngs_data/hnf6/PP2_Hnf6_summits_10.bed"
newPeakFileNameT = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/ngs_data/hnf6/PP2_Hnf6_summits_10_temp.bed"
newPeakFileName = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/ngs_data/hnf6/PP2_Hnf6_summits_10_format.bed"
peakFile = open(peakFileName,"r")
newPeakFile = open(newPeakFileNameT,"w")
for line in peakFile:
  ll = line.strip().split("\t")
  mid = (int(ll[1]) + int(ll[2])) / 2
  p1 = str(mid-peakHalfExt); p2 = str(mid+peakHalfExt)
  newPeakFile.write("\t".join([ll[0],p1,p2])+"\n")
peakFile.close()
newPeakFile.close()
os.system("grep -v -E 'chrY|chrM|random' "+newPeakFileNameT+" > "+newPeakFileName)
