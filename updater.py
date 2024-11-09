import requests
import os

# 다운로드 URL
DOWNLOAD_URL = "https://raw.githubusercontent.com/MrPlayerLee/AbidosCalculator/main/Release/AbidosCalculator.exe"

def download_and_update():
    try:
        # 파일 다운로드
        response = requests.get(DOWNLOAD_URL, stream=True)
        if response.status_code == 200:
            # 기존 파일 덮어쓰기
            with open("AbidosCalculator.exe", "wb") as f:
                f.write(response.content)
            print("업데이트가 완료되었습니다.")
        else:
            print(f"다운로드 실패: 상태 코드 {response.status_code}")
    except Exception as e:
        print(f"다운로드 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    download_and_update()

os.system("pause>nul")