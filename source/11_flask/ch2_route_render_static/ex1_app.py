# PowerShell 관리자 모드
# PowerShell 관리자로 실행 -> Get-ExecutionPolicy -> 
#                               Set-ExecutionPolicy RemoteSigned
from flask import Flask
app = Flask(__name__) # 웹서버 객체(앱 인스턴스 생성)
@app.route("/") # 데코레이터를 통해 가능한 url 등록
def main_handler():
    return "<H1> Hello, World</H1>"
@app.route("/apt")
def apt_handler():
    # return "<h1> 예상 금액은 1,000원입니다</h1>"
    return {
        'price':'1,000',
        'unit':'won'
    }

if __name__=="__main__":
    app.run(port=80, debug=True) # 소스 수정시 서버 자동 재시작, port=80번
    
