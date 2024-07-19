import boto3
import json
from random import choice
from objectlist import rand_word


count = 1
word = ''
otto = False

boto3.setup_default_session(profile_name='21-questions')
client = boto3.client('bedrock-runtime', region_name="eu-west-2")

def main(prompt, message_history):

    global count
    global word
    llama_model_id = 'meta.llama3-70b-instruct-v1:0'

    if count == 1 and otto == False:  
        word = rand_word()

    current_prompt = ''
    llama_gameprompt = f"""<|begin_of_text|><|start_header_id|>system<|end_header_id|>
                    The user is playing a game of 21 questions with you. 
                    This has been the game so far {message_history}.
                    You are current on the {count + 1}th question (since they will move onto the 2nd question once you have responded to their initial prompt),
                    so DISPLAY on each response that the user is on the {count + 1}th question. Display this at the end of the message on a seperate line.
                    the word the user is trying to guess is {word}.
                    The user will ask you yes or no questions about the object which you must answer truthfully.
                    Only deliver information about the question through a simple yes or no and nothing else.
                    The questions will be about the object so answer as best as you can. 
                    The user is also allowed to guess the object. 
                    You MUST NOT reveal or say {word} unless the user makes an explicit guess about {word}.
                    When answering yes or no, include in your response what you interpreted by their question, put this on a seperate line
                    If this happens and the users makes a guess asking if it is {word}, do not just respond with yes but also congratulate the user as they have won.
                    Tell them that they guessed the word in {count} questions and don't display which question they are on.
                    This is the user's first question <|eot_id|>
                    <|start_header_id|>user<|end_header_id|> 
                    {prompt}<|eot_id|> 
                    <|start_header_id|>assistant<end_header_id|>""", 
    
   
   

    current_prompt = llama_gameprompt

    llama_data = {
    "prompt": f"\n\nHuman: {current_prompt}\n\nAssistant:",
    "temperature": 0.9,
    "max_gen_len": 512,
    "top_p": 0.9
    }


    current_data = llama_data
    current_model = llama_model_id


    if count == 22:
        count = 1
        holdword = word
        return (f'Unlucky, you did not get the word, the word was: {holdword}!')
    

    print(prompt)

    input_data = json.dumps(current_data)

    if prompt.lower() == 'retry':
        
        count = 1
        otto = False
        return("SYSTEM RESTARTING GAME\nNEW WORD GENERATED: TRUE\n Please ask your 1st Question")
    
    elif prompt.lower() == 'otto':
        otto = True
        return(word)

    else:

        response = client.invoke_model(contentType='application/json', body=input_data, modelId=current_model)
        inference_result = response['body'].read().decode('utf-8')
        output = json.loads(inference_result)
        otto = False
        count += 1

        print(count)
        print(output['generation'])

        return (output['generation'])




    

    # user_message = f'''You are playing a game of hangman, and you have picked
    # the word sunshine, use the history to determine and the current guess here: {prompt} to determine
    # which letters are revealed'''


    

if __name__ == '__main__':
    output = main('e', 5)
    output = main('retry', 5)
    print(output)
    
    