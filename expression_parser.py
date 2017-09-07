class ExpresisonParser():
    iterator = 0
    query = ''

    def parse(self, query):
        self.iterator = 0
        self.query = query
        self.query+='#'
        return self.parseLogical()

    def parseLogical(self):
        left_term = self.parseNot()
        while (True):
            operator = self.parseLogOperator()
            if operator != None:
                right_term = self.parseNot()
                # add to the expression
                left_term = Logical(operator, left_term, right_term)
            else:
                break
        return left_term

    def parseNot(self):
        left_term = None
        operator = self.parseLogOperator() # if expression starts with not

        if operator == '~':
            left_term = self.parsePrimary()
            left_term = Logical(operator, left_term, None)
        else:
            left_term = self.parsePrimary()

        return left_term

    def parsePrimary(self):
        result = None
        self.skipSpaces() #????
        n_char = self.charPoint()
        if n_char[0].isalpha():
            result = self.parseTerm()
        elif n_char == '(':
            self.moveIterator() #skip '('
            result = self.parseLogical()
            self.skipSpaces();
            n_char = self.charPoint()
            if (n_char != ')'):
                print ("Wrong brackets")
            self.moveIterator() #skip ')'
        else:
            print ("ERROR")
        return result

    def parseTerm(self):
        term = ''
        while (self.charPoint().isalpha()):
            term+=self.charPoint()
            self.moveIterator()
        result = Term(term)
        return result

    def charPoint(self):
        return self.query[self.iterator]

    def moveIterator(self):
        self.iterator+=1

    def skipSpaces(self):
        while (True):
            if self.charPoint() == ' ':
                self.moveIterator()
            else: break

    def parseLogOperator(self):
        self.skipSpaces()
        if self.charPoint() == '~':
            self.moveIterator()
            return '~'
        if self.charPoint() == '&':
            self.moveIterator()
            return '&'
        if self.charPoint() == '|':
            self.moveIterator()
            return '|'
        return None

class Expression(object):
    def __init__(self):
        pass

class Logical(Expression):
     def __init__(self, operator, left, right):
         self.operator = operator
         self.left = left
         self.right = right

class Term(Expression):
    def __init__(self, term):
        self.term = term

def main():
    query = "~(terms & termz) | ~terma & termb & termc"
    parser = ExpresisonParser()
    result = parser.parse(query)
    print ("enddd")

if __name__ == '__main__':
    main()
