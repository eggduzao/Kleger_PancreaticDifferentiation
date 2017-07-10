# gene exp association analysis
#python ~/projects/reg-gen/tools/geneAssociationZscore.py input_matrix.txt ~/projects/reg-gen/data/hg19/ 100 > z_score.wt_ko 
#python ~/projects/reg-gen/tools/geneAssociationZscore.py input_matrix_cluster.txt ~/projects/reg-gen/data/hg19/ 100 > z_score.cluster 

# gene to peaks
#cat ../expression/up/DE_Day*genelist.txt ../expression/down/DE_Day*genelist.txt | sort | uniq > all_genes.txt
#cat ../expression/up/DE_Day*genelist.txt ../expression/down/DE_Day*genelist.txt | sort | uniq > all_genes_wt.txt

python ~/projects/reg-gen/tools/genesFromBed.py --distance=20000 -m 4 input_bed.txt ~/rgtdata/hg19/ all_genes.txt
grep chr region_Hnf6.data  > region_Hnf6_all.data
python ~/projects/reg-gen/tools/genesFromBed.py --distance=20000 -m 4 input_bed.txt ~/rgtdata/hg19/ all_genes_wt.txt 
grep chr region_Hnf6.data  > region_Hnf6_wt.data


grep -w -f ../expression/up/DE_Day10_hetvsWT_rm126_genelist.txt region_Hnf6_wt.data > PP1_Het_UP.txt
grep -w -f ../expression/down/DE_Day10_hetvsWT_rm126_genelist.txt region_Hnf6_wt.data > PP1_Het_DOWN.txt
grep -w -f ../expression/up/DE_Day10_homvsWT_rm126_genelist.txt region_Hnf6_wt.data > PP1_Hom_UP.txt
grep -w -f ../expression/down/DE_Day10_homvsWT_rm126_genelist.txt region_Hnf6_wt.data > PP1_Hom_DOWN.txt

wc PP1_H*txt

grep -w -f ../expression/up/DE_Day14_hetvsWT_rm126_genelist.txt region_Hnf6_wt.data > PP2_Het_UP.txt
grep -w -f ../expression/down/DE_Day14_hetvsWT_rm126_genelist.txt region_Hnf6_wt.data > PP2_Het_DOWN.txt
grep -w -f ../expression/up/DE_Day14_homvsWT_rm126_genelist.txt region_Hnf6_wt.data > PP2_Hom_UP.txt
grep -w -f ../expression/down/DE_Day14_homvsWT_rm126_genelist.txt region_Hnf6_wt.data > PP2_Hom_DOWN.txt

wc ../expression/up/DE_Day14_*vsWT_rm126_genelist.txt
wc ../expression/down/DE_Day14_*vsWT_rm126_genelist.txt



# chip seq analysis

#slopBed -b 50 -i Hnf6_Day14_up.bed -g ../panc_prog/hg19.genome > aux.bed
#mv aux.bed Hnf6_Day14_up.bed
#slopBed -b 50 -i Hnf6_Day14_down.bed -g ../panc_prog/hg19.genome > aux.bed
#mv aux.bed Hnf6_Day14_down.bed

#sort -n -k 4 -r Hnf6_Day14_up.bed | head -n 500 > Hnf6_100_up.bed
#sort -n -k 4 -r Hnf6_Day14_down.bed | head -n 500 > Hnf6_100_down.bed
#fastaFromBed -fi ~/projects/genomes/hg19.fa -bed Hnf6_100_up.bed -fo Hnf6_100_up.fa
#fastaFromBed -fi ~/projects/genomes/hg19.fa -bed Hnf6_100_down.bed -fo Hnf6_100_down.fa


#meme-chip -nmeme 500 -ccut 100 -meme-maxw 12 Hnf6_100_down.fa -oc down
#meme-chip -nmeme 500 -ccut 100 -meme-maxw 12 Hnf6_100_up.fa -oc up

