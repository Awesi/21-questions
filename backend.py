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
                user_history += (word + ' | ')
                array_count += 1
            else:
                chat_history += (word + ' | ')

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

    initial_prompt = f'''
    Conversation history so far {chat_history}
    YOU, the chatbot are a gamemaster for the game hangman.
    Your word is {word}.
    Keep it a secret displaying a number of adjacent asterixes equal to the number of letters in the word.
    so if there were 5 letter in {word}, then do *****, and if the were 6 letter in {word}, then do ******
    This will be known as the hidden word
    The user has a number of lives starting at 5.
    Check the user history here: {user_history}. to determine the current amount of lives.
    For each unique letter in the user history that is not in the word, subtract one from the amount of lives.
    When the amount of lives equals 0, the game is over and the user has lost. 
    Prompt the user to restart the program to play again
    The user will either enter letters individually or will guess the word straight up
    When a letter is entered (or if it is a letter in {user_history}), if the letter is in {word}.
    Display in the hidden word where those letter would be as if they where in the {word} itself.
    e.g. if the word was carrot and the user history was ' a | c | ' then the current output would be ca****
    If the user guesses a word, if this word = {word}, they have won the game, otherwise, subtract a life

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
    return (game['message']['content'])

if __name__ == '__main__':
    main()