1. 잭의 요청 테이블 Data_log에 추가하기
	1. truecredits.marketing_events_info  `DONE`
		- 비즈니스 로직 수정이 필요할듯? -> 마케팅 이벤트 데이터 생성시기가 다름 (Rejected가 됬을때 Applied 가 Insert됨)
	2. truecredits.tc_loan_acs_report_status_tracker  [완료는 했고 빌드 해보고 오류 수정 하자]
		1. underwriting_logs 와 evaluation_logs 에 추가하기 
	3. truecredits.tc_business_event
		1. underwriting_logs에 추가
2. Underwriting/Offer 파악하기
3. Underwriting/Offer 테이블 Data_log에 추가하기
4. prerequisite파악하기
5. prerequisite 테이블들 Data_log에 추가하기