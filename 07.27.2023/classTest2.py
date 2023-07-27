class Person: 
    gene = 'XYZ'

    def __init__(self,name):
        self.name = name
        # self.age = age

    def greeting(self):
        return f'안녕,{self.name}입니다.'


class Mom(Person): #부모 클래스의 이름이 바뀌면?

    def __init__(self,name):      # 생성자 함수에 다른 변수가 없으므로 생략해도 되지만, 써주는게 스타일가이드에 맞음
        super().__init__(name)

    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    def __init__(self,name,age):      # 생성자 함수에 다른 변수가 없으므로 생략해도 되지만, 써주는게 스타일가이드에 맞음
        super().__init__(name)
        self.age = age

    gene = 'XY'
    def walk(self):
        return '아빠가 걷기'


class firstChild(Mom, Dad): # 상속 순서 중요
    dad_gene = Dad.gene  #상속순서는 바꿀수없지만, 아빠 유전자 써야 할 때
    
    per_gene = Person.gene #xyz 받아오려면?
    def __init__(self,name,age):      # 생성자 함수에 다른 변수가 없으므로 생략해도 되지만, 써주는게 스타일가이드에 맞음
        #super().__init__(name) #mom
        Dad.__init__(self,name,age)  #Dad의 init을 받아오기 위함

    def swim(self):
        return '첫쨰가 수영'
    
    def cry(self):
        return '첫째가 응애'
    
    
    


baby1 = firstChild('아가',1)
print(baby1.cry())
print(baby1.swim()) # 첫째가 응애 (본인의 인스턴스 메서드이므로 먼저 출력)
print(baby1.walk()) # 아빠가 걷기 ( Dad Class에서 물려받음 )\
print(baby1.gene) # XX(Mom를 먼저 상속받았기에)
print(firstChild.mro())

print(baby1.dad_gene)
print(baby1.per_gene)
# s1 = Student 
# ('김학생' , 20 , 3.5)

# p1.talk()
# s1.talk()