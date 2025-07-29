# MUW (Manual Underwriting) 시스템 분석 문서
## 1. 개요

MUW(Manual Underwriting)는 자동 심사를 통과하지 못한 대출 신청을 수동으로 심사하는 시스템입니다. 대출 상태가 `MANUAL_EVALUATION_WANTED`로 변경되면 MUW 프로세스가 시작됩니다.

## 2. MUW 프로세스 흐름

### 2.1 MUW 시작 트리거

- 대출 평가 결과 → `MANUAL_EVALUATION_WANTED` 상태 변경

- `EvaluationDecisionPostProcessor.postProcessForManualEvaluation()` 실행

- 슬랙 알림 발송 및 CB 스코어 태그 저장
### 2.2 주요 처리 로직 위치

- **EvaluationDecisionPostProcessor:64-66** - MUW 상태 감지 및 이벤트 발송

- **SlackManualEvaluationEventSender:35-67** - 슬랙 알림 발송

- **ManualEvaluator:164-166** - MUW 승인/거절 처리 및 상태 검증

  

## 3. MUW 관련 데이터베이스

  

### 3.1 MUW 전용 테이블

  

#### `manual_evaluation_assigned_case`

- **목적**: MUW 케이스 할당 정보

- **주요 필드**: `loan_id`, `cpa_user_id`, `score`, `status`, `cpa_comments`, `approved_by`

- **상태**: `ASSIGNED`, `ACTIVE`, `ON_HOLD`, `REJECTED`, `WAITING_FOR_APPROVAL`, `APPROVED` 등

  

#### `manual_evaluation_queue`

- **목적**: MUW 대기열 관리

- **주요 필드**: `loan_id`, `status`, `whatsapp_enabled`, `category`

- **카테고리**: `CL`, `LVL`, `WL`, `CL_WO_BS`

  

#### `manual_evaluation_form_data`

- **목적**: MUW 폼 데이터 저장 (JSON 형태)

- **주요 필드**: `loan_id`, `form` (JSON)

  

#### `manual_evaluation_user`

- **목적**: MUW 사용자 관리

- **역할**: `MAKER`, `CHECKER`

  

#### 기타 테이블

- `manual_evaluation_assigned_case_history` - 케이스 히스토리

- `manual_evaluation_maker_checker_map` - 심사자-검토자 매핑

- `manual_evaluation_queue_history` - 대기열 히스토리

- `manual_evaluation_user_sign_history` - 사용자 로그인/로그아웃 히스토리

  

### 3.2 공통 테이블

  

#### `tc_loan_evaluation_history`

- **목적**: 대출 평가 히스토리

- **주요 필드**: `loan_id`, `decision_response` (JSON), `status`, `sub_status`

  

#### `tc_loan_tag`

- **목적**: 대출 태그 정보

- **MUW 관련 태그**:

- `CB_SCORE`

- `MANUAL_ESTIMATED_INCOME`

- `MANUAL_REFERENCE_NO`

- `MANUAL_OBLIGATION`

- `UNDER_EVALUATION`

  

#### `tc_evaluation_result_log`

- **목적**: 평가 결과 로깅

- **주요 필드**: `evaluation_id`, `type`, `decision_path`

- **MUW type 예시**: `LOAN_TERMS_MUW__CL__12__WITH_BS`

  

## 4. MUW 승인 처리 흐름

  

### 4.1 승인 프로세스

1. **ManualEvaluator.approveApprovedAmount()** - MUW 승인 처리

2. **ManualUnderWriteOfferCreationService.updateEvaluationAndCreateOffer()** - 평가 결과 업데이트 및 오퍼 생성

3. **EvaluationResultLogService.log()** - 결과 로깅

  

### 4.2 승인 시 저장되는 정보

- 승인 금액, 추정 소득, 참조 번호, 의무사항

- 심사자 정보 및 코멘트

- 평가 결과 및 결정 정보

  

## 5. 데이터 로깅 시스템

  

### 5.1 tc_evaluation_result_log의 JSON 구조

  

**JSON 생성 과정:**

```java

Jackson.writeValueAsString(context.getDecisionResponse())

```

  

**DecisionResponse 주요 MUW 필드:**

- `evaluationProcessorType`: "LOAN_TERMS_MUW"

- `manualEstimatedIncome`: MUW 심사자 입력 추정 소득

- `manualReferenceNo`: MUW 참조 번호

- `manualObligation`: MUW 의무사항

- `comments`: MUW 심사 코멘트

- `approvedAmount`: MUW 승인 금액

  

### 5.2 Type 컬럼 생성 규칙

  

**생성 로직:**

```java

attributes.add(decisionResponse.getEvaluationProcessorType().name()); // LOAN_TERMS_MUW

attributes.add(decisionResponse.getCategory().name()); // CL

attributes.add(decisionResponse.getAppliedTenure().toString()); // 12

Collections.addAll(attributes, evaluationTypeAttributes); // WITH_BS

return String.join("__", attributes);

```

  

**결과 예시:** `LOAN_TERMS_MUW__CL__12__WITH_BS`

  

## 6. 주요 서비스 클래스

  

### 6.1 핵심 서비스

- **ManualEvaluator** - MUW 승인/거절 처리

- **ManualUnderWriteOfferCreationService** - MUW 오퍼 생성

- **EvaluationDecisionPostProcessor** - MUW 후처리

- **SlackManualEvaluationEventSender** - 슬랙 알림

  

### 6.2 지원 서비스

- **ManualEvaluationEventSender** - MUW 이벤트 발송 인터페이스

- **EvaluationResultLogService** - 평가 결과 로깅

- **MuwLimitAdjustmentService** - MUW 한도 조정

  

## 7. 알림 시스템

  

### 7.1 슬랙 알림

- MUW 필요 시 슬랙 채널에 알림 발송

- 대출 정보, 스코어, 소득 등 상세 정보 포함

- 심사자가 수동으로 승인/거절 처리 가능

  

### 7.2 알림 내용

- Loan ID, Repeat User 여부

- 소득 정보 (V4), 사용자 신고 소득

- Bank Score, PoD, FinBox Score

- 신용 한도, 상환 조건, 승인 정보

  

## 8. 데이터 분리

  

### 8.1 저장 위치별 데이터 구분

  

**tc_evaluation_result_log JSON:**

- DecisionResponse 객체 전체

- 대출 평가 결과 데이터

- MUW 관련 기본 정보만 포함

  

**MUW 전용 테이블:**

- MUW 프로세스 관리 정보

- 케이스 할당, 대기열, 사용자 관리

- 별도 생명주기 관리

  

---

  




# ⏺ MUW (Manual Underwriting) 워크플로우

  1. MUW 시작 흐름

  graph TD
      A[자동 심사 실행] --> B{심사 결과}
      B -->|통과| C[승인 처리]
      B -->|실패| D[MANUAL_EVALUATION_WANTED 상태 변경]
      D --> E[LoanMuwHelperService.moveLoanToMuwAndNotify]
      E --> F[manual_evaluation_queue 테이블에 등록]
      E --> G[EvaluationDecisionPostProcessor 실행]
      G --> H[CB_SCORE 태그 저장]
      G --> I[SlackManualEvaluationEventSender 호출]
      I --> J[슬랙 알림 발송]

  2. MUW Queue 관리 흐름

  graph TD
      A[manual_evaluation_queue 등록] --> B[상태: READY_TO_ASSIGN]
      B --> C[ManualUnderwriteCaseAssignService 실행]
      C --> D{할당 가능한 케이스?}
      D -->|없음| E[할당 대기]
      D -->|있음| F[우선순위별 케이스 선택]
      F --> G[ManualEvaluationAssignedCaseDTO 생성]
      G --> H[manual_evaluation_assigned_case 등록]
      H --> I[Queue 상태: ASSIGNED로 변경]

  3. MUW 심사 처리 흐름

  graph TD
      A[심사자 할당 완료] --> B[상태: ASSIGNED]
      B --> C[심사자 검토]
      C --> D{심사 결정}
      D -->|승인| E[ManualEvaluator.approveApprovedAmount]
      D -->|거절| F[ManualEvaluator.reject]

      E --> G[승인 정보 입력]
      G --> H[ManualUnderWriteOfferCreationService 호출]
      H --> I[DecisionResponse 업데이트]
      I --> J[EvaluationResult 저장]
      J --> K[tc_evaluation_result_log 기록]
      K --> L[Offer 생성]
      L --> M[상태: APPROVED]

      F --> N[거절 사유 입력]
      N --> O[대출 거절 처리]
      O --> P[슬랙 거절 알림]
      P --> Q[상태: REJECTED]

  4. 데이터 저장 흐름

  graph TD
      A[MUW 프로세스 시작] --> B[manual_evaluation_queue]
      B --> C[manual_evaluation_assigned_case]
      C --> D[tc_loan_tag - MUW 관련 태그]
      D --> E[tc_loan_evaluation_history]
      E --> F[tc_evaluation_result_log + JSON 파일]

      G[히스토리 테이블들] -->
  H[manual_evaluation_assigned_case_history]
      G --> I[manual_evaluation_queue_history]
      G --> J[tc_loan_tag_history]

  5. 상세 워크플로우

  5.1 MUW 요청 단계

  6. 자동 심사 실패 → MANUAL_EVALUATION_WANTED 상태
  7. LoanMuwHelperService.moveLoanToMuwAndNotify() 실행
  8. manual_evaluation_queue 테이블에 등록 (loanId, score, category)
  9. EvaluationDecisionPostProcessor.postProcessForManualEvaluation()
  실행
  10. CB_SCORE 태그 저장
  11. 슬랙 알림 발송 (대출 정보, 스코어 등 포함)

  5.2 심사자 할당 단계

  12. ManualUnderwriteCaseAssignService.assignNewCase() 실행
  13. 우선순위별 케이스 선택 (CL > LVL > WL > CL_WO_BS)
  14. manual_evaluation_assigned_case 테이블에 할당 정보 저장
  15. Queue 상태 ASSIGNED로 변경
  16. 할당 알림 (선택사항)

  5.3 MUW 승인 처리 단계

  17. 심사자 검토 및 승인 결정
  18. ManualEvaluator.approveApprovedAmount() 실행
  19. 승인 정보 입력: 추정소득, 참조번호, 의무사항, 코멘트
  20. ManualUnderWriteOfferCreationService.updateEvaluationAndCreateOff
  er() 호출
  21. DecisionResponse 업데이트: LOAN_TERMS_MUW, 승인 정보 설정
  22. EvaluationResult 상태 APPROVED로 변경
  23. tc_evaluation_result_log 기록 + JSON 파일 저장
  24. Offer 생성 및 대출 상태 DISBURSEMENT_NOT_REQUESTED로 변경

  5.4 MUW 거절 처리 단계

  25. 심사자 검토 및 거절 결정
  26. ManualEvaluator.reject() 실행
  27. 거절 사유 입력
  28. 대출 거절 처리 (MANUALLY_REJECTED)
  29. 슬랙 거절 알림 발송
  30. 태그 저장: 거절 관련 정보

  31. 주요 상태 변화

  | 단계       | 테이블                             | 상태/값
                           |
  |----------|---------------------------------|----------------------
  -----------------|
  | MUW 요청   | Loan                            |
  MANUAL_EVALUATION_WANTED              |
  | Queue 등록 | manual_evaluation_queue         | READY_TO_ASSIGN
                     |
  | 심사자 할당   | manual_evaluation_assigned_case | ASSIGNED
                        |
  | 심사 진행    | manual_evaluation_assigned_case | ACTIVE
                       |
  | 승인 완료    | manual_evaluation_assigned_case | APPROVED
                       |
  | 승인 완료    | Loan                            | APPROVED →
  DISBURSEMENT_NOT_REQUESTED |
  | 거절 완료    | manual_evaluation_assigned_case | REJECTED
                       |
  | 거절 완료    | Loan                            | REJECTED
                       |

  32. 알림 시스템

  7.1 슬랙 알림 시점

  - MUW 요청 시: 심사 필요 알림 (대출 정보, 스코어 등)
  - MUW 거절 시: 거절 처리 알림 (심사자 정보 포함)

  7.2 WhatsApp 연동

  - manual_evaluation_queue에서 관리
  - 고객 동의 여부에 따른 처리

  이 워크플로우는 MUW 시스템의 전체적인 처리 과정과 각 단계별 데이터
  흐름을 보여줍니다.
