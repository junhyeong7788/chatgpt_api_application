from bardapi import Bard

token = 'your_token'
bard = Bard(token=token, timeout=30)
result = bard.get_answer('your_question') # your_question에 질문을 넣어주세요.

print(result)