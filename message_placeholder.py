from pathlib import Path
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_history = []
chat_history_file = Path(__file__).resolve().parent / 'chat_history.txt'

# message parser for plain-text history entries
def parse_history_line(line: str):
    if ':' not in line:
        return None
    role, content = line.split(':', 1)
    content = content.strip()
    role = role.strip().lower()
    if role == 'system':
        return SystemMessage(content=content)
    if role == 'human':
        return HumanMessage(content=content)
    if role == 'ai' or role == 'assistant':
        return AIMessage(content=content)
    return None

# ensure chat history file exists
if not chat_history_file.exists():
    chat_history_file.touch()
    print(f"Created empty '{chat_history_file.name}' in script directory.")

# load chat history
with chat_history_file.open('r', encoding='utf-8') as f:
    for line in f:
        text = line.strip()
        if not text:
            continue
        message = parse_history_line(text)
        if message is not None:
            chat_history.append(message)
        else:
            print(f"Skipping malformed history line: {text}")

print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where chinnaswami stadium located'})

print(prompt)