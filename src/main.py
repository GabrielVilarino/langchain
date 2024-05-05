"""
Para iniciar o projeto é fazer o download do Ollama

Download Ollama no link: https://ollama.com/download

Depois instalar o ollama no projeto

poetry add ollama

Depois buscar um modelo

poetry run ollama pull llama2
"""

from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
#from langchain.chat_models.ollama import ChatOllama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
    

print("Inicinado o LLM")
llm = Ollama(model='gemma',
             callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
             temperature=0.1)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um dos melhores tradutores de todas as linguas"),
    ("user", "{input}")
])

##########################################################################################################
# text = '''Traduza para {lang} o seguinte texto:

# {text}
# '''

# chat_template = ChatPromptTemplate.from_template(text)

# print(chat_template.messages[0].prompt.template)
# print(chat_template.messages[0].prompt.input_variables)

# text_projetado = chat_template.format_messages(lang='inglês',
#                                                 text='O Gabriel Vilarino é muito lindo')

##########################################################################################################

text = '''Que dia foi a independencia do brasil?
'''
chain = prompt | llm
chain.invoke({"input": text})

