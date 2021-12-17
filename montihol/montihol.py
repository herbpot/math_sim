import random
from time import *

print('''
몬티홀 문제 시뮬레이션 입니다.
선택지를 바꾸는 경우 / 바꾸지 않는 경우의 정/오답 비율을 확인해 볼 수 있습니다
''')

sle = str(input('매 결과마다 기다리기를 하시겠습니까? (y/n) >>>'))
if sle == 'y': print('결과가 나올때마다 0.3초간 기다립니다')

def pick(l,fans):
        
        l.pop(l.index(fans))
            
        return l[0]

def sl(a:float):
    if sle != 'y' : return
    sleep(a)

def main(a):
    cy = 1000
    print(f'반복횟수 {cy}회')
    sus = 0
    fai = 0

    sleep(1)
    
    
    


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
                if l[b]!= answer and l[b] != ans:
                    print(f'선텍지 "{l[b]}"을(를) 제외합니다')
                    l.pop(b)
                    break
                
            print('선텍지를 바꿉니다') 
            ans = pick(l,ans)
            print(f'선텍지 : {ans}')
            if ans == answer :
                print('정답')
                sus += 1
            else:
                print('오답')
                fai += 1
            sl(0.7)

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
                sl(0.7)

    perS = sus/(sus+fai)*100
    perF = fai/(sus+fai)*100
    print(f'''
    총 반복 횟수 : {cy}회
    정답 횟수 : {sus}회
    오답 횟수 : {fai}회

    정답 비율 : {perS}%
    오답 비율 : {perF}%

    ''')
    sl(5)
    return perS

print(f'''

선택지를 바꿀떄의 정답 비율 : {main('y')}%

선택지를 바꾸지 않을떄의 정답 비율 : {main('n')}%

''')
ex = input("끝내려면 Enter키를 누르세요")