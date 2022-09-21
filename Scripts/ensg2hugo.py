import pandas as pd
import sys

filename = sys.argv[2]
df=pd.read_csv('expres.anal.csv')
x = df['gene_id'].ravel()
y = df['gene_type'].ravel()
d={}
for i in range(len(x)):
    d[x[i]] = y[i]
    
pip install gtfparse
from gtfparse import read_gtf

df1 = read_gtf("Homo_sapiens.GRCh37.75.formatted.gtf")
df1
lookup_ens = {}
x = df1['gene_id'].ravel()
y = df1['gene_name'].ravel()
for i in range(len(x)):
    lookup_ens[x[i]] = y[i]
    
import fileinput
import re

for each_line_of_text in fileinput.input('expres.anal.csv'):
    f = re.findall(r'ENSG\d{11,}' , each_line_of_text, re.I)
    print(f)
    