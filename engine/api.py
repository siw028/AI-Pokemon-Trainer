import requests, os, json, shutil
from openai import OpenAI
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_SETTING = None
if not os.path.exists(BASE_DIR / 'secret_setting.json'):
    shutil.copyfile(BASE_DIR / 'secret_setting.json.example',
                    BASE_DIR / 'secret_setting.json')
with open(BASE_DIR / 'secret_setting.json', 'r') as fp:
    SECRET_SETTING = json.loads(fp.read())

client = OpenAI(
    api_key=SECRET_SETTING["api-key"],
    base_url=SECRET_SETTING["base-url"],
)

def get_chatgpt_response(prompt):
    print("[DEBUG]", prompt)
    response = client.chat.completions.create(
        model='deepseek-chat',
        #model="gpt-4o",
        messages=prompt,
        response_format={"type": "json_object"},
    )
    print("[DEBUG] GPT OUT",response.choices[0].message.content)
    return response.choices[0].message.content
