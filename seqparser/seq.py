# DNA -> RNA Transcription


def transcribe(seq: str) -> str:
    """
    TODO: transcribes DNA to RNA by generating
    the complement sequence with T -> U replacement
    """
    # Create a dictionary to transcribe DNA to RNA
    dna_to_rna={'A':'U',
                'T':'A',
                'C':'G',
                'G':'C'}
    rna_seq='' # make an empty string to append RNA sequences into it.
    for base in seq: # for loop to iterate through each base in seq
       rna_seq+=(dna_to_rna[base]) # concatenate rna seq after transcribing dna seq
    return rna_seq # return stops the function and gives output after printing

dna_seq='TAGC' # assign dna_seq with a string input
seq=transcribe(dna_seq) # call the function with dna_seq as an argument
print(seq)
 


    
def reverse_transcribe(seq: str) -> str: # the function transcribes dna seq to rna seq and then reverses rna seq as string
    seq=transcribe(seq) # transcribe dna to rna
    reversed_seq=seq[::-1] # reverse rna seq. reverse() method doesn't work on str type input
    return reversed_seq 
dna='ATCG' # assigned input to dna seq
reversed_seq=reverse_transcribe(dna) # calling the function
print(reversed_seq)

     

 


   
    
    
    
   
        