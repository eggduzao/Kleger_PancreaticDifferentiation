library(affy)
#load("eset_symbol.RData")
load("HNF6_ALLDATA_UpdatedDEgene.RData")

# remove Bc and bad quality samples.
eset.data.symbol[,c(5,8,14,15,31,32,23,24,56, 45,46, 47, 48, 53, 54, 55 )] = list(NULL)
# remove all 126 clones
eset.data.symbol[,grep("126",colnames(eset.data.symbol))]= list(NULL)
pca=prcomp(t(eset.data.symbol))
pdf("PCA_names.pdf")

plot(pca$x[,1:2])
text(pca$x[,1:2],colnames(eset.data.symbol))
dev.off()

pdf("PCA_colors_shapes.pdf")
colors=colnames(eset.data.symbol)
colors[grep("ES",colnames(eset.data.symbol))]="black"
colors[grep("DE",colnames(eset.data.symbol))]="red"
colors[grep("PP1",colnames(eset.data.symbol))]="blue"
colors[grep("PP2",colnames(eset.data.symbol))]="grey"
points=as.numeric(colnames(eset.data.symbol))
points[grep("WT",colnames(eset.data.symbol))]=20 # circle
points[grep("Hom",colnames(eset.data.symbol))]=15 # square
points[grep("Het",colnames(eset.data.symbol))]=17 # triangle


plot(pca$x[,1:2],pch=points,cex=1.5,col=colors)
legend("topright", inset=.05, title="Diff. Stage",
  	c("ES","DE","PE","PP"), fill=c("black","red","blue","grey"), horiz=TRUE)

legend("bottomright", inset=.05, 
  	c("WT","HET","HOM"), pch=c(20,17,15), horiz=TRUE)

dev.off()


pdf("PCA_colors_shapes_large.pdf",width=14, height=14)



plot(pca$x[,1:2],pch=points,cex=1.5,col=colors)
legend("topright", inset=.05, title="Diff. Stage",
  	c("ES","DE","PE","PP"), fill=c("black","red","blue","grey"), horiz=TRUE)

legend("bottomright", inset=.05, 
  	c("WT","HET","HOM"), pch=c(20,17,15), horiz=TRUE)


dev.off()


#plot(pca$x[,1:2],)

pdf("PCA_names.pdf")
#plot(pca$x[,1:2],ylim=c(5,-30),xlim=c(70,120))
plot(pca$x[,1:2])
text(pca$x[,1:2],colnames(eset.data.symbol))
dev.off()

pdf("PCA_beta.pdf")
plot(pca$x[,1:2],xlim=c(140,200),ylim=c(-100,-50))
text(pca$x[,1:2],colnames(eset.data.symbol))
dev.off()


pdf("PCA.pdf",width=12,height=12)

plot(pca$x[,1:2],pch=19,cex=0.1)
sel=grep("ES",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='red',pch=20.,cex=1.5)
sel=grep("DE",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='blue',pch=20,cex=1.5)
sel=grep("PP1",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='green',pch=20,cex=1.5)
sel=grep("PP2",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='orange',pch=20,cex=1.5)
sel=grep("BC",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='cyan',pch=20,cex=1.5)

#sel=grep("ES",)
names_clean=gsub("ES_|PP1_|PP2_|DE_|BC_|_d0|_d4|_d10|_d14|_1|_2|_120|_82|_126|_96|_374|.2","",colnames(eset.data.symbol)) 

text(pca$x[,1:2]+2,names_clean,cex=1.5)

legend("bottomleft", inset=.05, title="Cell Type",
  	c("ES","DE","PP1","PP2","BC"), fill=c("red","blue","green","orange","cyan"), horiz=TRUE,title.cex=1.5)
dev.off()


type=rep(19,length(colnames(eset.data.symbol)))
type[grep("Hom",colnames(eset.data.symbol))]=0
type[grep("Het",colnames(eset.data.symbol))]=3

pdf("PCA_notext.pdf")

layout(rbind(1,2), heights=c(7,1))

plot(pca$x[,1:2],pch=26,cex=0.1,xlab="Beta Cell Component", ylab="Progenitor Component")
sel=grep("ES",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='red',pch=type[sel],cex=1.5)
sel=grep("DE",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='blue',pch=type[sel],cex=1.5)
sel=grep("PP1",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='green',pch=type[sel],cex=1.5)
sel=grep("PP2",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='orange',pch=type[sel],cex=1.5)
sel=grep("BC",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='cyan',pch=type[sel],cex=1.5)


#sel=grep("ES",)
names_clean=gsub("ES_|PP1_|PP2_|DE_|_d0|_d4|_d10|_d14|_1|_2|_82|_126|_96|_374","",colnames(eset.data.symbol))


legend("bottomleft", inset=.05, title="Cell Type",
c("WT","Het.","Hom."), col=c("black","black","black"),pch = c(19,3,0), horiz=TRUE, cex=1.25)

#text(pca$x[,1:2]+2,names_clean,cex=1.5)
par(mar=c(0, 0, 0, 0))
# c(bottom, left, top, right)
plot.new()
legend("center", inset=.05, title="Cell Stage",
  	c("ES","DE","PE","PP","BC"), fill=c("red","blue","green","orange","cyan"), horiz=TRUE, cex=1.25)
dev.off()


<<<<<<< .mine
pdf("PCA_zoom.pdf")

plot(pca$x[,1:2],ylim=c(-30,100),xlim=c(-70,70),pch=19,cex=0.1)
=======
pdf("PCA_zoom.pdf")
plot(pca$x[,1:2],ylim=c(-30,100),xlim=c(-70,70),pch=26,cex=0.1,xlab="Beta Cell Component", ylab="Progenitor Component")
>>>>>>> .r1349
sel=grep("ES",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='red',ylim=c(-30,100),xlim=c(-70,70),pch=type[sel],cex=1.5)
sel=grep("DE",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='blue',ylim=c(-30,100),xlim=c(-70,70),pch=type[sel],cex=1.5)
sel=grep("PP1",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='green',ylim=c(-30,100),xlim=c(-70,70),pch=type[sel],cex=1.5)
sel=grep("PP2",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='orange',ylim=c(-30,100),xlim=c(-70,70),pch=type[sel],cex=1.5)
sel=grep("BC",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='cyan',ylim=c(-30,100),xlim=c(-70,70),pch=type[sel],cex=1.5)

legend("bottomright", inset=.05, title="Cell Type",
c("WT","Het.","Hom."), col=c("black","black","black"),pch = c(19,3,0), horiz=TRUE, cex=1.25)

legend("topleft", inset=.05, title="Cell Stage",c("DE","PE","PP"), fill=c("blue","green","orange"), horiz=TRUE, cex=1.25)


#text(pca$x[,1:2]+1,names_clean)
#legend("topright", inset=.05, title="Cell Type",
#  	c("ES","DE","PP1","PP2"), fill=c("red","blue","green","orange"), horiz=TRUE,cex=1.5)
dev.off()

pdf("PCA_zoom2.pdf")
plot(pca$x[,1:2],ylim=c(40,100),xlim=c(-30,70),pch=26,cex=0.1,xlab="Beta Cell Component", ylab="Progenitor Component")
sel=grep("ES",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='red',ylim=c(40,100),xlim=c(-30,70),pch=type[sel],cex=1.5)
sel=grep("DE",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='blue',ylim=c(40,100),xlim=c(-30,70),pch=type[sel],cex=1.5)
sel=grep("PP1",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='green',ylim=c(40,100),xlim=c(-30,70),pch=type[sel],cex=1.5)
sel=grep("PP2",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='orange',ylim=c(40,100),xlim=c(-30,70),pch=type[sel],cex=1.5)
sel=grep("BC",colnames(eset.data.symbol))
points(pca$x[sel,1:2],col='cyan',ylim=c(40,100),xlim=c(-30,70),pch=type[sel],cex=1.5)



#text(pca$x[,1:2]+1,names_clean)
#legend("topright", inset=.05, title="Cell Type",
#  	c("ES","DE","PP1","PP2"), fill=c("red","blue","green","orange"), horiz=TRUE,cex=1.5)
dev.off()


#sel=grep("DE",colnames(eset.data.symbol))
#text(pca$x[sel,1:2]+5,rep(c("DE"),length(sel)))

#sel=grep("PP1",colnames(eset.data.symbol))
#text(pca$x[sel,1:2]+5,rep(c("PP1"),length(sel)))

#sel=grep("PP2",colnames(eset.data.symbol))
#text(pca$x[sel,1:2]+5,rep(c("PP2"),length(sel)))

