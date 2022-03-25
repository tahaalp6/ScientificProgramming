import random
import sys
import re

def process_line(line):
    if len(line) == 0:
        return ()
    tuple = ()
    split_lines = line.strip().split(" ")
    for i in range(len(split_lines)):

        if i==0 and len(split_lines) == 1:
            return (*tuple, ('BEGIN',split_lines[i]))
        
        if i == 0:
            tuple = (*tuple, ('BEGIN', split_lines[i]+ ' ' + split_lines[i+1]))
        elif i==len(split_lines)-1:
            tuple = (*tuple, (split_lines[i-1] + ' ' + split_lines[i],'END'))
        # elif i==len(split_lines)-2:
        #     tuple = (*tuple, (split_lines[i],split_lines[i+1]))
        else:
            tuple = (*tuple, (split_lines[i-1] + ' ' + split_lines[i],split_lines[i+1]))
    return tuple



def process_textfile(filename):
    '''
    Creates a dictionary with transition pairs
    based on a file provided

    For the first part of the assignment, we use a
    placeholder text that you will have to replace
    at some point.

    Based on the placeholder text, the dictionary
    should contain the following key-value pairs:

    'blue,': ['END']
    'by': ['yellow', 'day.', 'day?']
    'still': ['hopping', 'going']
    '''
    d = {}

    # Placeholder until we add File I/O in part two
    # Overwrite the following lines with your code:
    file = open("./data/"+filename, "r")
    read_data = file.read().replace("\n","").replace("\r\n","")
    read_data = re.sub(r'\\u.{4}', '',read_data)
    read_data = re.sub(r'\\x.{2}', '',read_data)
    
    f = read_data.split('.')
    # text from http://www.bygosh.com/Features/082000/rhymes.htm
    
    # YOUR CODE HERE #
    for line in f:
        for word in process_line(line):
            if word[0] in d:
                d[word[0]].append(word[1])
            else:
                d[word[0]] = [word[1]]
    return d

def generate_line(d):
    '''
    Generates a random sentence based on the dictionary
    with transition pairs

    Note that the first state is BEGIN but that we
    obviously do not want to return BEGIN

    Some sample output based on the placeholder text:
    'i have to go to go to go to go to play,'

    Hint: use random.choice to select a random element from a list
    '''

    # YOUR CODE HERE #
    sentence = ''
    tmp = 'BEGIN'
    size = len(d[tmp])
    #print(d.keys())
    tmp = d[tmp][random.randint(0,size-1)]
    #print(tmp)
    # for  i in list(d["BEGIN"]):
    #     size = len(i.split(" "))
    #     if(size< 2):
    #         print(f"Key {i} - Size : {size}")

    while 'END' not in tmp:
        #print(f"D-{d}")
        #print(f"tmp-{tmp}")
        if(tmp not in d):
            return sentence
        size = len(d[tmp])
        tmp_split = tmp.split(" ")
        sentence += tmp_split[0]
        sentence += ' '
        tmp = tmp_split[1] + ' ' + d[tmp][random.randint(0,size-1)]
    return sentence

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('ERROR: Run as python markov.py <filename>')
        exit()

    d = process_textfile(sys.argv[1])
    print(generate_line(d))