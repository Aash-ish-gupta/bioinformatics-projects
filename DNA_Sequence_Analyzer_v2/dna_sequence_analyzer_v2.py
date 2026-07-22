sequence=input("Enter The DNA Sequence:").upper()
countgc=0
countat=0
counta=0
countt=0
countg=0
countc=0
complement_dictionary={'A':'T','G':'C','T':'A','C':'G'}
complement=""
length=len(sequence)
start_codon=False
stop_codon=False
if length == 0:
    print("DNA sequence cannot be empty.")
    quit()

for base in sequence:
    if base not in ['A','T','G','C']:
        print("Invalid base:",base)
        print("Invalid Sequence(quitting program...)")
        quit()
        
for i in range(0, length,3):
    codon=sequence[i:i+3]

    if "ATG" in codon:
        print("Start codon Found(ATG) at Position",i+1)
        start_codon=True

    if "TAA" in codon:
        print("Stop codon Found(TAA) at Position",i+1)
        stop_codon=True
    elif "TAG" in codon:
        print("Stop codon Found(TAG) at Position",i+1)
        stop_codon=True
    elif "TGA" in codon:
        print("Stop codon Found(TGA) at Position",i+1)
        stop_codon=True
        
if not start_codon:
    print("No Start Codon Found")
        
if not stop_codon:
    print("No Stop Codon Found")
        
for base in sequence:
    complement+=complement_dictionary[base]
        
    if base=='G' or base=='C':
        countgc=countgc+1
    
    if base=='A' or base=='T':
        countat=countat+1
    
    if base=='A':
        counta=counta+1
        
    if base=='T':
        countt=countt+1
        
    if base=='G':
        countg=countg+1
    
    if base=='C':
        countc=countc+1

rna=sequence.replace('T','U')
reverse_sequence=sequence[::-1]
reverse_complement=complement[::-1]
print("GC Percentage:",format((countgc/length)*100,".2f"))
print("AT Percentage:",format((countat/length)*100,".2f"))
print("Count of A:",counta)
print("Count of T:",countt)
print("Count of G:",countg)
print("Count of C:",countc)
print("Length Of DNA Sequence:",length)
print("RNA transcription:",rna)
print("Reverse Sequence:",reverse_sequence)
print("Complement Sequence:",complement)
print("Reverse Complement Sequence:",reverse_complement)
