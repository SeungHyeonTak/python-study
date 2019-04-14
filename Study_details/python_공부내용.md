Python 공부하면서 궁금했던 내용
=============================
# * <- 가변인자
* 들어오는 인자의 갯수를 모른다거나, 그 어떤 인자라도 모두 받아서 처리를 해야하는때가 있다.
* positional arguments - 위치에 따라 정해지는 인자
  - positional arguments를 가지는 가변 인자 *args 로 나타냄 list나 변수
* keyword arguments - 이름을 가진 인자
  - keyword arguments를 가지는 가변인자 **keyargs 로 나타냄 key:value가 있는 dict
* * *
# nonloacl/global/closure 에 대해 공부
* nonlocal : 하위 함수가 상위 함수의 변수를 조작
  - nonlocal이 사용된 바로 위 함수안의 변수와 바인딩하여 사용 가능
* globar : 함수 내에서 지역 변수 조작
  - global은 함수 내부에 지역변수랑 제일 상단의 전역 변수랑 바인딩 하는것
> @proprety @함수명.setter 에 대해 공부(getter / setter)
* * *
# 상속 / 오버라이드 / super() 에 대해 공부 
## 상속
> 부모클래스와 자식클래스로 나누어져있으므로 자식클래스에서 부모클래스의 정보를 가져오는 것
## 메서드 오버라이드(Method Override) 
> 자식클래스에서 부모클래스의 함수를 덮어쓸때 이용
## super()
> 부모클래스의 생성자에서 선언한것들을 자식 클래스의 생성자로 상속 받아올때 쓰는것
* super(class 이름, self) >> ?? 뭐지 >> python2에서 하던거 상관 없음
하는것과 안하는것의 차이 코드 보여주면서
* * *
# relations between classes
> choose either inheritance(상속) or composition - 통합 / 집합
# IS - A
> 부모클래스에게 상속받은 자식클래스는 부모클래스가 사라지면 상속을 못받는다. 그러므로 기본적인 상속에 대한 예시를 나타낼 수 있다.
# HAS - A -> ~객체가 ~을 가지고 있다. / composition(합성) / Aggregation(통합)
> HAS-A는 기본적으로 상속이 아니다. 예시로 경찰이 없어진다고 하여 총도 없어지는것이 아닌것 처럼 총은 다만, 소유권을 잃는것 뿐 IS-A처럼 사라지지않는다. 이 차이다.
* * *
# polymorphism (다형성)
* 모양은 같은데 다른기능들까지 가능하다는것을 다형성이라고 한다.
* * *
# Overriding(오버라이딩)
> super() 클래스를 상속받은 서브 클래스에서 슈퍼 클래스의 메소드를 같은 이름 / 같은 반환 값 / 같은 인자로 메소드 내의 로직들을 새롭게 정의하는 것을 말한다.
같은 이름에 다른 기능을 하는 메소드를 정의하고 사용하게끔 할 수 있다.
# Overloading(오버로딩)
> 오버 로딩은 하나의 클래스에서 같은 이름의 메소드들을 여러개 가지 수 있게 한다.
- 단, 메서드 인자들은 달라야함.

인스터스 멤버?

# 추상클래스
> 추상메서드 -> 순수가상함수
> 인스턴스를 만들 수 없다
# abstract method
> 몸체가 없는 함수
> 파생클래스에서 반드시 오버라이딩해야함
> 추상클래스 슈퍼클래스에서 선언하되, 서브클래스에서 반드시 오버라이딩해서 선언해줘야함
> 추상클래스란 미구현 추상메소드를 한개 이상 가지며, 자식클래스에서 해당 추상 메소드를 반드시 구현하도록 강제합니다.

# name space 
> m = Myclass()
> class name space >> Myclass.foo(m,10)   >> unbound 방식
> Object name space >> m.foo() >> bound 방식

>  s = Student("철수", 16)
> Student.print_name(s) <-- unbound method call
> s.print_name() <-- bound method call 

# class method
> 클래스 메소드에서는 cls인자를 활용하여 cls의 클래스 속성을 가져옴
# static Method
> 스태틱클래스는 부모클래스의 클래스속성 값을 가져옴
# 클래스 멤버
> 클래스 멤버는 함수안이 아닌 클래스 바로 밑에다 쓰는것
# 인스턴스 멤버
> 함수쪽에다가 self.x =x <<-- 이런식으로 써주는걸 의미함
* * *
# 생성자와 소멸자
> python에서는 기본적으로 __init__을 생성자라 하고 __del__을 소멸자라고 한다.
* * *
# __str__ 의 속성
> __str__ 속성은 자바에서 toString() 메서드와 유사함
* * *
#연산자 오버로딩 -> 다형성의 한 종류
> 연산자 오버로딩 클래스에서 재정의한 값을 다른값으로 다시 재정의한다는 그런뜻?
* 오버로딩(overloading) : 메소드의 중복정의
* 오버라이딩(overriding) : 메소드의 재정의
# Polymorphism(다형성)
> 재정의 하는것 슈퍼클래스 밑에 서브클래스들의 함수에다가 재정의 하는것
# class variable
> 일반 적으로 클래스 변수를 쓰고 함수에서 바로 쓰는것은 불가능하다 
 - 그러므로 self.variable을 쓰거나 클래스의 이름을 직접 가져와 쓰는 방법을 이용하면 된다.
# interface 
* massage passing
  * Extension -> 확장에 대해서는 open
* modfiacation(수정) ->기존코드에 대해선 closed되어있다(단 한줄도 바뀌지는 않는다.)
  * 솔리드에서 open-closed

# ADT(abstruct datatype)
* Queue
 - Q.empty() -> Boolean ( 큐가 비어있으면, True 아니면 False)
 - Q.enqueue(data) -> None (큐의 맨 뒤에 데이터를 쌓는다)
 - Q.dequeue() -> data (큐의 맨앞에 데이터를 삭제하면서 반환)
 - Q.peek() -> data (큐 맨앞 데이터를 반환)

# process와  Thread

# 퀵소트
* sort
1. conporison sort : 두수를 비교해서 정렬
  * simple sort - O(n**2)
   - bubble sort (거품 정렬)
   - insertion sort (삽입 정렬)
   - selection sort (선택정렬) 
  * divide and conquer -  O(n log n)
   - *** quick sort (퀵 정렬)
   - merge sort (합법 정렬)  -- 
   - heap sort
2. non - conparison sort

generater
 - yield
 - yield from
async io

Thread Pool
 s = socket. sodcef() slow
 connect
 s.send(regredt)
?? fetch
Task Pool 

iterpreter
linked list (simple Liked List)
 - 알고리즘이 어떻게 되는지
 - node / link로 구성이 된다. 노드는 데이터를 담고 링크는 각 노드를 연결
 - 연결리스트는 메모리가 필요하면 할당, 필요없으면 해제하는식으로 메모리 관리가 가능하다
 - 배열 처럼 메모리에 연속적으로 [1,2,3,4] <- 이렇게 할당 되지 않고 임의로 할당된 뒤에 각  요소들을 링크로 연결 하는 방식
 - 단순 연결리스트는 사용자가 첫번째 노드를 알고 있어야 연결 리스트에 진입할수 있으며 마지막 노드는 아무것도 가리키지 않게 함
 - size 해주는 이유 : 지금 현재 몇개가 있다 이렇게 알기 위해 
-아티클 영상 강의 보기
Double linked list
 - 더미 : 데이터를 가지지 않은 노드를 의미
 - instance Member
   1. head - 리스트 맨 앞에 있는 더미를 가리킨다
   2. tail - 리스트 맨 뒤에 있는 더미를 가리킨다.
   3. d_size - 리스트의 요소개수
add / searced / delete / insert
더미 빼고 링크드 리스트로 구현
스택과 큐를 연결리스트로 구현하기
is ? 
동적 / 정적
-----------------------------
oop(중요)
1. 객체지향이란?
2. 캡슐화
   정보은닉
   다형성
3. solid
   1. single responsibilrty prmc (단일 책임)
   2. Dpen-closed pm (확장-폐쇄)
   3. Liskov substitation prm (리스코프 치환)
   4. interface segregation prm (인터페이스 분리)
   5. Dependoncy inversion prm (의존 역전)
4. 디자인패턴 (Design pattern)    GOF
  7가지 정도....

process - thread
 1. concurency programe(동시성 프로그래밍)
    1) 멀티 스레딩 -> (약점) race condition -> (해결책) mutual exclusion(상호배제)
 2. asynchroaus I/O
     비동기 I/O (자바스크립트)

 * 1_1) Thraed pool (스레드 풀)
 * 2_1) task pool -> async I/O -> 3.7.2  (vasync / awact / ...)
 vs
 parrellesm programeing

Network -> os 7계층 Tcp/IP 4계층 -> 프로토콜
socket programe - echo server - client
                            - chat server -client

glossary - iterable용어는 이렇게 번역하는 편이 좋음
iterable의 의미
- 자신의 멤버를 한 번에 리턴할 수 있는 객체
- member를 하나씩 차례로 반환가능한 object를 말함
- 대표적인 예로는 sequence type인 list, str, tuple,dict 이있다.

iterator의 의미
- "next()" Method로 데이터를 순차적으로 호출 가능한 Object이다.
- 만약 next()로 다음 데이터를 불러 올수 없을 경우 Stoplteration exception을 발생시킨다.

iter() 함수를 사용하여 list를 listiterator 타입으로 변경 가능하다
ex)
x=[1,2,3]
type(x)  >> type 'list'
y = iter(x)
type(y) >> type 'listiterator' 으로 바뀐다.

immutable : 값이 변하지 않는다
- Number / String / Tuple / 
mutable : 값이 변한다.
- List / Dictionary
===
closure
def inner(a,b):
    #a = 123 <-- 정보은닉?
    def outter(a_1):
        return (a,b) <-- 위 함수의 parameter를 쓰는것도 closure 라고 할 수 있다.
    return outter

