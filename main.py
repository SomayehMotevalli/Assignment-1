from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    TODO: The main function
    """
    # Create instance of FastaParser
    aparser = FastaParser('data/test.fa') # aparser is an instance
    # Create instance of FastqParser
        
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    parser_obj = FastaParser('data/test.fa')
    for header,sequence in parser_obj:
        print(header)
        print(transcribe(sequence))
    parser_obj = FastaParser('data/test.fa')
    for record in parser_obj:
        header,sequence=record
        seq=sequence
        seq=transcribe(seq)
        reversed_seq=seq[::-1]
        print(reversed_seq)
       
        
   



        
            
    aparser = FastqParser('data/test.fq')
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    
    parser_obj = FastqParser('data/test.fq')
    for record in parser_obj:
        header,sequence,quality=record
        seq=transcribe(sequence)
        reversed_seq=seq[::-1]
        print(reversed_seq)
     
     

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
