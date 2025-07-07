# 1. VKYC
![[스크린샷 2025-06-09 오전 11.55.03.png]]
tc_video_kyc_attempt
tc_video_kyc_attempt_result
tc_video_kyc_loan_attempt_map

sddsd

# Selfie
# autopay
https://dev.truebalance.cc/api/v2/emandate/register/details?verificationMode=UPI&pgCompany=PAYU&offerId=1007&bankAccountId=501&lendingPartner=TC

/api/v2/emandate/register/details![[스크린샷 2025-06-09 오후 3.12.09.png]]
![[temp_image_1749609088188.png]]tag_val: CONFIRMATION_ON_EMANDATE_PROCESS


pay_later_id_user_map 만들어야함
- 다른 연결 고리가 user 밖에 없음 pay_later에는
- 근데 user_id는 주로 매핑이 안됨 -> 과거에 만들어진 건 안불러 오니까. 
	- 해결: client_user_map은 인크리멘탈로 하지말고 풀리프레쉬로한다? 
		- 일단은 기존 형태로 놔두고 나중에 범위를 전체로 돌리자. 