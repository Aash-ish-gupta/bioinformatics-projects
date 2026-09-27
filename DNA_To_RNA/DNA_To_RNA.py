dnasequence=input("Enter Dna Sequence:").upper()
if dnasequence=="":
    print("Empty Sequence,quitting program...")
    quit()

for i in dnasequence:
    if i not in "ATGC":
        print("Invalid Sequence, quitting program...")
        quit()

rnaconverison=dnasequence.replace("T","U")
print("DNA to RNA Conversion:",rnaconverison)

#converts coding dna sequence to rna sequence by replacing thymine with uracil
