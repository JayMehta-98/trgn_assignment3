import sys
import re
import fileinput

gtf_file=sys.argv[1]
Lookup_gene={}
for each_line_of_text in fileinput.input(gtf_file):
    ensg = re.findall(r'ENSG[\d\.]{11}',each_line_of_text, re.I)
    #print (ensg)
    HUGO = re.findall(r'gene_name\s(\".*?\")',each_line_of_text)
    #print (HUGO)
    if ensg:
        if HUGO:
            Lookup_gene[ensg[0]] = HUGO[0]
            print (ensg[0]+ ":"+ HUGO[0])

sample = open('expression_analysis.hugo.tsv', 'w')
file_to_change=sys.argv[2]
for each_line_of_text in fileinput.input(file_to_change):
    #print (each_line_of_text)
    splitcolumn_array = re.split(',',each_line_of_text.replace('\n','').replace( '"' ,''))
    if splitcolumn_array[1] in Lookup_gene:
        #print (splitcolumn_array)
        if splitcolumn_array[1] in Lookup_gene:
            print (Lookup_gene[splitcolumn_array[1]])
            splitcolumn_array.append(Lookup_gene[splitcolumn_array[1]])
            res = str(splitcolumn_array)[1:-1]
            resmod = res.replace("\'", "")
            print(resmod, file = expression_analysis.hugo.tsv)


