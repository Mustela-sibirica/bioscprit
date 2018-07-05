import csv
import re

csvFile = open(r'C:\Users\SUN\Desktop\tpase.fasta.csv', 'r')
reader = csv.reader(csvFile)
f = open(r'C:\Users\SUN\Desktop\tpase.fasta.bed', 'w')
result = ["","","","","",""]
for item in reader:
    if re.search(r'[A-Za-z]',item[1]):
        pass
    else:
        result[0] = item[1]
        if int(item[8]) < int(item[9]):
            result[1] = str(int(item[8]) - 1)
            result[2] = str(int(item[9]) - 1)
            result[5] = "+"
        else:
            result[1] = str(int(item[9]) - 1)
            result[2] = str(int(item[8]) - 1)
            result[5] = "-"
        result[3] = 'BLAST query \"' + item[0] + '\"'
        result[4] = "0"
        result_str = "\t".join(result) + "\n"
        f.write(result_str)
f.close()
csvFile.close()