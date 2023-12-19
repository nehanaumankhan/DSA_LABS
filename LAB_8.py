from STACK import stack

# Evaluation of a Postfix expression
def evaluate_postfix(expression):
    expression = expression + ' )'
    expression = expression.split()
    s = stack(len(expression)//2)
    for i in expression:
        if i.isdigit():
            s.PUSH(i)
        elif i == ')':
            return s.POP()
        else:
            b = s.POP()
            a = s.POP()
            s.PUSH(eval(f'{a} {i} {b}'))

#Transforming Infix expression to Postfix expression
def transform_infix_to_postfix(infix_exp):
    infix_exp = infix_exp + ' )'
    infix_exp = infix_exp.split()
    postfix_exp = ''
    precedence = '+=*/'
    s = stack(len(infix_exp)//2)  
    for i in infix_exp:
        if i.isalpha() or i.isdigit():  #if i is operand add to postfix expression
            p += f'{i} '
        elif i == '(' or i == '^':
            s.PUSH(i)
        elif i == ')':
            res = s.POP()
            while(res != '('):
                p += res
                s.POP()
        elif i in precedence:
            if s[s.TOS]


            

print("Evaluation of postfix infix_exp")
print(f"Expression: '1 4 18 6 / 3 + + 5 / +' Result: {evaluate_postfix('1 4 18 6 / 3 + + 5 / +')}")
print(f"Expression: '3 1 + 2 ^ 7 4 - 2 * + 5 -' Result: {evaluate_postfix('3 1 + 2 ^ 7 4 - 2 * + 5 -')}")
