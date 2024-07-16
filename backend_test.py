import boto3
import json


count = 0
word = ''

boto3.setup_default_session(profile_name='hangman-client')
client = boto3.client('bedrock-runtime', region_name="eu-west-2")

def main(prompt, message_history):

    global count
    global word
    model_id = 'meta.llama3-70b-instruct-v1:0'

    if count == 0:
        data2 = {
        "prompt": f"\n\nHuman: Pick a random object that you are confident you know a lot about. To do this, pick a random number from 1 to 10. If 1, pick an object; If 2, pick a food; If 3, pick an animal... . Return a one word answer that is just that word. DO NOT respond with more than a one word answer in quotation marks\n\nAssistant:",
        "temperature": 0.5,
        "max_gen_len": 512,
        "top_p": 0.9
        }

        input_data2 = json.dumps(data2)

        response2 = client.invoke_model(contentType='application/json', body=input_data2, modelId=model_id)
        inference_result2 = response2['body'].read().decode('utf-8')
        output2 = json.loads(inference_result2)
        
        word = (output2['generation'])

    print(word)

    data = {
    "prompt": f"\n\nHuman: The user is playing a game of 21 questions with you. This has been the game so far {message_history}, use this to determine how many yes or no questions the user has asked, if it is 21, then they have lost and state this. the word the user is trying to guess is {word}. The user will ask you yes or no questions about the object which you must answer truthfully. The user is also allowed to guess the object. You MUST NOT reveal or say {word} unless the user makes an explicit guess about {word}. If this happens, congratulate the user as they have won. This is the user's first question " + prompt + " \n\nAssistant:",
    "temperature": 0.5,
    "max_gen_len": 512,
    "top_p": 0.9
    }



    input_data = json.dumps(data)


    response = client.invoke_model(contentType='application/json', body=input_data, modelId=model_id)
    inference_result = response['body'].read().decode('utf-8')
    output = json.loads(inference_result)
    
    count += 1

    return (output['generation'])

    # user_message = f'''You are playing a game of hangman, and you have picked
    # the word sunshine, use the history to determine and the current guess here: {prompt} to determine
    # which letters are revealed'''


    

if __name__ == '__main__':
    output = main('e', 5)
    output = main('s', 5)
    
    