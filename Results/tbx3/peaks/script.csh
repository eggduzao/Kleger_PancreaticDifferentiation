for l in `ls *.fastq`;
do
  l1=${l/fastq/}   
  bwa aln -t 6  ~/projects/genomes/mm9.fa $l > $l1'sai'
  bwa samse ~/projects/genomes/mm9.fa $l1'sai' $l > $l1'sam'
  samtools view -S -b $l1'sam' > $l1'bam'
  samtools sort $l1'bam' $l1'sorted.bam'
  #rm $l1'sai'
  #rm $l1'sam'
  /home/ivan/projects/app/IGVTools/igvtools count -e 200  $l1'sorted.bam.bam'  $l1'tdf' ~/projects/genomes/mm9.fa    
done 


macs2 -t Tbx3_ES.sorted.bam.bam -c Tbx3_ES_Control.sorted.bam.bam
#mv NA_peaks.broadPeak Tbx3_ES.bed

#awk '$9 > 1.5' PP2_H3K4me1.bed > PP2_H3K4me1_1_5.bed
#awk '$9 > 1' PP2_H3K4me1.bed > PP2_H3K4me1_1.bed

#slopBed -b 50 -i PP2_Hnf6_summits.bed -g hg19.genome > PP2_Hnf6_100.bed
##sort -n -k 5 -r PP2_Hnf6_100.bed | head -n 500 > PP2_Hnf6_100_500.bed
#fastaFromBed -fi ~/projects/genomes/hg19.fa -bed PP2_Hnf6_100_500.bed -fo PP2_Hnf6_100.fa
fastaFromBed -fi ~/projects/genomes/hg19.fa -bed PP2_Hnf6_100.bed -fo PP2_Hnf6_100_all.fa

#meme-chip -db ~/projects/app/meme_4.10.0/motif_databases/JASPAR_CORE_2014_vertebrates.meme -meme-maxw 12 -meme-nmotifs 5 PP2_Hnf6_100.fa



