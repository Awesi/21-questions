import boto3
import json
from random import choice
from objectlist import rand_word


count = 0
word = ''

boto3.setup_default_session(profile_name='hangman-client')
client = boto3.client('bedrock-runtime', region_name="eu-west-2")

def main(prompt, message_history):

    global count
    global word
    model_id = 'meta.llama3-70b-instruct-v1:0'

    current_prompt = ''
    gameprompt = f"The user is playing a game of 21 questions with you. This has been the game so far {message_history}. If this number {count} is 21, the user has lost, state this, you are current on the {count}th questions, so display this, return to 0 if retry is entered by the user. the word the user is trying to guess is {word}. The user will ask you yes or no questions about the object which you must answer truthfully. The user is also allowed to guess the object. You MUST NOT reveal or say {word} unless the user makes an explicit guess about {word}. If this happens, congratulate the user as they have won. This is the user's first question " + prompt, 
    checkprompt = f"Look at this word: {word}, if you think it is an umbrella term, return True, otherwise, return false. ONLY RETURN A SINGLE WORD, EITHER TRUE OR FALSE. DO NOT RETURN MORE THAN ONE WORD"

    data = {
    "prompt": f"\n\nHuman: {current_prompt}\n\nAssistant:",
    "temperature": 0.9,
    "max_gen_len": 512,
    "top_p": 0.9
    }

    if count == 0:  
        word = rand_word()

    if prompt.lower() == 'retry':   
        count = 0
        print(count)
        word = rand_word()

    if count == 22:
        count = 0
        holdword = word
        word = rand_word()
        return (f'Unlucky, you did not get the word, the word was: {holdword}!')
    
    print(word)

    current_prompt = gameprompt

    data = {
    "prompt": f"\n\nHuman: {current_prompt}\n\nAssistant:",
    "temperature": 0.9,
    "max_gen_len": 512,
    "top_p": 0.9
    }



    input_data = json.dumps(data)


    response = client.invoke_model(contentType='application/json', body=input_data, modelId=model_id)
    inference_result = response['body'].read().decode('utf-8')
    output = json.loads(inference_result)
    
    count += 1

    print(count)

    if prompt.lower != 'retry':
        return (output['generation'])

    # user_message = f'''You are playing a game of hangman, and you have picked
    # the word sunshine, use the history to determine and the current guess here: {prompt} to determine
    # which letters are revealed'''


    

if __name__ == '__main__':
    output = main('e', 5)
    output = main('s', 5)
    
    