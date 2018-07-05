import csv
import re

csvFile = open(r'C:\Users\SUN\Desktop\tpase.fasta.csv', 'r')
reader = csv.reader(csvFile)
f = open(r'C:\Users\SUN\Desktop\tpase.fasta.gtf', 'w')
result = ["","","","","","","","",""]
for item in reader:
    if re.search(r'[A-Za-z]',item[1]):
        pass
    else:
        result[0] = item[1]
        result[1] = "BLAST"
        result[2] = "gene"
        if int(item[8]) < int(item[9]):
            result[3] = item[8]
            result[4] = item[9]
            result[6] = "+"
        else:
            result[3] = item[9]
            result[4] = item[8]
            result[6] = "-"
        result[5] = "."
        result[7] = "."
        result[8] = 'gene_id \"' + item[0] + '\"'
        result_str = "\t".join(result) + "\n"
        f.write(result_str)
f.close()
csvFile.close()