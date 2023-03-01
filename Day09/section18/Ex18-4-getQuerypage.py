'''
서버에 요청 requests
서버에서 응답 response

http 응답(response) 코드
    200번대 코드 : 성공 (success)
    300번대 코드 : 리다이렉션(redirection)
    400번대 코드 : 클라이언트 에러(client error)
        ex) 404 찾을 수 없는 페이지 (주소 잘못 입력)
    500번대 코드 : 서버 에러(server error)
        ex) 503 서버의 요청을 처리할 준비가 되지 않음 (개발자 코드 에러 발생했을 떄)
'''
import requests

url = 'https://www.naver.com'
response = requests.get(url)
print('응답 코드: {}'.format(response.status_code))
print(response.text)
