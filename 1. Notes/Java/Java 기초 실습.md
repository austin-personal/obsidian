
자바로만 만드는 실습
# 0. 비즈니스 요구사항과 설계
### 비즈니스 요구사항
- 회원
	- 회원 데이터는 자체 db로 할지 외부 서비스를 사용할지 모름
- 주문과 할인 정책
	- - 할인 정책은 정해지지 않았다.



# 1. 회원 도메인 설계
### 회원 도메인 요구사항
- 회원
	- 회원 데이터는 자체 db로 할지 외부 서비스를 사용할지 모름

### 회원 도메인 설계

![[Pasted image 20250528183016.png]]
- 회원도메인 협력 관계
- 회원 클래스 다이어그램: 전체적인 클래스 구조
	- 회원 저장소 interface: db가 바뀌어도 interface에서 다른 db를 연결하는 코드 한줄만 바꾸면 됨
	- 회원 서비스: MemberService interface와 MemberServiceImpl 로 구성
		- implt은 구현이란 뜻
- 회원 객체 다이어그램: 전체적인 클래스 구조가 실제 서버위에 떴을때의 다이어그램
	- 클래스 다이어 그램과 다른 점: 클래스 다이어그램의 각 [[구현체]]들은 서버가 떴을 때 어떤 구현체가 사용될지 동적으로 변한다. 클래스 다이어그램이 서버에서 돌때 스냄샷
	- 클라이언트 -> 회원 서비스(MemberServiceImpl) -> 메모리 회원 저장소
# 2. 회원 도메인 개발
### 1. Create Member package 
- Package = Folder
### 2. Grade ENUM
- 회원 등급 설정
### 3. Member CLASS
- 속성
	- private Long id
	- name
	- grade
- getter setter
	- 해당 클래스의 속성값을 넣기/불러오기 위한 겟과 셋
	- 속성은 Private이기 때문에 겟과 셋으로 접근한다
### 4. MemberRepo Interface
- 인터페이스와 하단의 implimentation은 항상 동행한다. 
### 5. MemoryMemberRepository Implimentation
- Override
- Map
- Method
	- Save
	- findById
### 6. MemberService interface
- Methods
	- join
	- findMember
### 7. MemberSeviceImpl implimentation
- 인터페이스의 실제 구현체들
	- MemberService의 비즈니스 로직인 조인과 맴버 찾기 기능구현
	- 이것들은 실제 DB에 저장하는 로직들이다. 
		- 그렇기에 레포지토리와 연결 시켜야한다.
		- 이떄 전에 만든"MemberRepo Interface" 를 선언한다. 
		- `private final MemberRepository memberRepository;`
		- 하지만 인터페이스만 선언하면 NullExceptiion이 난다. 실제 Impl이 없기 때문이다. 
		- 그래서 ` private final MemberRepository memberRepository = new MemoryMemberRepository Implimentation
- Methods
	- join
	- findMember
# 3. 회원 도메인 실행과 테스트
### 1. Create MemberApp.java
### 2. Create PSVM 
### 3. Inject dependency of MemberService And its Implementation
	- `MemberService service = new MemberServiceImpl();`
### 4. Create a member ob 