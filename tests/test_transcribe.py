# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    TODO: Write your unit test for the
    transcribe function here.
    """

    # Testing to see if transcribe is working properly
    base1 = 'A'
    base2 = 'C'
    base3 = 'AG'
    # Converts A to U 
    assert transcribe(base1) == 'U'
    # Converts C to G
    assert transcribe(base2) == 'G' # converts C to G
    assert transcribe(base2) != 'T' # converts C to G, not T. 
    assert transcribe(base3) == 'UC' # converts AG to UC



def test_reverse_transcribe():
    """
    TODO: Write your unit test for the
    reverse transcribe function here.
    """
    base1='CA'
    base2='CG'
    assert reverse_transcribe(base1) == 'UG' # convert 'CA' to 'GU' and inverse it to 'UG'
    assert reverse_transcribe(base2) == 'CG'  # convert 'CG' to 'GC' and inverse it to'CG'
    
