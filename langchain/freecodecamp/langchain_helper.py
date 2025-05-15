from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv


load_dotenv()

def generate_pet_name(animal_type):
    llm=GoogleGenerativeAI(model="gemini-1.5-flash-latest",temperature=0.3)

    prompt_temp=PromptTemplate(
        input_variables=['animal_type'],
        template='I have a {animal_type} pet and i want a cool name for it.' \
        'Suggest me five cool names for my pet.'
    )

    



    name_chain=LLMChain(llm=llm, prompt=prompt_temp)
    response=name_chain({'animal_type':animal_type})

    return response

if __name__=="__main__":
    print(generate_pet_name('cat'))

