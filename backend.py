import ollama


count = 0
user_history = ''
chat_history = ''
word = ''

def main(prompt, history):

    global count
    global word
    global user_history
    global chat_history
    
    for array in history:
        array_count = 1
        for word in array:
            if array_count == 1:
                user_history += (word + ' , ')
                array_count += 1
            else:
                chat_history += (word + ' , ')

    response = ollama.generate(model='mistral', prompt=
        
            '''You are a random word generator whos only purpose is to return a SINGLE WORD.
            Be creative with your word choice, you can choose any one word in the english language.
            It could be very complicated or very simple.
            Do not choose the word SERENDIPITY.
            Do not make up random words.
            Do not try to think of complicated words for the sake of it e.g. 'Zephyr' or 'Whimsicality'
            Do pick normal words that are used often e.g. Truck , Kitty , Transport
            Pick simplicity over complexity
            Perform this function returning one word in quotation marks'''
        
    )

    if count == 0:
        word = response['response']

    print(word)
    print(user_history)

    initial_prompt = f'''
    KEEP THIS WORD HIDDEN AND DO NOT MENTION IT WHATSOEVER: {word}.
    When a user guesses from one of 26 letters, only now reveal information about that ONE letter in relation to the word
    Reveal the follow letters if they are in the word: {user_history}, {prompt}
    You are playing against the person guessing letters and you are not to help them in anyway or participate.
    '''
    

    # if count == 0:
    #     message_prompt = initial_prompt
    # else:
    #     message_prompt = f'''
    #     We are playing a game of hang man, so far the user has guessed {user_history} where the guessed have been seperated by the | character.
    #     Your history as the chatbot has been {chat_history}. Continue the game with the rules, remembering the lives that the user has.
    #     This is the user's input for the current move: {prompt}.
    #     '''


    game = ollama.chat(model='mistral', messages=[
        {
            'role': 'user',
            'content': initial_prompt,
        },
    ])

    
    count += 1
    return ("AI: \n" + game['message']['content'])

if __name__ == '__main__':
    main()