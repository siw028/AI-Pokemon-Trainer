import os, json, shutil
from openai import OpenAI
from pathlib import Path

import logging
logger = logging.getLogger("ai_pokemon_trainer")

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
    logger.debug(f"Send to API, {json.dumps(prompt, indent=4, separators=(',', ': '), ensure_ascii=False)}")
    response = client.chat.completions.create(
        model=SECRET_SETTING["model"],
        messages=prompt,
        response_format={"type": "json_object"},
    )
    logger.debug(f"Recived by API, {json.dumps(response.choices[0].message.content, indent=4, separators=(',', ': '), ensure_ascii=False)}")
    return response.choices[0].message.content
