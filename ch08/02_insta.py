#인스타그램 사진 업로드 py
from pathlib import Path
from instagrapi import Client
from PIL import Image

USER_ID = "instagram ID"
USER_PASSWORD = "Password!"

# 이미지 사이즈 변환 (pillow라이브러리 사용)
image = Image.open("instaimg.jpg")
image = image.convert("RGB") #RGB레벨로 converting 한다.
new_image = image.resize((1080, 1080)) #정사각형 사이즈로 resizing 한다.
new_image.save("new_picture.jpg")

#인스타그램 로그인
cl = Client()
cl.login(USER_ID, USER_PASSWORD)

#사진 가져오기
phot_path = "new_picture.jpg"
phot_path  = Path(phot_path)
print(phot_path)

#업로드하기
cl.photo_upload(phot_path , "hello this is a test from instagrapi")

# http://github.com/adw0rd/instagrapi
