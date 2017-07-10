
# Import
import os

# Parameters
rootLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/"
organism="--organism hg19"
promoter_length="--promoter-length 1000"
maximum_association_length="--maximum-association-length 50000"
multiple_test_alpha="--multiple-test-alpha 0.05"
processes="--processes 1"
print_thresh="--print-thresh 1.0"
bigbed="--bigbed"

#################################################
# Background
#################################################
"""
# Parameters
expMatLoc = rootLoc+"exp_mat/background/"
mLoc = rootLoc+"/results_match/"
resLoc = rootLoc+"results_enrich/background/"
inList = ["dnase_down","dnase_up","faire_down","faire_up","h3k4me1_down","h3k4me1_up","hnf6_down","hnf6_up","promoters_down","promoters_up"]

# Execution
for inName in inList:

  inputMatrix=expMatLoc+inName+".txt"
  matchLoc=mLoc+inName+"/"
  output_location="--output-location "+resLoc
  print "ME_BG_"+inName.upper()

  clusterCommand = "rgt-motifanalysis --enrichment "
  clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
  clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
  os.system(clusterCommand)
"""
#################################################
# Nev
#################################################
"""
# Parameters
expMatLoc = rootLoc+"exp_mat/"
mLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/results_enrich/nev/"

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
      promExtList = ["250","500","1000"]
      for pExt in promExtList:

        print "ME_NEV_"+peakName+"_"+en+"_"+cond+"_"+pExt

        inputMatrix = expMatLoc+peakName+"/"+en+"/"+cond+"_"+pExt+".txt"
        matchLoc = mLoc+peakName+"/"+en+"/"+cond+"_"+pExt+"/"
        output_location="--output-location "+mLoc+peakName+"/"+en+"/"

        clusterCommand = "rgt-motifanalysis --enrichment "
        clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
        clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
        os.system(clusterCommand)
"""
#################################################
# With Enhancer
#################################################

# Parameters
expMatLoc = rootLoc+"exp_mat/random_withEnhancer_background/enrichment/"
mLoc = rootLoc+"results_match/"
rLoc =  rootLoc+"results_enrich/with_enhancer/"

# Iterating on peak files
#peakList = ["hnf6", "dnase", "faire", "h3k4me1"]
peakList = ["hnf6", "h3k4me1"]
for peakName in peakList:

  # Iterting on down / up condition
  enList = ["up", "down"]
  for en in enList:

    # Iterating on conditions
    condList = ["DE_Day0_hetvsWT", "DE_Day10_hetvsWT", "DE_Day14_hetvsWT"]
    for cond in condList:

      print "ME_ENH_"+peakName+"_"+en+"_"+cond

      inputMatrix = expMatLoc+peakName+"_"+en+"/"+cond+".txt"
      matchLoc = mLoc+peakName+"/"
      ol = rLoc+peakName+"_"+en+"/"
      os.system("mkdir -p "+ol)
      output_location="--output-location "+ol

      clusterCommand = "rgt-motifanalysis --enrichment "
      clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
      clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
      os.system(clusterCommand)


