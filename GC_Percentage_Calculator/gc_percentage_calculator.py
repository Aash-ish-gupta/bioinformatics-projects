sequence=input("Enter Sequence:").upper()
count=0
for gc in sequence:
    if  gc=='G' or gc=='C':
        count=count+1
lenght=len(sequence)
GC=(count/lenght)*100
print("GC% Of The Given Sequence Is:",GC)
