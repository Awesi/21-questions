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
    global otto
    claude_model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'

    if count == 1 and otto == False:  
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
                    When answering yes or no, include in your response what you interpreted by their question,
                    put this on a seperate line at the beginning of the message. 
                    If {word}, is used in your interpretation, instead refer to it as 'the object' 
                    If the user makes a guess asking if it is {word}. In this case, you can reveal that they are correct and that they have won the game.
                    e.g. 'User: Is it {word}' or 'User: Is the object {word}'. In this case, do the congratulation process.
                    Also, If the interpreted question is 'Is the object {word}' then do the same thing and congratulate the user telling them that they have won
                    You must do this and NOT just say No but say yes. e.g. word = glasses 'User: is the object glasses' or 'AI: Yes it is, congratulations'
                    Tell them that they guessed the word in {count} questions and don't display which question they are on.
                    This is the user's first question: {prompt}""",

    hint_prompt = f""" The user is playing a game of 21 questions with you. 
            This has been the game so far {message_history}.
            You are called upon as the game master to deliver a brief and vague hint about the object {word}.
            You should only mention ONE thing about this object such as one of the following: where you would find it, a cryptic description of its purpose, its normal/usual colour  to suggest a few
            The response should be 1 word and should only describe one thing about the object. This word MUST NOT BE IN {message_history}
            The response should be vague. For examples, if the word was watch, model answer: 'item mostly worm for style', bad answer: 'keeps track of time passing'.
            DO NOT MENTION {word} in any part of your response. """

    current_prompt = claude_gameprompt
        

    if count == 22:
        count = 1
        holdword = word
        otto = False
        return (f'Unlucky, you did not get the word, the word was: {holdword}!')
    
    print(prompt)

    if prompt.lower() == 'retry':
        
        count = 1
        otto = False
        return("SYSTEM RESTARTING GAME\n\nNEW WORD GENERATED: TRUE\n\n Please ask your 1st Question")
    
    elif prompt.lower() == 'otto':
        otto = True
        return(word)

    else:

        if prompt.lower() == 'hint':
            current_prompt = hint_prompt


        conversation = [
            {
                "role": "user",
                "content":[{"text": str(current_prompt)}],
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
        otto = False

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
    
    