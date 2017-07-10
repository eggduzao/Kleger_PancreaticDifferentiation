
# Previous
#load("./DEgene.RData")
#ls()
#print(DE_Day0_hetvsWT)
#print(DE_Day10_hetvsWT)
#print(DE_Day14_hetvsWT)
#print(DE_Day14_hetvshom)
#write.table(DE_Day0_hetvsWT, file = "DE_Day0_hetvsWT.txt", append = FALSE, quote = FALSE, sep = "\t")
#write.table(DE_Day10_hetvsWT, file = "DE_Day10_hetvsWT.txt", append = FALSE, quote = FALSE, sep = "\t")
#write.table(DE_Day14_hetvsWT, file = "DE_Day14_hetvsWT.txt", append = FALSE, quote = FALSE, sep = "\t")
#write.table(DE_Day14_hetvshom, file = "DE_Day14_hetvshom.txt", append = FALSE, quote = FALSE, sep = "\t")

# New
load("./DEgene_update.RData")
load("../../expression/HNF6_ALLDATA_UpdatedDEgene.RData")
load("./DE_Day25.RData")


write.table(DE_Day0_hetvsWT_rm9682, file = "DE_Day0_hetvsWT_rm9682.txt", append = FALSE, quote = FALSE, sep = "\t")
write.table(DE_Day0_homvsWT_rm9682, file = "DE_Day0_homvsWT_rm9682.txt", append = FALSE, quote = FALSE, sep = "\t")

write.table(DE_Day10_hetvsWT_rm126, file = "DE_Day10_hetvsWT_rm126.txt", append = FALSE, quote = FALSE, sep = "\t")
write.table(DE_Day10_homvsWT_rm126, file = "DE_Day10_homvsWT_rm126.txt", append = FALSE, quote = FALSE, sep = "\t")
write.table(DE_Day14_hetvsWT_rm126, file = "DE_Day14_hetvsWT_rm126.txt", append = FALSE, quote = FALSE, sep = "\t")
write.table(DE_Day14_homvsWT_rm126, file = "DE_Day14_homvsWT_rm126.txt", append = FALSE, quote = FALSE, sep = "\t")
write.table(DE_Day25_hetvsWT_e56, file = "DE_Day25_hetvsWT_rm56.txt", append = FALSE, quote = FALSE, sep = "\t")
write.table(DE_Day25_homvsWT_e56, file = "DE_Day25_homvsWT_rm56.txt", append = FALSE, quote = FALSE, sep = "\t")


