# -*- coding: utf-8 -*-
# 이 파일은 한글 프로그래밍 언어, 아라(Ara)에 의해 작성되어진 Python 파일입니다.
# NewPyengine build, beta 0.0.3
# 만들어진 시각 : 2015. 07. 22. 19:53:24

 # 본 예제의 내용은 중학 수준 이상의 수학 지식을 요구합니다.

 # 초등학생 분들은 원의_둘레_구하기.ara를 참조하십시오.


 # x^2 + 2x + 1 = 0

a = 1
b = 2
c = 3

 # b^2 - 4ac를 계산합니다.

결과 = b * b - 4 * a * c

 # 결과를 판독합니다.

if 결과 < 0:
	print("허근입니다.")
elif 결과 == 0:
	print("중근입니다.")
else:
	print("실근입니다.")
