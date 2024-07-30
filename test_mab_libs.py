from mad_libs import get_adjective, get_verb, get_noun, get_graduate_name, get_verb_with_ing
import pytest
import random

def test_get_adjective():
    '''Test that the get_adjective
       function works properly.
       
       Parameters:None
       Returns:Nothing
    '''
    if get_adjective == ['pleased','happy','sad','big','angry','beautiful','breakable','fat']:
       assert get_adjective('adjective')==['pleased','happy','sad','big','angry','beautiful','breakable','fat']

def test_get_verb():
    ''' 
       Test that the get_verb funtion works properly

       Parameters:None
       Retuns:Nothing
    '''
    if get_verb==['go','come','eat','fly','speak','shout','walk','run']:
        assert get_verb('verb')==['go','come','eat','fly','speak','shout','walk','run']

def test_get_noun():
    '''
    Test that the get_noun function works properly

    Parameters:None
    Returns:Nothing
    '''
    if get_noun==['cat','dog','america','hospital','angie','china','stone']:
        assert get_noun('noun')==['cat','dog','america','hospital','angie','china','stone']

def test_get_graduate_name():
    '''
    Test that the get_graduate_funtion works properly

    Parameters:None
    Returns:Nothing
    '''
    if get_graduate_name==['william','derick','prince','edward','charlotte','thomas','conner','kim']:
        assert get_graduate_name('names')==['william','derick','prince','edward','charlotte','thomas','conner','kim']

def test_get_verb_with_ing():
    '''
    Test if the get_verb_with_ing works properly

    Parameters:None
    Returns:Nothing
    '''
    if get_verb_with_ing==['flying','eating','swimming','jumping','crying','shooting','working']:
        assert get_verb_with_ing('verbs')==['flying','eating','swimming','jumping','crying','shooting','working']


pytest.main(["-v", "--tb=line", "-rN", __file__])