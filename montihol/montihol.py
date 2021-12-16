import random
from time import *

print('''
몬티홀 문제 시뮬레이션 입니다.
선택지를 바꾸는 경우 / 바꾸지 않는 경우의 정/오답 비율을 확인해 볼 수 있습니다
''')

sleep(3)

def main(a):
    cy = 1000
    print(f'반복횟수 {cy}회')
    sus = 0
    fai = 0

    sleep(1)
    
    def pick(l):
        ans = random.randint(1,3)
        try:
            l.pop(ans)
        except:
            pick(l)
        return ans
    


    if(a == 'y'):
        print('선텍지를 바꾸며 시뮬레이션을 진행합니다')
        for i in range(cy):
            l = [1,2,3]

            print('''
                1       2       3
            ''')
            ans = random.randint(1,3)
            print(f'선텍지 : {ans}')
            n = random.randint(0,2)
            answer = l[n]
            while True:
                b = random.randint(0,2)
                if l[b]!= answer:
                    print(f'선텍지 "{l[b]}"을(를) 제외합니다')
                    l.pop(b)
                    break
            print('선텍지를 바꿉니다')    
            ans = pick(l)
            print(f'선텍지 : {ans}')
            if ans == answer :
                print('정답')
                sus += 1
            else:
                print('오답')
                fai += 1

    elif a == 'n':
            print('선텍지를 바꾸지 않으며 시뮬레이션을 진행합니다')
            for i in range(cy):
                l = [1,2,3]

                print('''
                    1       2       3
                ''')
                ans = random.randint(1,3)
                print(f'선텍지 : {ans}')
                n = random.randint(0,2)
                print(n)
                answer = l[n]
                if ans == answer :
                    print('정답')
                    sus += 1
                else:
                    print('오답')
                    fai += 1
    perS = sus/(sus+fai)*100
    perF = fai/(sus+fai)*100
    print(f'''
    총 반복 횟수 : {cy}회
    정답 횟수 : {sus}회
    오답 횟수 : {fai}회

    정답 비율 : {perS}%
    오답 비율 : {perF}%

    ''')
    sleep(5)
    return perS

print(f'''

선택지를 바꿀떄의 정답 비율 : {main('y')}%

선택지를 바꾸지 않을떄의 정답 비율 : {main('n')}%

''')
