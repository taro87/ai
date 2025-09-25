# sample_pac/cd/c.py
# import sys
# sys.path.append(r'C:\taro\ai\source\pylib')
# from sample_pac.ab import a
# python -m sample_pac.cd.c 로 실행시 위 코드가 생략
from ..ab import a
def byebye():
    print('sample_pac.cd.c모듈의 byebye')
    a.hello()
if __name__ == '__main__':
    byebye()