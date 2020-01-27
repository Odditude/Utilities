import sys
database = sys.argv[1]
taxID_database = sys.argv[2]

with open(database, 'r') as fa_in:
    with open(taxID_database, 'w') as fa_out:
        for line in fa_in:
            if line.startswith(">"):
                fa_out.write("|kraken:taxid|50557 ".join(line.split(" ", 1)))
            else:
                fa_out.write(line)
                
'''
Uses:
python add_taxid.py input output
input is a fasta file

Used to change the fasta header to make it appropriate for kraken
'''
