# Read DNA sequence from user
dna = "acgctcgcgcggcgatagctgatcgatcggcgcgctttttttttaaaag"

# Count the number of Cs in the DNA sequence
no_c = dna.count('c')

# Count the number of Gs in the DNA sequence
no_g = dna.count('g')

# Determine the length of DNA sequence
len_dna = len(dna)

# Compute GC%
gc_percent = ((no_c + no_g) / len_dna) * 100
print(f'GC percent: {gc_percent:.2f} %')