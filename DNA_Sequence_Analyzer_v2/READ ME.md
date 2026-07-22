# DNA Analyzer V2

## Description

DNA Analyzer V2 is a Python program that performs basic DNA sequence analysis. It validates DNA sequences, calculates nucleotide statistics, converts DNA to RNA, generates complementary sequences, and detects start and stop codons.

---

## Features

- Validate DNA sequences (A, T, G, C only)
- Calculate DNA sequence length
- Count the number of A, T, G, and C nucleotides
- Calculate GC percentage
- Calculate AT percentage
- Generate the RNA transcript
- Generate the reverse DNA sequence
- Generate the complementary DNA sequence
- Generate the reverse complement sequence
- Detect the start codon (ATG)
- Detect stop codons (TAA, TAG, and TGA)

---

## Example

### Input

```text
Enter The DNA Sequence:
ATGCGCTAA
```

### Output

```text
Start Codon Found (ATG) at Position 1
Stop Codon Found (TAA) at Position 7

GC Percentage: 44.44
AT Percentage: 55.56

Count of A: 3
Count of T: 2
Count of G: 2
Count of C: 2

Length Of DNA Sequence: 9

RNA Transcription: AUGCGCUAA
Reverse Sequence: AATCGCGTA
Complement Sequence: TACGCGATT
Reverse Complement Sequence: TTAGCGCAT
```
