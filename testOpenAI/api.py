# api.py

# 패키지 설치 : openai

from openai import OpenAI

# 발급받은 API 키 설정
OPENAI_API_KEY = '키설정'

client = OpenAI(api_key=OPENAI_API_KEY)
print(client)


def ask(question, message_history=[], model='gpt-3.5-turbo'):
    if len(message_history) == 0:
        message_history.append(
            {
                "role": "system",
                "content": "안녕하세요",
            }
        )

    # 사용자 질문
    message_history.append(
        {
            "role": "user",
            "content": question,  # 사용자의 질문을 입력
        },
    )

    # GPT 에 질문을 전달해서 답변 생성
    completion = client.chat.completions.create(
        model = model,
        messages=message_history
    )

    # 사용자 질문에 대한 답변 추가
    message_history.append(
        {
            'role': 'assistant',
            'content': completion.choices[0].message.content
        }
    )
    # 답변을 반환
    return message_history


# 실행
# 최초 질문
message_history = ask('태양계에 속한 행성을 말해줘?', message_history=[])

# 최초 답변
print(message_history[-1])

# 두번째 질문
message_history = ask('이전 내용을 영어와 일어로 답변해줘', message_history=message_history)

# 두번째 답변
print(message_history[-1]['content'])




