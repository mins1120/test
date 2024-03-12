from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수를 로드
load_dotenv()

# 환경 변수를 사용하여 API 키를 불러옴
openai_api_key = os.getenv("OPENAI_API_KEY")
pass