import requests
import json

BASE_URL = ''
START_URL = BASE_URL + '/newgame'
WORD_LIST_URL = BASE_URL + '/wordlist.txt'
GUESS_URL = BASE_URL + '/guess'

word_list = []
game_id = None
char_set = set()

def start_game():
    url = START_URL
    x = requests.post(url)
    # print(x.text)
    x_json = json.loads(x.text)
    game_id = x_json['game_id']
    word = x_json['word']
    # print(game_id)
    # print(word)
    # print('start_game')
    list = [game_id, word]
    return list

def get_word_list():
    x = requests.get(WORD_LIST_URL)
    # print(x.status_code)
    # print(x.text)
    for word in x.text.split():
        word_list.append(word)
    return word_list
    # print('get_word_list')

def make_freq_table(word_list):
    freq_table = {}
    for word in word_list:
        for char in word:
            if char in freq_table:
                freq_table[char] += 1
            else:
                freq_table[char] = 1
    return freq_table

def make_length_table(word_list):
    length_table = {}
    for word in word_list:
        if len(word) in length_table:
            length_table[len(word)].append(word)
        else:
            length_table[len(word)] = []
            length_table[len(word)].append(word)
            
    return length_table


def guess_char(game_id, char):
    
    post_arg = {
        "game_id": str(game_id),
        "guess": char
    }
    # print(post_arg)
    try:
        x = requests.post(GUESS_URL, data = json.dumps(post_arg))
    except Exception as e:
        print(e)
    # print(x.text)
    # print('guess_char')

    return json.loads(x.text)

def guess_rest_of_chars(game_id, char, word_list, position):
    new_list = []
    for word in word_list:
        if word[position] == char:
            new_list.append(word)
    
    freq_table = make_freq_table(new_list)
    for w in sorted(freq_table, key=freq_table.get, reverse=True):
        guess = guess_char(game_id, w)
        char_set.add(char)
        break

    return guess

def guess_the_word():
    word_list = []
    game_id = None
    list = start_game()
    
    game_id = list[0]
    empty_word = list[1]

    word_list = get_word_list()
    length_table = make_length_table(word_list)
    # print(empty_word)
    # print(len(empty_word))
    # print(len(word_list))
    freq_table = make_freq_table(length_table[len(empty_word)])
    
    # print(length_table)

    # counter = 0
    
    counter = None

    # print(freq_table)
    for w in sorted(freq_table, key=freq_table.get, reverse=True):
        # print(w, freq_table[w])
       
        guess = guess_char(game_id, w)
        char_set.add(w)
        
        if 'strikes' in guess:
            # print(guess['strikes'])
            word = guess['word']
            print(word)
            counter = 0
            for char in word:
                
                if char != '_' and char not in char_set:
                    print(str(counter) + str(char))
                    guess = guess_rest_of_chars(game_id, char, length_table[len(empty_word)], counter)
                    word = guess['word']
                counter = counter + 1        
        else:
            # print(guess)
            return guess
            # guess = guess_char(game_id, w)
            break

    # for  word in word_list:
    # return
if __name__ == "__main__":

    counter_lost = 0
    counter_win = 0

    for i in range(100):
        guess = guess_the_word()
        # print(guess)
        if guess['message'] == "Game over! You lost.":
            counter_lost += 1
            print('Lose')
        elif guess['message'] == "You win!":
            counter_win += 1
            print('Win')

    print(str(counter_lost))
    print(str(counter_win))      


    # guess_char(game_id, "s")
