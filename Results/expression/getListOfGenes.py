
# Import
import os
import sys
from glob import glob

# Input
inFileList = glob("./*.txt")
gtfFileName = "/home/egg/Projects/RGT/reg-gen/data/hg19/gencode_annotation.gtf"
gtfGeneFileName = "/home/egg/Projects/PancreaticDifferentiation/Results/motif_enrichment/genes/genes.gtf"
assocFileName = "./association_file.bed"
promLoc = "/home/egg/Projects/PancreaticDifferentiation/Results/motif_enrichment/promoters/"
promExtList = [250,500,1000]

# Fetch promoters function
def fetch_promoters(inFileName,outFileName):
  inFile = open(inFileName,"r")
  outFileNameListUns = [outFileName+"_"+str(e)+"Uns.bed" for e in promExtList]
  outFileNameList = [outFileName+"_"+str(e)+".bed" for e in promExtList]
  outFileList = [open(e,"w") for e in outFileNameListUns]
  for line in inFile:
    ll = line.strip().split("\t")
    if(ll[5] == "+"):
      for i in range(0,len(outFileList)): outFileList[i].write("\t".join([ll[0],str(int(ll[1])-promExtList[i]),str(int(ll[1])+1)])+"\n")
    else:
      for i in range(0,len(outFileList)): outFileList[i].write("\t".join([ll[0],str(int(ll[2])-1),str(int(ll[2])+promExtList[i])])+"\n")
  for i in range(0,len(outFileList)):
    outFileList[i].close()
    os.system("sort -k1,1 -k2,2n "+outFileNameListUns[i]+" > "+outFileNameList[i])
    os.system("rm "+outFileNameListUns[i])
  inFile.close()
  
# Reading association file
assocDict = dict()
assocFile = open(assocFileName,"r")
for line in assocFile:
  ll = line.strip().split("\t")
  assocDict[ll[3].upper()] = ll
assocFile.close()

# Reading alias file
alias_file = open("/home/egg/Projects/RGT/reg-gen/data/hg19/alias.txt","r")
alias_dict = dict()
for line in alias_file:
  ll = line.strip().split("\t")
  ensembl_id = ll[0]
  official_name = ll[1]
  alias_vec = ll[2].split("&")
  for e in alias_vec:
    try: alias_dict[e][0].append(ensembl_id)
    except Exception: alias_dict[e] = [[ensembl_id],official_name]
alias_file.close()

# Iterating on file list
for inFileName in inFileList:

  # Opening file
  inFile = open(inFileName,"r")
  resList = []
  
  # Iterating on file
  inFile.readline()
  for line in inFile:
    ll = line.strip().split("\t")
    if("chr" in ll[0]): 
      lll = ll[0].split(":")
      zzz = lll[2].split("_")
      ppp = zzz[0].split("-")
      strand = "+"
      if(zzz[1] == "R"): strand = "-"
      resList.append([[lll[1],ppp[0],ppp[1],lll[0],"0",strand],float(ll[1])])
    else:
      try: resList.append([assocDict[ll[0].upper()],float(ll[1])])
      except Exception:
        try: resList.append([[".",".",".",alias_dict[ll[0].upper()][0][0],".","."],float(ll[1])])
        except Exception: resList.append([[".",".",".",ll[0].upper(),".","."],float(ll[1])])

  # Writing output
  outName = inFileName.split("/")[-1].split(".")[0]
  outFileUpName = "./up/"+outName+"_evUns.bed"
  outFileDwName = "./down/"+outName+"_evUns.bed"
  outFileUp = open(outFileUpName,"w")
  outFileDw = open(outFileDwName,"w")
  outFileUpNA = open("./up/"+outName+"_notfound.txt","w")
  outFileDwNA = open("./down/"+outName+"_notfound.txt","w")
  outFileUpENSNameT = "./up/"+outName+"_ensT.txt"
  outFileDwENSNameT = "./down/"+outName+"_ensT.txt"
  outFileUpENS = open(outFileUpENSNameT,"w")
  outFileDwENS = open(outFileDwENSNameT,"w")
  outFileUpENS.close()
  outFileDwENS.close()
  for res in resList:
    if(res[0][0] == "."):
      if("ENS" in res[0][3]):
        if(res[1] >= 0): os.system("grep "+res[0][3]+" "+gtfFileName+" >> "+outFileUpENSNameT)
        else: os.system("grep "+res[0][3]+" "+gtfFileName+" >> "+outFileDwENSNameT)
      else:
        if(res[1] >= 0): outFileUpNA.write(res[0][3]+"\n")
        else: outFileDwNA.write(res[0][3]+"\n")
    else:
      if(res[1] >= 0): outFileUp.write("\t".join(res[0])+"\n")
      else: outFileDw.write("\t".join(res[0])+"\n")
  
  # Reading ensembl genes
  outFileUpENSName = "./up/"+outName+"_ens.txt"
  outFileDwENSName = "./down/"+outName+"_ens.txt"
  inFileUpENS = open(outFileUpENSNameT,"r")
  inFileDwENS = open(outFileDwENSNameT,"r")
  upDict = dict()
  for line in inFileUpENS:
    upDict[line.strip().split("\t")[8].split("\"; ")[0].split(" \"")[1]] = "."
  downDict = dict()
  for line in inFileDwENS:
    downDict[line.strip().split("\t")[8].split("\"; ")[0].split(" \"")[1]] = "."
  inFileUpENS.close()
  inFileDwENS.close()
  upEnsList = sorted(upDict.keys())
  downEnsList = sorted(downDict.keys())

  # Writing ensembl genes
  for k in upEnsList:
    os.system("grep "+k+" "+gtfGeneFileName+" > "+outFileUpENSNameT)
    inF = open(outFileUpENSNameT,"r")
    ll = inF.readline().strip().split("\t")
    geneName = ll[8].split("\"; ")[4].split(" \"")[1]
    outFileUp.write("\t".join([ll[0],ll[3],ll[4],geneName,"0",ll[6]])+"\n")
    inF.close()
  for k in downEnsList:
    os.system("grep "+k+" "+gtfGeneFileName+" > "+outFileDwENSNameT)
    inF = open(outFileDwENSNameT,"r")
    ll = inF.readline().strip().split("\t")
    geneName = ll[8].split("\"; ")[4].split(" \"")[1]
    outFileDw.write("\t".join([ll[0],ll[3],ll[4],geneName,"0",ll[6]])+"\n")
    inF.close()

  # Termination
  inFile.close()
  outFileUp.close()
  outFileDw.close()
  outFileUpNA.close()
  outFileDwNA.close()
  os.system("rm "+outFileUpENSNameT+" "+outFileDwENSNameT)

  # Fetching nev genes
  outFileUpNameNev = "./up/"+outName+"_nevUns.bed"
  outFileDwNameNev = "./down/"+outName+"_nevUns.bed"
  os.system("intersectBed -v -wa -a "+assocFileName+" -b "+outFileUpName+" > "+outFileUpNameNev)
  os.system("intersectBed -v -wa -a "+assocFileName+" -b "+outFileDwName+" > "+outFileDwNameNev)

  # Sorting files
  outFileUpNameS = "./up/"+outName+"_ev.bed"
  outFileDwNameS = "./down/"+outName+"_ev.bed"
  outFileUpNameNevS = "./up/"+outName+"_nev.bed"
  outFileDwNameNevS = "./down/"+outName+"_nev.bed"
  os.system("sort -k1,1 -k2,2n "+outFileUpName+" > "+outFileUpNameS)
  os.system("sort -k1,1 -k2,2n "+outFileDwName+" > "+outFileDwNameS)
  os.system("sort -k1,1 -k2,2n "+outFileUpNameNev+" > "+outFileUpNameNevS)
  os.system("sort -k1,1 -k2,2n "+outFileDwNameNev+" > "+outFileDwNameNevS)

  # Fetching promoters
  promUpFileNameEv = promLoc+"up/"+outName+"_ev"
  promUpFileNameNev = promLoc+"up/"+outName+"_nev"
  promDwFileNameEv = promLoc+"down/"+outName+"_ev"
  promDwFileNameNev = promLoc+"down/"+outName+"_nev"
  fetch_promoters(outFileUpNameS,promUpFileNameEv)
  fetch_promoters(outFileUpNameNevS,promUpFileNameNev)
  fetch_promoters(outFileDwNameS,promDwFileNameEv)
  fetch_promoters(outFileDwNameNevS,promDwFileNameNev)

  # Termination
  for e in [outFileUpName,outFileDwName,outFileUpNameNev,outFileDwNameNev]: os.system("rm "+e)


