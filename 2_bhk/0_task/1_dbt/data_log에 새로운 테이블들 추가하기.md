잭의 요청 테이블 Data_log에 추가하기
	1. truecredits.marketing_events_info  `DONE`
		- 비즈니스 로직 수정이 필요할듯? -> 마케팅 이벤트 데이터 생성시기가 다름 (Rejected가 됬을때 Applied 가 Insert됨)
	2. truecredits.tc_loan_acs_report_status_tracker  [완료는 했고 빌드 해보고 오류 수정 하자]
		1. underwriting_logs 와 evaluation_logs 에 추가하기 
	3. truecredits.tc_business_event
		1. underwriting_logs에 추가
			1. [문제가 있음] 이벤트가 개많음
2. Underwriting/Offer 파악하기
3. Underwriting/Offer 테이블 Data_log에 추가하기
4. prerequisite파악하기
5. prerequisite 테이블들 Data_log에 추가하기
   
# All events

- __대출/심사 관련__

  - UnderwritingStarted
  - UnderwritingCreated
  - EvaluationPassed
  - LoanRejectedEvent
  - LoanWithdrawEvent
  - ReroutingRequiredEvent
  - LoanJourneyEventFireDone
  - OverDueChargesAppliedOnPartnerLoanEvent

- __오퍼/제안 관련__

  - OfferCreatedEvent
  - OfferTakenEvent
  - OfferDisbursementRequestedEvent
  - PrerequisiteStartEvent

- __문서/계약 관련__

  - EvaluationDocumentChangeEvent
  - LoanDocumentEvent
  - DisbursementEvent

- __마케팅/동의/알림 등__

  - ConsentStored
  - SmsNotificationEvent

- __기타__

  - BankTransactionEvent
  - PartnerPennyDropEvent
  - LoanClosedEvent


# 잭과 미팅
1. 