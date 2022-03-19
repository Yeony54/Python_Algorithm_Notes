Python Coding Test Study

# Code Note

Algorithm 문제 풀이 중 많이 쓰이는 문법 정리



### 01. input()

python의 내장함수로 개행문자를 벗겨내어 문자열로 변환하여 return 한다.

백준 문제에서 맨 첫줄 N을 받을 때, input()을 사용

```python
N = int(input())
for i in range(N):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
```

간혹 많은데이터를 입력 받을 때, 시간초과가 발생할 수 있다.



### 02. sys.stdin()

file object로 사용자의 입력을 받는 buffer을 만들어 그 buffer에서 읽어들인다.

백준 문제에서 input()으로 입력받으면 시간초과가 발생할 수 있다.



```python
import sys
```

sys모듈을 import하여 사용한다.



**🛸 정해지지 않은 개수 사용자 입력 받을 때**

```python
nums = []
for line in sys.stdin:
	nums.append(line)
print(nums)

nums.append(line.strip()) # ?
```

`sys.stdin` 은 `^Z`를 입력받으면 종료한다.

개행문자가 입력되기 때문에 `strip()`이나 `rstrip()`으로 제거해 주어야 한다.



**🛸 한개의 정수를 입력받을 때**

```python
a = int(sys.stdin.readline())
```

> 📌 `a = sys.stdin.readline()` 를 하지 않는 이유
>
> `sys.stdin.readline()`은 한줄 단위로 입력받기 떄문에, 개행문자가 같이 받아진다. `5`를 입력하면 `5\n`이 저장되기 때문에, 개행문자를 제거해야 한다.
> 또 변수타입이 문자열 형태(str)로 저장되기 때문에, 정수로 사용하기 위해서 형변환을 거쳐야 한다.



🛸 **정해진 개수의 정수를 한줄에 입력받을 때**

```python
a,b,c = map(int,sys.stdin.readline().split())
```

`map`은 반복 가능한 객체(리스트 등)에 대해 각각의 요소들을 지정된 함수로 처리해주는 함수이다.



🛸 **임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때**

```python
data = list(map(int,sys.stdin.readline().split()))
```

`split()`은 문자열을 나눠주는 함수이다.
괄호안에 특정값을 넣어주면 그 값을 기준으로 문자열을 나누고, 아무값도 넣지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 나눈다.

`list()`는 자료형을 리스트형으로 변환해주는 함수이다.

> 📌  `map()`은 맵 객체를 만들기 때문에, 리스트형으로 바꿔주기 위해서 `list()`로 감싸주었다.



🛸 **임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장할 때**

```python
data = []
n = int(sys.stdin.readline())
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
```

이코드로 각 요소의 길이가 동일한 2차원 리스트도 만들 수 있고, 
각각 길이가 다른 2차원 리스트도 입력받을 수 있다.



**🛸 문자열 n줄을 입력받아 리스트에 저장할 때**

```python
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
```

컴프리헨션을 사용하여 간단하게 사용

`strip()`은 문자열 맨 앞과 맨 끝의 공백문자를 제거한다.



### 03. map

### 04. heapq

### 05. permutation

### 06. combination

### 07. if 한줄 (one-line)

- 결과 = A if 조건 else B
- 결과 = A if 조건 else B if 조건 else C

### 이외 유용한 함수

1. zip()

   - 동일한 개수로 이루어진 iterable한 객체들을 인수로 받아 묶어서 iterator로 반환

   ```python
    z = zip([1, 2, 3], ('A', 'B', 'C'))
   ```

2. all()

   - iterable한 객체를 인수로 받아서 원소가 모두 참이면 True, 아니면 False를 반환

   ```python
   a = all([1, 2, 3]) # True
   a = all([0, 1, 2]) # False
   ```

3. any()

   - iterable한 객체를 인수로 받아서 원소가 하나라도 참이면 True, 아니면 False를 반환

   ```python
   a = any([0, 1, 2]) # True
   a = any([0, False, []] # False
   ```

4. chain()

   - iterable한 객체들을 인수로 받아 하나의 iterator로 반환

   ```python
   c1 = [1, 2]
   ca = ['A', 'B']
   c = itertools.chain(c1, ca)
   ```

   

   



















Reference

[yeseolee.log - 파이썬 입력받기](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)