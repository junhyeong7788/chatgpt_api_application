import requests

PAPAGO_ID = ''
PAPAGO_PW = ''

def papago_translate(text):
    
    data = {'text': text,
            'source': 'en',
            'target': 'ko'}
    
    url = 'API_url'
    headers = {'X-Naver-Client-Id': PAPAGO_ID, #http에서 헤더부분
               'X-Naver-Client-Secret': PAPAGO_PW}
    
    response = requests.post(url, data=data, headers=headers) #서버에서 응답을 받는부분
    rescode = response.status_code
    
    if(rescode == 200): #서버에서 200이라는 응답을 받으면 아래 코드 실행
        send_data = response.json() #json형태로 데이터를 변환, 데이터 타입을 확인하는 것이 중요하다. (파이썬의 단점 : 변수명으로 데이터 타입을 확인할 수 없다.)
        trans_data = (send_data['message']['result']['translatedText']) #json은 키값으로 데이터를 불러옴
        return trans_data #번역된 데이터를 리턴
    else:
        print("Error Code:" + rescode) 


text = '''
Black tea (also literally translated as red tea from various East Asian languages) is a type of tea that is more oxidized than oolong, yellow, white and green teas. Black tea is generally stronger in flavour than other teas. All five types are made from leaves of the shrub (or small tree) Camellia sinensis, though Camellia taliensis is also used rarely.
'''

result = papago_translate(text)
print(result)