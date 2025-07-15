# building_logs_1
#7/14
## Steps
1. Download docker-compose file and env file from the devlake website
2. Modify env file into .env
3. In the docker-compose file you can check three containers: 
	1. mysql: The DB to store each productivity metrics/numbers
	2. grafana: The Monitoring visulaisation tool to visualise the Productivity metrics
	3. devlake: The Server that hosts/manages connecting thrid parties such as Github, Jira etc and gathering data. 
	4. config-ui: The UI page for devlake
4. I changes all 4 containers' version into latest
5. Run `docker-compose up`
6. Access into `localhost:4000`
7. Connect with github
8. Set up the project and connect with the third party connections
9. ***I Faced a connection problem related to endpointURL***
10. ***Solved with putting /api/v3/ at the end of the url***
11. ***I Faced a data gathering problem in github graghQL*** 
12. ***Solved by turnning off graphQL And using REST API***
	1. `bash
		➜  productivity-test git:(main) ✗ curl -X PATCH http://localhost:4000/api/plugins/github/connections/1 \     -H 'Content-Type: application/json' \ -d '{
           "name": "test",
           "endpoint": "https://github.balancehero.cc/api/v3",
           "authMethod": "AccessToken",
           "token": "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",
           "enableGraphql": false
         }'{"name":"test","id":1,"createdAt":"2025-07-14T13:19:04.919Z","updatedAt":"2025-07-14T13:26:30.362Z","endpoint":"https://github.balancehero.cc/api/v3","proxy":"","rateLimitPerHour":0,"authMethod":"AccessToken","token":"ghp_xduRhIIW********************s23Mxm36","appId":"","secretKey":"","installationId":0,"enableGraphql":false} 
13. After finishing gathering data, Go to Grafana that is linked to DevLake
14. Check the Gtihub Dashboards

![[스크린샷 2025-07-15 오후 1.14.20.png]]
# building_logs_2
#7/15
