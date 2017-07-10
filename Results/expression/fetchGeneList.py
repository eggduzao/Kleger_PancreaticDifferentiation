
import os
import sys

inLoc = "./"
#inList = ["DE_Day0_hetvsWT", "DE_Day10_hetvsWT", "DE_Day14_hetvshom", "DE_Day14_hetvsWT"]
inList = ["DE_Day0_hetvsWT_rm9682", "DE_Day0_homvsWT_rm9682", "DE_Day10_hetvsWT_rm126", 
          "DE_Day10_homvsWT_rm126", "DE_Day14_hetvsWT_rm126", "DE_Day14_homvsWT_rm126","DE_Day25_homvsWT_rm56","DE_Day25_hetvsWT_rm56"]

for inName in inList:
  inFileName = inLoc+inName+".txt"
  inFile = open(inFileName,"r")
  inFile.readline()
  outFileD = open("./down/"+inName+"_genelist.txt","w")
  outFileU = open("./up/"+inName+"_genelist.txt","w")
  for line in inFile:
    ll = line.strip().split("\t")
    if(float(ll[1]) >= 0): outFileU.write(ll[0]+"\n")
    else: outFileD.write(ll[0]+"\n")
  inFile.close()
  outFileD.close()
  outFileU.close()


