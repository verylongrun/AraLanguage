import sys, os, optparse

__author__ = 'Seunghwan Hong'

def main():
    p = optparse.OptionParser()
    usage = "%prog -i [아라 파일] -o [출력될 파일 경로] (-c, -p, -b)"

    p.set_usage(usage)

    # 본 파일과 변환된 파일의 경로를 지정
    p.add_option("-i", "--infile", action="store", help="작성하신 아라 파일의 경로", dest="infile", metavar="[아라 파일 경로]")
    p.add_option("-o", "--outfile", action="store", help="변환된 파일의 경로 ('.'만 입력하면 이 파일과 같은 경로에 변환됩니다)", dest="outfile", metavar="[출력될 파일 경로]", default=".")

    # 변환할 언어를 지정
    p.add_option("-l", "--lang", action="store", type="choice", dest="lang", metavar="[언어 이름]", choices=["py", "c", "python", "all"], default="py", help="변환할 언어를 선택합니다. 언어는 Python과 C, 혹은 모두로 변환할 수 있습니다.")

    # 옵션 파싱 및 변수 설정
    opts, args = p.parse_args()
    infile = opts.infile
    outfile = opts.outfile
    lang = opts.lang

    print("[*] 아라(Ara) : 한글을 사용하는 프로그래밍 언어\n[*] 작성자 : 홍승환, 최현우\n")

    # 인수가 잘못 설정되었을 때 프로그램 종료
    if len(sys.argv) != 7:
        print("[-] 인수가 잘못 설정되었습니다. 도움이 필요하시면 python AraCompiler.py -h를 참조하세요.")
        sys.exit(2)

    # 아라 파일 오픈 (.ara) 혹은 인코딩 에러 catch 후 수정
    try:
        if ".ara" not in infile:
            raise Exception
        f = open(infile, "rU", encoding="euc-kr")
        araCode = f.readlines()
    except UnicodeDecodeError as e:
        f.close()
        f = open(infile, "rU", encoding="utf-8")
        araCode = f.readlines()

    print("[+] 아라 파일을 읽어들입니다... : " + infile)

    if "".join(araCode[-1:]).find("아라") == -1:
        print("[-] 정상적인 아라 파일이 아닙니다! 파일 하단에 \"아라\" 문자열을 넣으셨습니까?")
        sys.exit(9)
    else:
        araCode.pop()

    # 변환 완료 소스 리스트 준비
    pyCode = []
    cCode = []

    # 언어별로 변환 : 엔진 연계
    try:
        if lang == "py" or lang == "python":
            print("[+] Python으로 변환을 시작합니다...")
            from . import Pyengine as engine
            pyCode = engine.convert(araCode)
        elif lang == "c":
            print("[+] C로 변환을 시작합니다...")
            from . import Cengine as engine
            cCode = engine.convert(araCode)
        else:
            print("[+] Python과 C로 변환을 시작합니다...")
            from . import Pyengine as pye
            from . import Cengine as ce
            pyCode = pye.convert(araCode)
            cCode = ce.convert(araCode)
        f.close()
    except Exception as e:
        print("[-] 예기치 못한 오류가 발생했습니다. 다시 시도하시거나, 에러 내용을 문의해주세요.")
        print("[-] 에러 명세 : " + str(e))
        sys.exit(4)

    # 변환 완료
    print("[+] 변환을 성공적으로 끝마쳤습니다!")

    # 변환 완료된 파일을 저장
    print("[+] 파일을 저장합니다...")
    try:
        if lang == "py" or lang == "python":
            f = open(outfile + "/" + os.path.basename(infile).strip(".ara") + ".py", "w")
            for i in range (0, len(pyCode) - 1):
                f.write(pyCode[i])
            f.close()
        elif lang == "c":
            f = open(outfile + "/" + os.path.basename(infile).strip(".ara") + ".c", "w")
            for i in range (0, len(cCode) - 1):
                f.write(cCode[i])
            f.close()
        else:
            f = open(outfile + "/" + os.path.basename(infile).strip(".ara") + ".py", "w")
            for i in range (0, len(pyCode) - 1):
                f.write(pyCode[i])
            f.close()
            f = open(outfile + "/" + os.path.basename(infile).strip(".ara") + ".c", "w")
            for i in range (0, len(cCode) - 1):
                f.write(cCode[i])
            f.close()
    except Exception as e:
        print("[-] 예기치 못한 오류가 발생했습니다. 다시 시도하시거나, 에러 내용을 문의해주세요.")
        print("[-] 에러 명세 : " + str(e))
        sys.exit(5)

    print("[+] 변환 완료 파일이 다음 위치에 저장되었습니다 : " + outfile)
    print("[+] 즐거운 프로그래밍 되세요!")
    sys.exit(1)

main()