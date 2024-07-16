import boto3
import json

boto3.setup_default_session(profile_name='hangman-client')
client = boto3.client('bedrock-runtime', region_name="eu-west-2")

def main(prompt, message_history):

    data = {
    "prompt": f"\n\nHuman: You are playing a game of hangman, and you have picked the word sunshine. Use the history (here: {message_history}) and the current guess here: {prompt} to determine which letters are revealed\n\nAssistant:",
    "temperature": 0.5,
    "max_gen_len": 512,
    "top_p": 0.9
    }

    input_data = json.dumps(data)

    model_id = 'meta.llama3-70b-instruct-v1:0'

    response = client.invoke_model(contentType='application/json', body=input_data, modelId=model_id)
    inference_result = response['body'].read().decode('utf-8')
    output = json.loads(inference_result)
    
    return (output['generation'])

    # user_message = f'''You are playing a game of hangman, and you have picked
    # the word sunshine, use the history to determine and the current guess here: {prompt} to determine
    # which letters are revealed'''


    

if __name__ == '__main__':
    output = main('e', 5)
    print(output)