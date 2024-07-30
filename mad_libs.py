import random

def main():
    
    adjectives=get_adjective('adjective')
    verbs=get_verb('verb')
    names=get_graduate_name('names').capitalize()
    verbs_ing=get_verb_with_ing('verbs')
    noun=get_noun('noun')
    print()
    print(f'This is a Mab lib graduation message.')
    print()

    print(f'Dear {names},\n')
    print(f'I am {adjectives} and {adjectives} to tell you that you simply have passed your graduation')
    print(f'with flying colors. Acccept my {adjectives} congratulations on your success.')
    print(f'I am overjoyed that you are {verbs_ing} the {noun} of your labor.')
    print(f'Keep {verbs_ing} hard. This wont definitely be the last time i get to {verbs} about you.')
    print(f'We know you have got it achieved due to your {noun} and {noun}. I know you will do well in')
    print(f'your {adjectives} work if you maintain the {noun} you demonstrated in school. Always remeber:')
    print(f'There is no {noun} to what you can do if you keep {verbs_ing} in yourself.')
    print(f'It took a lot of {adjectives} work to reach this goal. You had to show up everyday, whether')
    print(f'you {verbs} like it or not. You had {noun} in your head. You have {noun} in your shoes.')
    print(f'You can steer yourself in any direction you choose. You are the only person who will {verbs}')
    print('where you go.')
    print('Love')
    print(f'{names}.')


# This function gets an adjective from a list of adjectives.
def get_adjective(adjective):
    '''Chooses and returns a random 
       adjective from a list or adjectives.
    '''
    '''
       Parameter
       adjective:They are words that modifies or describes a noun.

       Return:
       An adjective from a list of adjectives. 
    '''
    adjective=['pleased','happy','sad','big','angry','beautiful','breakable','fat']
    word=random.choice(adjective)
    return word


# This function gets a verb from a list of verbs.
def get_verb(verb):
    '''Chooses and return a random
       verb from a list of verbs

       Parameter:
       verb:A doing word or an action word

       Return:
       A verb from a list of verbs
    '''
    verb=['go','come','eat','fly','speak','shout','walk','run']
    word=random.choice(verb)
    return word


# This function gets a name from a list of names.
def get_graduate_name(names):
    '''
       Chooses and return a random
       name from a list of names

       Parameter:
       names:names of a graduant

       Return:
       A name from a list of names
    '''
    names=['william','derick','prince','edward','charlotte','thomas','conner','kim']
    word=random.choice(names)
    return word


# This function gets a verb ending with an ing from a list of verbs.
def get_verb_with_ing(verbs):
    '''
      Chooses and returns a random
      verb ending with ing from a list of verbs

      Parameter:
      verbs:verbs ending with ing

      Return:
      A verb ending with ing.
    '''
    verbs=['flying','eating','swimming','jumping','crying','shooting','working']
    word=random.choice(verbs)
    return word



# This function gets a noun from a list of noun.
def get_noun(noun):
   '''
      Chooses and return a random noun
      from a list of nouns

      Parameter:
      A noun is a name of a person, place or an item

      Return:
      A noun from a list of nouns
   '''
   noun=['cat','dog','america','hospital','angie','china','stone']
   word=random.choice(noun)
   return word

if __name__ =="__main__":
    main()
