import boto3
import json


count = 0

boto3.setup_default_session(profile_name='hangman-client')
client = boto3.client('bedrock-runtime', region_name="eu-west-2")

def main(prompt, message_history):

    global count
    model_id = 'meta.llama3-70b-instruct-v1:0'

    data = {
    "prompt": f"\n\nHuman: You are playing a game of hangman, and you have picked the word sunshine. Don't give the python code, play as the gamemaster. Create a variable called hidden word made up of 8 '*'s. Use the history (here: {message_history}) and the current guess here: {prompt} as the letters and words guessed. Out of the letters guessed, reveal all instances on them in the hidden word at the correct index. e.g, if s was guessed and the word was sunshine, since it appears in the 0th and 3rd index in the word, fill out the 0th and 3rd index of hidden word with s\n\nAssistant:",
    "temperature": 0.5,
    "max_gen_len": 512,
    "top_p": 0.9
    }

    if count == 0:
        data2 = {
        "prompt": f"\n\nHuman: Pick a random object that you are confident you know a lot about\n\nAssistant:",
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
    print(output)