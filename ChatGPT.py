import os
import openai
from PyKakao import Karlo
import requests
from PIL import Image
from io import BytesIO
from PyPDF2 import PdfReader
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.getenv('OPENAI_API_KEY')
KAKAO_API_KEY = "APIKEY"

kakao_api_key = Karlo(service_key=KAKAO_API_KEY)
model = "gpt-3.5-turbo"
question = input("무엇을 물어볼까요?: ")
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant who is good at detailing."
    },
    {
        "role": "user",
        "content": question
    }
]

answer = openai.ChatCompletion.create(
    model=model,
    messages=messages
)
answer = answer.choices[0].message.content
print(answer)

messages.append(
    {
        "role": "assistant",
        "content": answer.choices[0].message.content
    },
)

messages.append(
    {
        "role": "user",
        "content": "더 자세히 말해줘."
    }
)

answer2 = openai.ChatCompletion.create(
    model=model,
    messages=messages
)
print(answer2.choices[0].message.content)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant who is good at translating."
    },
    {
        "role": "assistant",
        "content": answer2.choices[0].message.content
    },
    {
        "role": "user",
        "content": "영어로 번역해주세요."
    }
]

# ChatGPT API 호출하기
answer3 = openai.ChatCompletion.create(
    model=model,
    messages=messages
)

print(answer3.choices[0].message.content)

# 새 메시지 구성
messages = [
    {
        "role": "system",
        "content": "You are an assistant who is good at creating prompts for image creation."
    },
    {
        "role": "assistant",
        "content": answer3.choices[0].message.content
    },
    {
        "role": "user",
        "content": "Condense up to 4 outward description to focus on nouns and adjectives separated by ,"
    }
]

answer4 = openai.ChatCompletion.create(
    model=model,
    messages=messages
)
print(answer4.choices[0].message.content)

params = ", concept art, realistic lighting, ultra-detailed, 8K, photorealism, digital art"
prompt = f"Delicious Cream Pasta, {answer4.choices[0].message.content}{params}"
print(prompt)

# 이미지 생성하기 REST API 호출
img_dict = kakao_api_key.text_to_image(prompt, 1)

# 생성된 이미지 정보
img_str = img_dict.get("images")[0].get('image')

# base64 string을 이미지로 변환
img = kakao_api_key.string_to_image(base64_string=img_str, mode='RGBA')

img.save("./pasta.png")

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
res = requests.get(image_url)
img = Image.open(BytesIO(res.content))
