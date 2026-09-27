# DNA to RNA Converter

This Python program converts a **DNA sequence into an RNA sequence** by replacing **thymine (T)** with **uracil (U)**.

## Features

* Accepts a DNA sequence from the user.
* Automatically converts the input to uppercase.
* Checks if the sequence is empty.
* Validates that the sequence contains only valid DNA bases: **A, T, G, and C**.
* Converts the DNA sequence to RNA by replacing:

  * `T → U`
  * `A → A`
  * `G → G`
  * `C → C`
* Displays the resulting RNA sequence.

## How It Works

The program first asks the user to enter a DNA sequence:

```text
Enter Dna Sequence:
```

It then checks whether the sequence is valid. If an invalid base is detected, the program exits with an error message.

For a **coding DNA sequence**, the RNA conversion is performed using:

```python
dna_sequence.replace("T", "U")
```

### Example

**Input:**

```text
ATGCCATTA
```

**Output:**

```text
DNA to RNA Conversion: AUGCCAUUA
```

## Requirements

* Python 3.x

No external libraries are required.

## Purpose

This project is a basic bioinformatics program designed to demonstrate **DNA-to-RNA transcription concepts** and fundamental Python programming concepts such as:

* User input
* Strings
* Conditional statements
* `for` loops
* Validation
* String replacement
* Program termination
