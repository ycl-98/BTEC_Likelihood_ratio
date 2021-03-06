# Base code to set up data 
import math
import matplotlib.pyplot as plt
import numpy as np
import gzip
from scipy.stats import gaussian_kde
filename = gzip.open(r'/content/drive/MyDrive/chr21_SpliceAI_GTEx.txt.gz') #change directory 
real_acc1=[]  #GTEx>0
real_don1=[]  
real_acc2=[] #GTEx >100
real_don2=[]
real_acc3=[] #GTEx >10000
real_don3=[] 
non_acc=[] #for all acceptor GTEx =0
non_don=[] #for all donor GTEx=0
line = filename.readlines()
threshold1= 0  #thresholds 
threshold2=100
threshold3=10000
for i in range(1,len(line)):
    x=line[i].split()
    if float(x[4])==0:  #null acceptor 
      non_acc.append(math.log(float(x[2]),10))
    if float(x[4]) > threshold1:      # Note: x[4]=GTEx_acc_read, if GTEx acc>threshold, append spliceAI mean
      real_acc1.append(math.log(float(x[2]),10))
    if float(x[4]) > threshold2:
      real_acc2.append(math.log(float(x[2]),10))
    if float(x[4]) > threshold3:
      real_acc3.append(math.log(float(x[2]),10))

    if float(x[9])==0:  #null donor
      non_don.append(math.log(float(x[7]),10))
    if float(x[9])> threshold1:       # Note: x[9]=GTEx_don_read, if GTEx don>threshold, append spliceAI mean
      real_don1.append(math.log(float(x[7]),10))
    if float(x[9])> threshold2:
      real_don2.append(math.log(float(x[7]),10))
    if float(x[9])> threshold3:
      real_don3.append(math.log(float(x[7]),10))
    
#ePDF empirical Probability Density Function, normalized with gaussian kernel density estimation PLOTS EPDFs
plt.figure(figsize=(12, 8))
non_acc_density=gaussian_kde(non_acc)
real_acc1_density=gaussian_kde(real_acc1)
real_acc2_density=gaussian_kde(real_acc2)
real_acc3_density=gaussian_kde(real_acc3)
linspace=np.linspace(-12, 0.5, 100)
plt.plot(linspace, non_acc_density(linspace))
plt.plot(linspace,real_acc1_density(linspace))
plt.plot(linspace,real_acc2_density(linspace))
plt.plot(linspace,real_acc3_density(linspace))

plt.legend(['Null, GTEx==0','GTEx>'+str(threshold1),'GTEx>'+str(threshold2),'GTEx>'+str(threshold3)])
plt.xlabel('SpliceAI score Acceptor (log10 scale)')
plt.ylabel('Density')
plt.title('Chr 21. Acceptor ePDF --with gaussian kde')
plt.show()

plt.figure(2) #for donor
plt.figure(figsize=(12, 8))
non_don_density=gaussian_kde(non_don)
real_don1_density=gaussian_kde(real_don1)
real_don2_density=gaussian_kde(real_don2)
real_don3_density=gaussian_kde(real_don3)
linspace=np.linspace(-12, 0.5, 100)
plt.plot(linspace, non_don_density(linspace))
plt.plot(linspace,real_don1_density(linspace))
plt.plot(linspace,real_don2_density(linspace))
plt.plot(linspace,real_don3_density(linspace))

plt.legend(['Null, GTEx==0','GTEx>'+str(threshold1),'GTEx>'+str(threshold2),'GTEx>'+str(threshold3)])
plt.xlabel('SpliceAI score Donor (log10 scale)')
plt.ylabel('Density')
plt.title('Chr 21. Donor ePDF --with gaussian kde')
plt.show()

###Setting up for K ratio plots
reala0=non_acc_density(linspace)
reala1=real_acc1_density(linspace)
reala2=real_acc2_density(linspace)
reala3=real_acc3_density(linspace)

#for donor
reald0=non_don_density(linspace)
reald1=real_don1_density(linspace)
reald2=real_don2_density(linspace)
reald3=real_don3_density(linspace)

### K likelihood ratio plot
plt.figure(figsize=(12, 8))
y=[]
for i in range(0,100):
  y.append(1)
### ACCEPTOR
K0=reala1/reala0
K100=reala2/reala0
K10000=reala3/reala0
plt.plot(linspace, K0)
plt.plot(linspace, K100)
plt.plot(linspace, K10000)

plt.plot(linspace,y,'--')
plt.yscale("log")
plt.axis([-12,1,0.00000001, 10000000])

plt.legend(['K0','K100','K10000'])
plt.xlabel('SpliceAI score Acceptor (log10 scale)')
plt.ylabel('K value')
plt.title('Chr 21. Acceptor likelihood ratio-- with Gaussian KDE')

### DONOR
plt.figure(2)
plt.figure(figsize=(12, 8))
K0=reald1/reald0
K100=reald2/reald0
K10000=reald3/reald0
plt.plot(linspace, K0)
plt.plot(linspace, K100)
plt.plot(linspace, K10000)

plt.plot(linspace,y,'--')
plt.yscale("log")
plt.axis([-12,1,0.00000001, 10000000])

plt.legend(['K0','K100','K10000'])
plt.xlabel('SpliceAI score Donor (log10 scale)')
plt.ylabel('K value')
plt.title('Chr 21. Donor likelihood ratio-- with Gaussian KDE')
