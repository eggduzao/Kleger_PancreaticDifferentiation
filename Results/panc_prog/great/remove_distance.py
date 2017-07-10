import sys

for l in open(sys.argv[1]):
  l=l.strip("\n")
  l=l.split("(")
#print l
  try:
    print l[1].split(")")[0]
    print l[2].split(")")[0]
  except:
    pass

