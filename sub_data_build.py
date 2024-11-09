import os, sys, zipfile, shutil
shutil.copyfile('updater.exe', 'dist/updater.exe')

def zip_folder(folder_path, output_path):
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for folder_name, subfolders, filenames in os.walk(folder_path):
            for filename in filenames:
                file_path = os.path.join(folder_name, filename)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))

prgname = "AbidosCalculator.py"
file_name = "읽어주세요..txt"
results_folder = "Release"
file_path = os.path.join(results_folder, file_name)
os.rename("dist", results_folder)
os.makedirs(f"{results_folder}\Results")

print("안내문구 추가중.")
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
print("완료.")

print("압축중.")
zip_folder('Release', 'AbidosCalculator.zip')
print("완료.")
