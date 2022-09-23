# extract_phonenum.py

## Usage

python3 extract_phonenum.py mytextfile.txt

## Description

Extracts phone numbers from a text file, and prints formatted phone numbers.
One-line per phone number formatted as [+][country code] ([AreaCode]) [local phone number]. [+][country code] optional output if number is international. 

## Known Issues

The regex seems to work on most of the numbers. However, when it comes to formatting, the code only seems to accept a certain format i.e when the numbers are separated using hyphens. This is becuase I have used the hyphens as a delimiter to separate the number and then format it according to the description. Hence, to get the correct format for international numbers, you need to make sure that the country code, area code and the local number are seperated via a hyphen.


# ensg2hugo.py

## Usage

python3 ensg2hugo.py Homo_sapiens.GRCh37.75.formatted.gtf [file]

## Description

You need to read the Homo_sapiens.GRCh37.75.formatted.gtf to create a dictionary, whereby you lookup the Ensembl name and replace it with the HUGO name.

To download the gtf file, paste the code below in your terminal.

```
wget https://github.com/comprna/SUPPA_supplementary_data/raw/master/annotation/Homo_sapiens.GRCh37.75.formatted.gtf.gz
```
Once you download the file, unzip the file using 

```
gunzip Homo_sapiens.GRCh37.75.formatted.gtf.gz
```

## Known Issues

I have created a dictonary and developed a regex to identify the ensembl name. I am yet having issues trying to figure out how to replace the ensembl name with HUGO. I have sucessfully split the columns for the input file into arrays but the code doesn't seem to match the gene_id array with the dictionary.


# histogram.py

## Usage

python3 histogram.py [-f][0-9] [file]

## Description

Creates a histogram as a png from a file using the specified column in a tab delimited file.

-f An optional flag where -f is followed by a number 0-9 indicating which column to use to create the histogram.  If no option is selected, use the 2nd column

## Known Issues

Make sure the column number you add has a numerical value.
