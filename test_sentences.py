from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

    
def test_get_noun():
    ''' Test if the get_noun function is correct
        Parameters:None
        Return:None
    '''
    # Test the single nouns
    single_nouns=['bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl', 'man', 'rabbit', 'woman']

    for _ in range(11):
        word=get_noun(1)

    assert word in single_nouns

    # Test the plural nouns
    plural_nouns=['birds', 'boys', 'cars', 'cats', 'children', 'dogs', 'girls', 'men', 'rabbits', 'women']

    for _ in range(11):
        word=get_noun(2)

    assert word in plural_nouns


def test_get_verb():
    '''Test the get_verb function if it's correct
       Parameters:None
       Return:None
    '''
    # Test the past verbs
    past_tense_words=['drank', 'ate', 'grew', 'laughed', 'thought', 'ran', 'slept', 'talked', 'walked', 'wrote']

    for _ in range(11):
        word=get_verb(1, 'past')

    assert word in past_tense_words

    # Test the present single verbs
    present_single_verbs=['drinks', 'eats', 'grows', 'laughs', 'thinks', 'runs', 'sleeps', 'talks', 'walks', 'writes']

    for _ in range(11):
        word=get_verb(1, 'present')

    assert word in present_single_verbs

    # Test the present plural verb
    present_plural_verbs=['drink', 'eat' 'grow', 'laugh', 'think', 'run', 'sleep', 'talk', 'walk', 'write']

    for _ in range(11):
        word=get_verb('words', 'present')

    assert word in present_plural_verbs

    # Test the future plural verb

    future_plural_verb=['will drink', 'will eat', 'will grow', 'will laugh', 'will think', 'will run', 'will sleep', 'will talk', 'will walk', 'will write']

    for _ in range(11):
        word=get_verb('words', 'future')

    assert word in future_plural_verb


def test_get_preposition():
    '''Test if the get_preposition function is correct'''

       
 #test for prepositions

    prepositions=['about', 'above', 'across', 'after', 'along',
           'around', 'at', 'before', 'behind', 'below',
           'beyond', 'by', 'despite', 'except', 'for',
           'from', 'in', 'into', 'near', 'of',
           'off', 'on', 'onto', 'out', 'over',
           'past', 'to', 'under','with', 'without']
    
    for _ in range(31):
        word=get_preposition()

        assert word in prepositions 

def test_get_prepositional_phrase():
    '''Test if the get_prepositional_phrase is correct'''

    phrase = get_prepositional_phrase(1).split(' ')
    assert len(phrase) == 3


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])