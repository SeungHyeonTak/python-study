Stack
======
## Node
*LIFO (Last In, First Out)*
> 가장 먼저 넣은것이 가장 나중에 나온다.
*무언가를 쌓아올리는 형태*
* stack은 기본적으로(주요기능) push() / pop()이 존재 한다.
![Alt text](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory&fname=http%3A%2F%2Fcfile2.uf.tistory.com%2Fimage%2F224D574F535BE4B82B3B0A)
* 함수의 콜스택에 쓰이고 문자열을 역순으로 출력할때, 연산자 후위표기법등에 쓰인다.

 - push() -> 데이터를 stack에 저장한다.
 - pop() -> 데이터를 stack에서 꺼낸다. / 데이터를 꺼내고 나서는 스택에서 해당 데이터를 삭제
 - peek() -> 데이터를 스택에서 꺼내기전에 잠깐 참조가능하다.
 - is_empty() -> 데이터가 비어있다면 pop연산을 실행 할 수 없다.
 - is_full() -> 데이터가 꽉차 있다면, push연산을 실핼할 수 없다.
 *Stack에 있는 모든 데이터를 차례대로 출력할 수 있어야 한다*
