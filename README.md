# BTEC_Likelihood_ratio
get_K.py returns the Likelihood ratio (K) plots between the empirical Probability Denisty Functions (ePDFs) of real splicing data and non splicing data. 

Please note that the indexing in this code is specifically for the annonated SpliceAI score for positions in different Chromosomes (Columns should include: Chromosome, position, spliceAI_acc_means, spliceAI_acc_stdev, GTEx_acc_reads, GTEX_acc_samples, ENSEMBL_acc, spliceAI_don_means, spliceAI_don_stdev, GTEx_don_reads, GTEX_don_samples, ENSEMBL_don). 

The code was developed based on the following dependencies:
1. matplotlib
4. NumPy
5. gzip
6. SciPy

#Code Summary
This code first unzips the input Chromosme_SpliceAI_GTEx.txt.gz file and divides the data set into 8 subsets:  3 real acceptor data sets with different GTEx_read thresholds, 1 non acceptor data set where GTEx_acc_read=0, 3 real donor data sets with different GTEx_read thresholds, and 1 non donor data set where GTEx_don_read=0. 

The code then normalizes the density of the 8 subsets with Gaussian Kernel Density Estimation and calculuates the Likelihood ratios and produce the plots. 
