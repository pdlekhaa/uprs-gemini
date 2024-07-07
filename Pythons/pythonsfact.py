import vertexai
from google.cloud import aiplatform_v1
from google.cloud import aiplatform
import vertexai.preview
import csv
from vertexai import preview
from vertexai.preview.generative_models import GenerativeModel, Part
import time
from vertexai.generative_models._generative_models import ResponseBlockedError

aiplatform.init(
    # your Google Cloud Project ID or number
    # environment default used is not set
    project='urps-411903',

    # the Vertex AI region you will use
    # defaults to us-central1
    location='us-central1',

    # Google Cloud Storage bucket in same region as location
    # used to stage artifacts
    staging_bucket='gs://my_staging_bucket',
)



def multiturn_generate_content():
    config = {
        "max_output_tokens": 2048,
        "temperature": 0.9,
        "top_p": 1
    }
    model = GenerativeModel("gemini-pro")
    chat = model.start_chat()

    q = """
    Fact 1: All pythons are snakes. 
    Fact 2: Some pythons are pythonistas. 
    Fact 3: Female snakes lay eggs.
    Given the first three factual statements, briefly answer which of the following options are true:
    Option I. All snakes lay eggs. Option II. Pythonistas are snakes. Option III. Some pythons are not pythonistas. 
    """
    #print(chat.send_message(q, generation_config=config))
    return chat.send_message(q, generation_config=config)
    
    #note: this is only one variation (there are 7 more questions)

answers = []
answers.append(["Type", "Fact", "Response"])
x = 0
while x < 100: 
    try:
        print(x)
        response = multiturn_generate_content()
        data = ["Python", "Factual", response.text]
        #print(response.text)
        answers.append(data)
        x+=1
    except:
        print("blocked!11!!!11")

csv_file = "PythonsFact.csv"

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(answers)
