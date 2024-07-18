import boto3
import json
from random import choice
from objectlist import rand_word


count = 1
word = ''

boto3.setup_default_session(profile_name='21-questions')
client = boto3.client('bedrock-runtime', region_name="eu-west-2")

def main(prompt, message_history):

    global count
    global word
    claude_model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'

    if count == 1:  
        word = rand_word()

    claude_gameprompt = f""" The user is playing a game of 21 questions with you. 
                    This has been the game so far {message_history}.
                    You are current on the {count + 1}th question (since they will move onto the 2nd question once you have responded to their initial prompt),
                    so DISPLAY on each response that the user is on the {count + 1}th question. Display this at the end of the message on a seperate line.
                    the word the user is trying to guess is {word}.
                    The user will ask you yes or no questions about the object which you must answer truthfully.
                    Only deliver information about the question through a simple yes or no and nothing else.
                    The questions will be about the object so answer as best as you can. 
                    The user is also allowed to guess the object. 
                    You MUST NOT reveal or say {word} unless the user makes an explicit guess about {word}.
                    When answering yes or no, include in your response what you interpreted by their question, put this on a seperate line at the beginning of the message
                    If this happens and the users makes a guess asking if it is {word}, do not just respond with yes but also congratulate the user as they have won.
                    You must do this and not just say No.
                    Tell them that they guessed the word in {count} questions and don't display which question they are on.
                    This is the user's first question: {prompt}""",


  
        

    if count == 22:
        count = 1
        holdword = word
        return (f'Unlucky, you did not get the word, the word was: {holdword}!')
    
    print(prompt)

    if prompt.lower() == 'retry':
        
        count = 1
        return("SYSTEM RESTARTING GAME\nNEW WORD GENERATED: TRUE\n Please ask your 1st Question")
    
    elif prompt.lower() == 'otto':
        return(word)

    else:

        conversation = [
            {
                "role": "user",
                "content":[{"text": str(claude_gameprompt)}],
            }
        ]

        response = client.converse(
            modelId=claude_model_id,
            messages=conversation,
            inferenceConfig={"maxTokens":4096,"temperature":0},
            additionalModelRequestFields={"top_k":250}
        )

        response_text = response["output"]["message"]["content"][0]["text"]

        count += 1

        print(count)
        print(response_text)

        return (response_text)




    

    # user_message = f'''You are playing a game of hangman, and you have picked
    # the word sunshine, use the history to determine and the current guess here: {prompt} to determine
    # which letters are revealed'''


    

if __name__ == '__main__':
    output = main('e', 5)
    output = main('retry', 5)
    print(output)
    
    