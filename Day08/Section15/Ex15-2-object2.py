

class Calculator :
    def input_expr(self) :
        expr = input('수식을 입력하세요:')
        self.expr = expr

    def calculate(self):
        return eval(self.expr)


calculator1 = Calculator()
calculator1.input_expr()
print(calculator1.calculate())