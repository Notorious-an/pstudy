try:
    score = int(input('점수를 입력하세요 : '))
    if score < 0 or score > 100:
        raise Exception('점수는 0~100 사이입니다.') # 예외 강제로 발생시키기

except Exception as e : # Exception(별칭 e)라는 예외 발생시
    print(e) # 예외시 발생만 문구 출력

else : # 예외 아닐시 실행할 코드
    if score >= 80:
        print('{}점은 합격입니다.'.format(score))
    else :
        print('{}점은 불합격입니다.'.format(score))