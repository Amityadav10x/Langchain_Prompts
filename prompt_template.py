from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI # 💡 Swapped to Gemini integration
from dotenv import load_dotenv

# Load the environment variables from your local .env file
load_dotenv()

# 💡 Initialize Gemini model framework (gemini-1.5-pro is excellent for multilingual tasks)
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

# detailed way
template2 = PromptTemplate(
    template='Greet this person in 5 languages. The name of the person is {name}',
    input_variables=['name']
)

# fill the values of the placeholders
prompt = template2.invoke({'name': 'Amit'})

# Invoke the model with our compiled prompt payload
result = model.invoke(prompt)

print(result.content)