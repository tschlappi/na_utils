"""
Convert DNA sequences to RNA.
"""

def rna(seq):
    """Convert a DNA sequence to RNA."""

    #Determine if the original sequence was uppercase
    seq_upper = seq.isupper()

    #Convert to lowercase
    seq = seq.lower()

    #Swap out 't' for 'u'
    seq = seq.replace('t','u')

    #Return upper or lower, depending on input
    if seq_upper:
        return seq.upper()
    else:
        return seq

def reverse_rna_complement(seq):
    """Convert a DNA sequence into its reverse complement as RNA"""

    #Determine if the original sequence was uppercase
    seq_upper = seq.isupper()

    #Reverse sequence
    seq = seq[::-1]

    #Convert to uppercase
    seq = seq.upper()

    #Compute complement
    seq = seq.replace('A','u')
    seq = seq.replace('T','a')
    seq = seq.replace('G','c')
    seq = seq.replace('C','g')

    #Return in appropriate case
    if seq_upper:
        return seq.upper()
    else:
        return seq
