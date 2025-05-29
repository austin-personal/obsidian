
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
![[Pasted image 20250528222717.png]]
### 1. Create MemberApp.java
### 2. Create PSVM 
### 3. Inject dependency of MemberService And its Implementation
	- `MemberService service = new MemberServiceImpl();`
### 4. Create a member object
- Member member = new Member( 멤버 정보들)
### 5. 멤버 서비스 구현체 사용


# 4. 주문과 할인 도메인 설계
### 4.1 주문 도메인 협력, 역할, 책임
![[Pasted image 20250528223323.png]]
### 4.2 주문 도메인 전체
![[Pasted image 20250528223411.png]]
- 역활(인터페이스가 될놈들)과 구현을 분리 해서 자유롭게 구현 객체를 조립할 수 있게된다. 
	- 역할: 할인 정책 역할
	- 할인 정책 (구현채)
		- 정액할인
		- 정률할인


![[3. 스프링 핵심 원리 이해2 - 객체 지향 원리 적용.pdf]]
# 5. 새로운 할인 정책 개발
- 새로운 할인 정책 구현체 생성
- `orderServiceImpl`에 
	-`private final DiscountPolicy dp = new RateDiscountPolicy` 라고 설정해둠. 
# 6. 새로운 할인 정책 개발의 문제점
![[Pasted image 20250529115353.png]]
- 문제:
	  - 폴리시를 바꿀때마다(확장), OrderService에 수정을 해야함 (OCP에 위배)
	  - 상위 객체인 orderService가 하위 객체인 discountPolicy에 직접 의존하고 있다. (DIP 위배)
- 해결: 
	- `orderServiceImpl`는 DiscountPolicy라는 추상화에만 의존하도록 바꿈
	- ==누군가가 클라이언트인 orderServiceImpl 에 DiscountPolicy의 구현 객체를 대신 생성하고 주입해야한다==

# 7. 관심사와 분리
- 6번에서의 문제
	- 로미오 역할(인터페이스)을 하는 디카프리오(구현체)가 줄리엣역할(인터페이스)을 하는 여자주인공(구현체)을 직접 초핑하는 것
	- 해결:  ==누군가가 클라이언트인 orderServiceImpl 에 DiscountPolicy의 구현 객체를 대신 생성하고 주입해야한다==
#### 7.1 생성자 주입
- 클라이언트에서 바로 인터페이스와 구현체를 연결 시키는 것을 생성자로 대체하여 의존성을 없엔다.
1. AppConfig 클래스를 새로 생성
2. 기존 MemberServiceImpl에 직접 인터페이스와 구현체를 정해줬던것을 없엔다.
3. 없엔 로직을 AppConfig에 넣는다.
4. MemberServiceImpl에는 해당 인터페이스의 생성자만 남긴다. 
#### 7.2 여전한 문제
- Appconfig에서 역활에 따른 구현이 잘 보이지 않는다. 
- 중복되는 구현체

# 8. AppConfig refactoring
![[Pasted image 20250529153714.png]]

#### 8.1 중복 해결
#### 8.2 역활(DiscountPolicy)과 구현(RateDiscountPolicy)이 잘 보이도록 변경


# 9. 새로운 구조에서 할인 정책 변경
![[Pasted image 20250529153954.png]]
- 구조체가 만들어졌음으로 구조체에서 구현 객체만 바꿔 끼면 끝.
- 사용영역의 변경 없이 구성영역만 바꾸면 된다. 
> 구현체 = Implementation
> 구현객체 = Interface와 구현체로 만들어진 객체


# 10. 지금까지 Recap
### L/O
1. 자바프로젝트 기본구성요소
2. 생성자 주입
3. SRP
	1. 문제: 클라이언트 객체가 직접 구현 객체 (생성, 연결) 설정하고 실행까지함
	2. 해결: AppConfig에서 구현객체를 설정하고 클라이언트에서는 실행만함
4. DIP
	1. 문제: 상위 객체가 하위객체의 인터페이스와 구현체에 의존함
	2. 해결: AppConfig에서 구현체 생성후 상위객체에 의존성 주입 (상위 객체는 인터페이스만 의존. 해당 인터페이스의 생성자가 AppConfig에서 설정된 구현객체에 의존)
5. OCP
	1. AppConfig를 도입함으로서 :
		1. 확장할때 수정할필요 없어짐
		2. 애플리케이션을 사용영역과 구성영역으로 나눔
		3. 확장할때 구성영역의 AppConfig만 수정하면 됨


# 11. IoC, DI And Container
#### [[IoC (inversion of control)]]
- 클라이언트 객체에서 하위 클래스들을 실행만 함. 정확히 어떤 것을 실행할지 결정하는 것은 AppConfig.
- 이렇듯 프로그램의 제어흐름을 직접제어하는 것이 아니라 외부에서 관리하는 것을 제어의 역전이라고 한다
- 프레임워크 VS 라이브러리
	- 내가 작성한 코드를 제어하고 대신 실행 -> 프레임워크 (JUnit)
	- 내가 작성한 코드가 직접 제어의 흐름을 담당 -> 라이브러리

#### [[DI (Dependency Injectyion)]]
- AppConfig처럼 구현 객체를 대신 생성하여 다른 클래스에 의존성을 주입하는 것

#### IoC Container & DI Container
- AppConfig
- 둘의 기능이 비슷하여 보통 DI container로 통용된다. 
- 다르게 불리는 경우도 있다: 어셈블러

# 12. Spring으로 전환
### 12.1.  스프링 컨테이너에 설정 정보 추가하기
1. AppConfig class에 @configuration 어노테이션 추가
	- 각 메소드별로 @Bean 추가
2. 클라이언트 객체에 스프링 컨테이너 생성자 생성: `ApplicationContext applicationContext = new AnnotationConfigApplicationContext(AppConfig.class)`
3. `applicationContext.getBean(MemberService, MemberServoce.class)`로 구현객체 가져오기
결론:
- AppConfig를 더이상 자바로 연결해주는 것이 아니라, 스프링 컨테이너에 등록하고 클라리언트에서도 스프링컨테이너를 사용하는 것이다. 
- 여기까지는 기존 AppConfig기능과 동일 오히려 어노테이션이 추가 되어 더 복잡해지기만 했는데 스프링 빈에 설정정보를 등록하는 게 좋은 이유는 뭘까? 

