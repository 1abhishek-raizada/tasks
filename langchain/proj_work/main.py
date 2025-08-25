import os
import json
from openai import OpenAI
from dotenv import load_dotenv

from template import system_prompt_info

load_dotenv()

base_dir =os.getcwd()

class InsightExtractor:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        os.environ['OPENAI_API_KEY'] = self.api_key

        self.client = OpenAI()
    def extract_insights(self, system_prompt:str,user_input:str) -> str: 

        response = self.client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input},
            
        ],
        top_p=1,
        temperature=0,
    )

        print("prompt_tokens::::",response.usage.prompt_tokens)         
        print("completion_tokens:::::",response.usage.completion_tokens)     
        print("total_tokens::::::::",response.usage.total_tokens)
        # function_args = response.choices[0].message.function_call.arguments
        return response.choices[0].message.content.strip()


    def load_file(self, input_file):
        with open(input_file, 'r') as file:
            content = file.read()
        return content
    
    def save_file(self,data,input_file):
        with open(input_file, "w") as f:
                json.dump(json.loads(data), f)



if __name__=="__main__":
     r =InsightExtractor()
     data =r.load_file(r"old_chat_info_text.txt")
    #  print(aa)
     a =r.extract_insights(system_prompt_info,data)
     print(a)
     data_=json.loads(a)
     with open("old_chat_info_text.json", "w") as f:
        json.dump(data_, f)
     

     
 