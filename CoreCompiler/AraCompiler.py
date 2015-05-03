import optparse
import sys

__author__ = 'Seunghwan Hong'

p = optparse.OptionParser()
usage = "%prog -i [아라 파일] -o [출력될 파일 경로] (-c, -p, -b)"

p.set_usage(usage)

# 본 파일과 변환된 파일의 경로를 지정
p.add_option("-i", "--infile", action="store", help="작성하신 아라 파일의 경로", dest="infile", metavar="[아라 파일 경로]")
p.add_option("-o", "--outfile", action="store", help="변환된 파일의 경로 ('.'만 입력하면 이 파일과 같은 경로에 변환됩니다)", dest="outfile", metavar="[출력될 파일 경로]")

# 변환할 언어를 지정
p.add_option("-l", "--lang", action="store", type="choice", dest="lang", choices=["c", "py", "python", "all"], help="변환할 언어를 선택합니다. 언어는 C와 Python, 혹은 모두로 변환할 수 있습니다.")

# 옵션 파싱 및 변수 설정
opts, args = p.parse_args()
infile = opts.infile
outfile = opts.outfile
lang = opts.lang

# 인수가 잘못 설정되었을 때 프로그램 종료
if(len(sys.argv) != 7):
    print("인수가 잘못 설정되었습니다. 도움이 필요하시면 python AraCompiler.py -h를 참조하세요.")
    sys.exit(3)

# 아라 파일 오픈 (.ara) 혹은 에러 출력 후 프로그램 종료
try:
    if(".ara" not in infile):
        raise Exception
    f = open(infile, "rU")
except Exception as e:
    print("아라 파일을 해당 경로에서 찾을 수 없습니다. 확장자가 .ara인 파일까지의 경로를 작성해야 합니다.")
    sys.exit(4)

# 아라 코드 읽어서 리스트로 저장
araCode = f.readlines()

# 변환 완료 소스 리스트 준비
pyCode = []
cCode = []

# 변환 알고리즘 - Cengine, Pyengine 연계
for i in range(0, len(araCode)):
    print(araCode[i].strip("\n"))

f.close() # 194