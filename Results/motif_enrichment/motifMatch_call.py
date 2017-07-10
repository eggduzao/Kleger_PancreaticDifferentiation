
# Import
import os

# Parameters
organism="--organism hg19"
fpr="--fpr 0.0001"
precision="--precision 10000"
pseudocounts="--pseudocounts 0.1"
rand_proportion="--rand-proportion 10"
bigbed="--bigbed"

"""
# Iterating on input matrices
inLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/exp_mat/"
outLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/results_match/"
inList = ["dnase_down","dnase_up","faire_down","faire_up","h3k4me1_down","h3k4me1_up","hnf6_down","hnf6_up","promoters_down","promoters_up"]
for inName in inList:

  # Initialization
  inputMatrix = inLoc+inName+".txt"
  ol = outLoc+inName+"/"
  os.system("mkdir -p "+ol)
  output_location="--output-location "+ol

  # Execution
  myL = inName
  clusterCommand = "bsub "
  clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
  clusterCommand += "-W 120:00 -M 24000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
  clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
  clusterCommand += output_location+" "+bigbed+" "+inputMatrix
  os.system(clusterCommand)
"""

# Iterating on input matrices
inLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/exp_mat/random_withEnhancer_background/matching/"
outLoc = "/work/eg474423/eg474423_Projects/trunk/PancreaticDifferentiation/Results/motif_enrichment/results_match/"
inList = ["dnase","faire","h3k4me1","hnf6"]
for inName in inList:

  # Initialization
  inputMatrix = inLoc+inName+".txt"
  ol = outLoc+inName+"/"
  os.system("mkdir -p "+ol)
  output_location="--output-location "+ol

  # Execution
  myL = inName
  clusterCommand = "bsub "
  clusterCommand += "-J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
  clusterCommand += "-W 120:00 -M 24000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
  clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
  clusterCommand += output_location+" "+bigbed+" "+inputMatrix
  os.system(clusterCommand)


