"""
Random gifts pairs generator.
If folder is provided, will output a text file for each person containing the receiverof the gift.
If not output folder provided, output to console.

Ludovic Herbelin
2020
"""

import random
import os
import copy
import sys
import argparse

n_stop = 1000

people = []

couples = []

# will check for directed constrain can't do person_1 -> person_2
directed_constraints = []

directed_constraints.extend([
])

def pop_random_item(l):
    id = random.randrange(0, len(l))
    return l.pop(id)

def get_padded_name(name, n_chars=None, padding_char=' '):
    if n_chars is None:
        n_chars = random.randint(1, 20)
        
    return ''.join((name, padding_char * n_chars))

def output_pairs(folder_output, pairs, source):
    if not folder_output:
        print(pairs)
    else:
        # save in files for the "secret"
        try:
            os.mkdir(folder_output)
        except Exception as e:
            print(f'Unable to create the folder "{folder_output}" : {e}')
            print(f'If folder existed already, program might overwrite some of the files.')

        for source, target in pairs:
            with open(f"{folder_output}/{source}.txt", 'w', encoding='utf-8') as f:
                f.write(get_padded_name(target))


def main():

    # for couples we can't do person_1 -> person_2 or person_2 -> person_1 either
    for p_1, p_2 in couples:
        directed_constraints.append((p_1, p_2))
        directed_constraints.append((p_2, p_1))
    


    # parse the console arguments (output folder)
    parser = argparse.ArgumentParser(description='Compute a random gift givers and receivers list')
    parser.add_argument("-o", '--output', help="Output folder, might overwrite existing files in it", required=False)
    args = parser.parse_args()
    
    try:
        folder_output = args.output
    except:
        folder_output = False


    # create a list of gift source and targets
    people_source = copy.deepcopy(people)
    people_target = copy.deepcopy(people)

    # in case there is a couple at the end, revert
    random.shuffle(people_source)
    random.shuffle(people_target)

    pairs = []

    i = 0
    while len(people_source) > 0 and i <= n_stop:
        source = pop_random_item(people_source)
        target = pop_random_item(people_target)
        
        # check so you don't give a gift to yourself
        if source == target:
            if len(people_source) == 0:
                people_source = copy.deepcopy(people)
                people_target = copy.deepcopy(people)
                pairs.clear()
            else:
                people_source.append(source)
                people_target.append(target)
            continue

        pair = (source, target)

        # check that the pair does not equal to a constraint
        if pair in directed_constraints:
            # if yes, revert the changes and start again

            # check that we don't arrive to a dead end (all others are picked except a pair which has a constraint)
            if len(people_source) == 0:
                people_source = copy.deepcopy(people)
                people_target = copy.deepcopy(people)
                pairs.clear()
            else:
                people_source.append(source)
                people_target.append(target)

            random.shuffle(people_source)
            random.shuffle(people_target)

        # if everything goes well
        else:
            pairs.append(pair)
        
        i += 1

    try:
        # check that we generated a gift possibility for everyone
        assert len(pairs) == len(people)     
    except AssertionError:
        print(f"Problem with the computation ! {len(pairs)} pairs found.")
        exit()

    sources = [pair[0] for pair in pairs]
    targets = [pair[1] for pair in pairs]

    # check that we don't have duplicates
    try:
        assert len(set(sources)) == len(sources)
        assert len(set(targets)) == len(targets)
    except AssertionError:
        print(f"Problem : duplicates in the gifts")
        exit()
        
    output_pairs(folder_output=folder_output, pairs=pairs, source=source)
    
    
if __name__ == '__main__':
    main()

 