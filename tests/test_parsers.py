# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser,
        )


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    TODO: Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
 

    aparser = FastaParser('test1.fa')
    for line in aparser:
        assert type(line) == tuple
        assert line[0][:4] == '>seq'
        assert type(line[1][:4])== str
        
        
        
    
    

def test_FastqParser():
    """
    TODO: Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    aparser = FastqParser('test1.fq')
    for line in aparser:
        assert type(line) == tuple
        assert line[0][:5] != ">"
        assert type(line[1][:4]) == str
        assert type(line[2][:4]) == str
        
       

