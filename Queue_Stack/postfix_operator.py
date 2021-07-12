sik = input("식 입력 :").split() # 공백으로 분리해주기
s1 = [] #stack 생성해주기

for i in sik :
    # 연산자별 연산 정의 
    if i == '+' or i == '-' or i == '*' or i == '/':
        op2 = s1.pop()
        op1 = s1.pop()
        if i == '+' :
            r = op1 + op2
        elif i == '-':
            r = op1 - op2
        elif i == '*':
            r = op1 * op2
        else:
            r = op1 / op2
        s1.append(r)
    #그냥 숫자일때
    else:
        s1.append(float(i))

print(s1[0])
