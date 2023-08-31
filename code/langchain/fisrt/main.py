from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
# from langchain.chat_models import ChatOpenAI
#
#
# chat([HumanMessage(content="Translate this sentence from English to French: I love programming.")])

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

llm = OpenAI(openai_api_key='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')
chat_model = ChatOpenAI(openai_api_key='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')

print(llm.predict("hi!"))
print(chat_model.predict("hi!"))
print(chat_model([HumanMessage(content="Translate this sentence from English to French: I love programming.")]))