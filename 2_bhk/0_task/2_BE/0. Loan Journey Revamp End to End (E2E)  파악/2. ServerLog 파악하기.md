Kerberos 
- kinit
- ssh
- less file_name.log
- :/17324235235235 (client_id 입력)
	- N 이전 n이후 로 돌아다니기

~~~
+-------------------------------------------------------------+
| A. UnderwritingJpaEntity.setLastEvaluatedStep               |
|    underwritingId=436, clientId=1747889887552000579         |
|    상태: IN_PROGRESS, 단계: BASIC                            |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| B. OfferUnderwritingApplicationService                       |
|    언더라이팅 시작                                          |
|    (UnderwritingStartContext: clientId, loanApplicationId…)  |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| C. EvaluationApplicationService                              |
|    Evaluation 시작 (evaluationResultId=3803)                |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| D. OutboxMessageStageScheduler                                |
|    [OutBox] Fetched 0 outbox events                          |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| E. DynamicRuleEvaluationService                              |
|    [evaluate][start][root] (DYNAMIC_REPORT_VERSION_DECIDER)  |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| F. DynamicRuleEvaluationService                              |
|    [evaluate][start] (초기 EvaluationDecision 생성)         |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| G. DynamicRuleEvaluationService                              |
|    [parseCondition][start] (조건: 1==1)                      |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| H. DynamicRuleEvaluationService                              |
|    [parseCondition][end] (conditionResult: true)             |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| I. DynamicRuleEvaluationService                              |
|    [parseAction][start]                                      |
|    (action: setAcsReportVersion, setAcsSmsReportVersion)     |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| J. DynamicRuleEvaluationService                              |
|    [parseAction][end] (parseActionResult 적용 완료)         |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| K. DynamicRuleEvaluationService                              |
|    [evaluate][end] (실행된 룰: ACS_REPORT_FOIR_EVALUATION)   |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| L. CreditReportReadinessService                              |
|    CreditReportStatusResolver prepared for loanId: 2249080   |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| M. ClientCreditReportEvaluationProcessor                     |
|    Experian report needed for loanId: 2249080 CL             |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| N. BankTransactionStatusUpdateScheduler                       |
|    fetchSize: 0                                              |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| O. BankTransactionStatusUpdateScheduler                       |
|    No transactions to process                                |
+-------------------------------------------------------------+
                    |
                    v
+-------------------------------------------------------------+
| P. OfferUnderwritingEvaluationApplicationService              |
|    Underwriting evaluation is not passed (underwritingId:436)|
+-------------------------------------------------------------+
~~~
# Apply 이후 ServerLog 보기
- 시간기준은 UTC 0이다. 
	- 13시 50분쯤부터 (키바나)
	- 04시 50분부터 (ServerLog)
## pattern 1

04:58:05.184 - b37288842e2c8f72 7b531f6b34035d60 - - [underwriting-10] DEBUG c.t.t.a.o.e.OfferUnderwritingEvaluationApplicationService[65] - Underwriting evaluation is not passed, underwritingId: 436
cc.truecredits.truecreditlms.domain.creditevaluation.CreditReportRequiredException: CreditReport Required

---
![[스크린샷 2025-06-02 오후 4.35.29.png]]
n
04:58:06.144 - 80c4b733d9c69291 37ac356d48082a15 - - [underwriting-10] INFO  c.t.t.d.a.a.r.LoanAcsReportService[68] - [LoanAcsReportService-findRetrieved] acs report not found for evaluation Id 3806
04:58:06.147 - 80c4b733d9c69291 423319435ca308c3 - - [underwriting-10] INFO  c.t.t.infra.acs.AcsCaller[174] - [ACSCaller:retrieveAcsSmsReport] loanId: 2249080, version: V3
04:58:06.179 - 8e188114cdd6ff3f 8e188114cdd6ff3f - - [scheduler-thread-pool-1] INFO  c.t.t.b.BankTransactionStatusUpdateScheduler[114] - fetchSize : 0
04:58:06.180 - 8e188114cdd6ff3f 8e188114cdd6ff3f - - [scheduler-thread-pool-1] INFO  c.t.t.b.BankTransactionStatusUpdateScheduler[117] - No transactions to process
04:58:06.193 - 32e6141a3e9f2e78 32e6141a3e9f2e78 - - [scheduler-thread-pool-7] INFO  c.t.t.b.BankTransactionStatusUpdateScheduler[114] - fetchSize : 10
04:58:06.194 - 32e6141a3e9f2e78 32e6141a3e9f2e78 - - [scheduler-thread-pool-7] INFO  c.t.t.b.BankTransactionStatusUpdateScheduler[117] - No transactions to process
04:58:06.215 - efd49408452a51e1 efd49408452a51e1 - - [scheduler-thread-pool-2] INFO  c.t.t.b.BankTransactionStatusUpdateScheduler[114] - fetchSize : 10
04:58:06.216 - efd49408452a51e1 efd49408452a51e1 - - [scheduler-thread-pool-2] INFO  c.t.t.b.BankTransactionStatusUpdateScheduler[117] - No transactions to process
04:58:06.233 - 80c4b733d9c69291 a57ef9621f6264d2 - - [underwriting-10] INFO  i.t.c.o.OkHttpB3PropagationInterceptor[32] - Failed to treat request: Request{method=POST, url=https://stage-acs.truebalance.cc/sms-score/v3, headers=[X-B3-TraceId:80c4b733d9c69291, X-B3-SpanId:a57ef9621f6264d2, X-B3-Sampled:1]}
java.io.IOException: Unexpected response code for CONNECT: 502

---
## pattern 2
![[스크린샷 2025-06-02 오후 4.33.46.png]]
04:58:06.386 - 80c4b733d9c69291 eb1f06239c9d8b64 - - [underwriting-10] INFO  c.t.t.d.a.a.s.AcsSmsReportV3Preparator[30] - [AcsSmsReportV3Preparator] Preparing AcsReport for  SMS_V3_CIBIL, loanId 2249080
04:58:06.386 - 80c4b733d9c69291 eb1f06239c9d8b64 - - [underwriting-10] INFO  c.t.t.d.a.a.s.AcsSmsReportV3Preparator[46] - [AcsSmsReportV3Preparator] Preparing AcsReport for  SMS_V3_CIBIL, loanId 2249080
04:58:06.389 - 80c4b733d9c69291 eb1f06239c9d8b64 - - [underwriting-10] INFO  c.t.t.d.a.a.s.AcsSmsReportV3Preparator[56] - [AcsSmsReportV3Preparator] Retrieving AcsReport for  SMS_V3_CIBIL, CreditBureauNameCode CIBIL
04:58:06.392 - 80c4b733d9c69291 eb1f06239c9d8b64 - - [underwriting-10] INFO  c.t.t.d.a.a.r.LoanAcsReportService[68] - [LoanAcsReportService-findRetrieved] acs report not found for evaluation Id 3807
04:58:06.393 - 80c4b733d9c69291 87557924d7adc7df - - [underwriting-10] INFO  c.t.t.infra.acs.AcsCaller[174] - [ACSCaller:retrieveAcsSmsReport] loanId: 2249080, version: V3
04:58:06.400 - 80c4b733d9c69291 d0ff8bc60a00aa2a - - [underwriting-10] INFO  i.t.c.o.OkHttpB3PropagationInterceptor[32] - Failed to treat request: Request{method=POST, url=https://stage-acs.truebalance.cc/sms-score/v3, headers=[X-B3-TraceId:80c4b733d9c69291, X-B3-SpanId:d0ff8bc60a00aa2a, X-B3-Sampled:1]}
java.io.IOException: Unexpected response code for CONNECT: 502



---
## 각 패턴 하위 에러 메세지
05:00:02.860 - 3be534c5a812f365 351e43a825d1d059 - - [underwriting-10] INFO  i.t.c.o.OkHttpB3PropagationInterceptor[32] - Failed to treat request: Request{method=POST, url=https://stage-acs.truebalance.cc/sms-score/v3, headers=[X-B3-TraceId:3be53
4c5a812f365, X-B3-SpanId:351e43a825d1d059, X-B3-Sampled:1]}
java.io.IOException: Unexpected response code for CONNECT: 502

05:00:02.861 - 3be534c5a812f365 86e4e539cd14196b - - [underwriting-10] WARN  i.t.c.o.MonitoringEventListener[53] - Call to [POST https://stage-acs.truebalance.cc/sms-score/v3] failed with exception.
java.io.IOException: Unexpected response code for CONNECT: 502

05:00:02.861 - 3be534c5a812f365 86e4e539cd14196b - - [underwriting-10] WARN  c.t.t.infra.acs.AcsCaller[110] - Fail to communicate.
java.io.IOException: Unexpected response code for CONNECT: 502

05:00:02.861 - 3be534c5a812f365 86e4e539cd14196b - - [underwriting-10] WARN  c.t.t.infra.acs.AcsCaller[183] - [ACSCaller:retrieveAcsSmsReport] Could not get ACS SMS Report, loanId: 2249080
cc.truecredits.truecreditlms.commons.exception.GeneralException: Internal Error

Caused by: java.io.IOException: Unexpected response code for CONNECT: 502

05:00:02.886 - 3be534c5a812f365 9264edcbe72d583c - - [underwriting-10] DEBUG c.t.t.a.o.e.OfferUnderwritingEvaluationApplicationService[65] - Underwriting evaluation is not passed, underwritingId: 436
cc.truecredits.truecreditlms.domain.creditevaluation.AcsSmsReportRequireException: Required ACS SMS Report

