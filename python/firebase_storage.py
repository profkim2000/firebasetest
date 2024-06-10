# pip install --upgrade google-cloud-storage. 그런데 이거 안해도 될 거 같다. 어차피 import도 안함.

# 참조문서: https://cloud.google.com/storage/docs/reference/libraries
# 참조문서: https://firebase.google.com/docs/storage/admin/start?hl=ko&_gl=1*bcle9q*_up*MQ..*_ga*MTExMDA0ODI0OS4xNzE4MDIzOTQw*_ga_CW55HF8NVT*MTcxODAyMzk0MC4xLjAuMTcxODAyMzk0MC4wLjAuMA..#python

from firebase_admin import credentials, initialize_app, storage

# 아래 json 파일은 firebase 프로젝트 개요 옆에 톱니바퀴 누르고 프로젝트 설정 > 서비스 계정 > firebase admin sdk 페이지를 python으로 놓고 [새 비공개 키 생성] 버튼을 눌러 다운로드받은 파일의 전체 경로임.
cred = credentials.Certificate(r'd:\download\jstestmsk-firebase-adminsdk-9xlr3-acd75125eb.json')

# 아래 jstestmsk.appspot.com는 firebase 콘솔창 왼쪽에 storage를 클릭하면 gs://jstestmsk.appspot.com 와 같은 부분이 나오는데. 여기서 가져왔음. gs:// 는 빼야 함.
initialize_app(cred, {'storageBucket': 'jstestmsk.appspot.com'})

# 로컬에 있는 파일 firebase에 업로드
fileName = "image.png"
bucket = storage.bucket()
blob = bucket.blob(fileName)
blob.upload_from_filename(fileName)

# 모든 사람이 다운로드 받을 수 있게 하기.(개인용으로 쓸 거면 안해야 함)
blob.make_public()

print("업로드된 파일 이름:", blob.public_url)


# firebase의 파일 다운로드
source_blob_name = "image.png"
bucket_name = "jstestmsk.appspot.com"

# firebase에서 다운로드받은 파일을 저장해서 어디에 어떤 파일명으로 저장할지
destination_file_name = r"d:\download\from_firebase.png"

bucket = storage.bucket()
blob = bucket.blob(source_blob_name)
blob.download_to_filename(destination_file_name)
