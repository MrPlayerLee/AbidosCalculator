from distutils.core import setup
import py2exe, time, os, glob, sys


prgname = "AbidosCalculator.py"
file_name = "읽어주세요..txt"
results_folder = "Release"
file_path = os.path.join(results_folder, file_name)

setup(
    console=[{
        'script': prgname,
        'icon_resources': [(1, 'Icon\Icon.ico')]
    }],
    options={
        'py2exe': {
            'bundle_files': 1,  # 단일 실행 파일로 묶기
            'compressed': True,  # 압축
            'optimize': 2,       # 최적화 수준
        }
    },
    zipfile=None,  # zip 파일을 생성하지 않음
)

os.rename("Dist", results_folder)
os.makedirs(f"{results_folder}\Results")

with open(file_path, 'w') as f:
    original_stdout = sys.stdout
    sys.stdout = f

    print(f"1. {prgname}를 실행하여 계산할 수 있습니다.")
    print(f"2. {prgname}로 계산한 후 {results_folder} 폴더에서 확인할 수 있습니다.")
    print("3. 본 결과는 절대적이지 않으며 일부 오류가 있을 수 있습니다.")
    print("4. 항상 결과보다 조금 더 적은 값으로 교환하고 이후 남은 부분은 직접 계산해보시길 바랍니다.")
    print("5. 충분한 테스트를 겨쳤음에도 문제가 있을 수 있습니다.")

    sys.stdout = original_stdout

warning_file_path = os.path.join(f"{results_folder}\Results", '0_이곳에_임의로_다른_파일을_넣지_마십시오.txt')
with open(warning_file_path, 'w', encoding='utf-8-sig') as warning_file:
    warning_file.write(" ")