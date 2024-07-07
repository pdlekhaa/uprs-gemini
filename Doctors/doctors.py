import vertexai
from google.cloud import aiplatform_v1
from google.cloud import aiplatform
import vertexai.preview
import csv
from vertexai import preview
from vertexai.preview.generative_models import GenerativeModel, Part
import time
from vertexai.generative_models._generative_models import ResponseBlockedError
from google.cloud import aiplatform
from google.cloud.aiplatform import initializer as aiplatform_initializer
from google.cloud.aiplatform_v1beta1 import types as aiplatform_types
from google.cloud.aiplatform_v1beta1.services import prediction_service
from google.cloud.aiplatform_v1beta1.types import (
    content as gapic_content_types,
)
from google.cloud.aiplatform_v1beta1.types import (
    prediction_service as gapic_prediction_service_types,
)
from google.cloud.aiplatform_v1beta1.types import tool as gapic_tool_types
from vertexai.language_models import (
    _language_models as tunable_models,
)

HarmCategory = gapic_content_types.HarmCategory
HarmBlockThreshold = gapic_content_types.SafetySetting.HarmBlockThreshold

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
def multiturn_generate_content(q):
    config = {
        "max_output_tokens": 2048,
        "temperature": 0.9,
        "top_p": 1
    }
    
    model = GenerativeModel("gemini-pro", safety_settings=my_safety_settings)
    chat = model.start_chat()

    return chat.send_message(q, generation_config=config)

#ensure nothing is blocked because of the word 'die'
my_safety_settings={
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            }

#Doctors
q1 = '''
Of 100 people having a certain surgery, 10 will die during treatment, 32 will have died by one year, 
and 66 will have died by five years. Of 100 people having radiation therapy, none will die during treatment, 
23 will die by one year, and 78 will die by five years. Which option would you recommend? You have to choose one. 
Please give a BRIEF response.
'''

q2 = '''
Of 100 people having a certain surgery, 90 will survive the treatment, 68 will survive one year or longer, and 
34 will survive five years or longer. Of 100 people having radiation therapy, all will survive the treatment, 77 will survive one year 
or longer, and 22 will survive five years or longer. Which option would you recommend? You have to choose one. 
Please give a BRIEF response.
'''

#print(multiturn_generate_content(q1))

answers = []
answers.append(["Form", "Response"])

x = 0
while x < 1000: 
    try:
        print(x)
        response = multiturn_generate_content(q1)
        data = ["Form A", response.text]
        print(response.text)
        answers.append(data)
        x+=1
    except:
        print("blocked!11!!!11")
        time.sleep(10)

print("Form B Time")

y = 0
while y < 1000: 
    try:
        print(y)
        response = multiturn_generate_content(q2)
        data2 = ["Form B", response.text]
        print(response.text)
        answers.append(data2)
        y+=1
    except:
        print("blocked!11!!!11")
        time.sleep(10)

csv_file = "Doctors1000.csv"

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(answers)