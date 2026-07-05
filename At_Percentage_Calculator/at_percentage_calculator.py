sequence=input("Enter Sequence:").upper()
count=0
for at in sequence:
    if  at=='A' or at=='T':
        count=count+1
lenght=len(sequence)
AT=(count/lenght)*100
print("AT% Of The Given Sequence Is:",AT)
