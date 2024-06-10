# pip install --upgrade firebase-admin

# 참조문서: https://firebase.google.com/docs/firestore/quickstart?hl=ko#python

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
# 아래 json 파일은 firebase 프로젝트 개요 옆에 톱니바퀴 누르고 프로젝트 설정 > 서비스 계정 > firebase admin sdk 페이지를 python으로 놓고 [새 비공개 키 생성] 버튼을 눌러 다운로드받은 파일의 전체 경로임.
cred = credentials.Certificate(r'd:\download\jstestmsk-firebase-adminsdk-9xlr3-acd75125eb.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

# 데이터 추가 1
doc_ref = db.collection("users").document("alovelace1")
doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

# 데이터 추가 2. 위와 다른 양식으로도 가능하다.
doc_ref = db.collection("users").document("aturing")
doc_ref.set({"first": "Alan", "middle": "Mathison", "last": "Turing", "born": 1912})

# 데이터 읽기. users collection의 모든 문서 읽기
users_ref = db.collection("users")
docs = users_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")
