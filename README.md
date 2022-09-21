# extract_phonenum.py

## Usage

python3 extract_phonenum.py mytextfile.txt

## Description

Extracts phone numbers from a text file, and prints formatted phone numbers.
One-line per phone number formatted as [+][country code] ([AreaCode]) [local phone number]. [+][country code] optional output if number is international. 

## Known Issues

The regex seems to work on most of the numbers. However, when it comes to formatting, the code only seems to accept a certain format i.e when the numbers are separated using hyphens. This is becuase I have used the hyphens as a delimiter to separate the number and then format it according to the description. 


# ensg2hugo.py

## Usage

python3 ensg2hugo.py [-f][0-9] [file]

## Description

Key hints. You need to read the Homo_sapiens.GRCh37.75.gtf to create a dictionary, whereby you lookup the Ensembl name and replace it with the HUGO name.

To download the gtf file, paste the code below in your terminal.

```
wget https://github.com/comprna/SUPPA_supplementary_data/raw/master/annotation/Homo_sapiens.GRCh37.75.formatted.gtf.gz
```

## Known Issues

I have issues in identifying the command line argument numbers for sys.argv input statement and hence there may be a possibility that the code breaks. However, according to my understanding, the file should run in their intended matter. For now, I have created a dictonary and developed a regex to identify the ensembl name. I am yet having issues trying to figure out how to replace the ensembl name with HUGO.


# histogram.py

## Usage

python3 histogram.py [-f][0-9] [file]

## Description

Creates a histogram as a png from a file using the specified column in a tab delimited file.

## Known Issues

I have tested the script on a sample csv file. However, I still need to run it on a tsv file. I am yet to incorporate  column based conditions for histogram generation.