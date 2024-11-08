from distutils.core import setup
import py2exe, time, os, glob

#변수 입력
prgname = "AbidosCalculator.py"
excludes = [
	"pywin" ,
	"pywin debugger" ,
	"pywin debugger.dbgcon" ,
	"pywin dialogs" ,
	"pywin dialogs.list" ,
	"win32com.server" ,
]
options = {
	"bundle_files" : 1,
	"compressed" : 1,
	"excludes" : excludes,
	"dll_excludes" : ["w9xpopen" , "MSVCP90.dll"]
}

#메인코드
print(f"{prgname} 를 빌드하기 시작합니다...")
time.sleep(2)
#setup(console=[f'{prgname}'])

setup(
	options = {"py2exe" : options},
	zipfile = None,
	console = [prgname]
	#windows = [""]
	#data_files=[("images", glob.glob("images/*"))]
)

print(f"{prgname} 빌드가 완료되었습니다.\n아무키를 입력해주세요.")
os.system('pause>nul')