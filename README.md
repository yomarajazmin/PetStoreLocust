#Performance on Pet store

*Pre-requisites*:
- Have swagger pet store runnning (https://github.com/swagger-api/swagger-petstore?tab=readme-ov-file)

Comand to run the execution:
```
locust --host=http://localhost:8080/api/v3
```

Scenario:
- Users: 100
- Runtime: 5m
- Spawn rate: 10
- Endpoints: Login user, get order, get pet, get inventory

Only gets where selected for this run because they usually tend to be the most consumed.

*From the report obtained* (report\report_1717844159.3413358.html):
- No failures because the load was small.
- There is a peak at the begining of the test in the response time, but it gradually diminishes until it begins to oscilate between 9 to 6 ms (95th percentile) and 2 to 3ms (50th percentile), indicating the overall response time of the endpoints took less than 9ms.
- The number of user was constant since a small number was used in this run.
