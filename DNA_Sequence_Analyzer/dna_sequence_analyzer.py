sequence=input("Enter The DNA Sequence:").upper()
countgc=0
countat=0
counta=0
countt=0
countg=0
countc=0
length=len(sequence)
if length == 0:
    print("DNA sequence cannot be empty.")
    quit()

for base in sequence:
    if base not in ['A','T','G','C']:
        print("Invalid base:",base)
        print("Invalid Sequence(quitting program...)")
        quit()
        
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
        
print("GC Percentage:",countgc/length*100)
print("AT Percentage:",countat/length*100)
print("Count of A:",counta)
print("Count of T:",countt)
print("Count of G:",countg)
print("Count of C:",countc)
print("Length Of DNA Sequence:",length)
