# python-api-assignment


**Before install**
- Cd into source code folder:
    - Install lib 
    - `sudo pip3 install -r requirement.txt`
- Install postgresql 11
    - `sudo apt-get install postgresql-11`
- Create user postgresql and database
    - `sudo -u postgres psql`
    - `create database demo;`
    - `create user demo with password 'demo';`
    - `grant all privileges on database demo to demo;`
- Cd into source code folder to create table anh columns:
    - `cd app`
    - `python3 customer`
- Create data demo
    - `python3 create_record_demo`
    
**Installation**

- Start service:
    - Cd into source code folder
    - Run command `gunicorn -b 0.0.0.0:8000 app:api --reload`
- Stop service
    `kill -9 $(lsof -i :8000)`

**Usage**

LOGIN

`http POST http://103.89.84.184:8000/login?email=<user>&pwd=<pass>`

Example

`http POST http://103.89.84.184:8000/login?email=danghieu1709@sample.test&pwd=test`

Response

```
200 OK
Time:391 ms
Size:386 B
Server →gunicorn/19.9.0
Date →Wed, 17 Jul 2019 16:46:21 GMT
Connection →close
content-length →0
content-type →application/json
set-cookie →token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjMzODg4NjMsInVzZXJfaWRlbnRpZmllciI6ImRhbmdoaWV1MTcwOUBzYW1wbGUudGVzdCJ9.YRrmTXN9wN-ewL_gA4wblU71NQAdsMk-ony6iLnwRKM; HttpOnly; Max-Age=86400; Path=/customers; Secure
```

CREATE

`http POST http://103.89.84.184:8000/customers?name=<customer_name>&dob=<customer_dob> { HEADER: { HEADER: authorization:<access_token> } }`

Example

`http POST http://103.89.84.184:8000/customers?name=test&dob=1992-09-17 { HEADER: { HEADER: authorization:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjMzODg4NjMsInVzZXJfaWRlbnRpZmllciI6ImRhbmdoaWV1MTcwOUBzYW1wbGUudGVzdCJ9.YRrmTXN9wN-ewL_gA4wblU71NQAdsMk-ony6iLnwRKM} }`

Response

`{
    "name": "test",
    "new_id": "100",
    "dob": "1992-09-17"
}`

READ

`http GET http://103.89.84.184:8000/customers/<id> { HEADER: { HEADER: authorization:<access_token> } }`

Example

`http GET http://103.89.84.184:8000/customers/10 { HEADER: { HEADER: authorization:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjMzODg4NjMsInVzZXJfaWRlbnRpZmllciI6ImRhbmdoaWV1MTcwOUBzYW1wbGUudGVzdCJ9.YRrmTXN9wN-ewL_gA4wblU71NQAdsMk-ony6iLnwRKM} }`

Response

`{
    "data": {
        "name": "Timothy Moran",
        "updated_at": "2002-06-27 14:34:23-04",
        "id": 10,
        "dob": "2014-04-04"
    },
    "error": "None"
}`

UPDATE

`http PUT http://103.89.84.184:8000/customers/<id>?<field_update>=<update_value> { HEADER: { HEADER: authorization:<access_token> } }`

Example

`http PUT http://103.89.84.184:8000/customers/20?name=test_again&dob=2000-09-17 { HEADER: { HEADER: authorization:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjMzODg4NjMsInVzZXJfaWRlbnRpZmllciI6ImRhbmdoaWV1MTcwOUBzYW1wbGUudGVzdCJ9.YRrmTXN9wN-ewL_gA4wblU71NQAdsMk-ony6iLnwRKM} }`

Response

`{
    "name": "test_again",
    "updated_at": "2019-07-17 13:49:31.283880",
    "id": 20,
    "dob": "2000-09-17"
}`

DELETE

`http DELETE http://103.89.84.184:8000/customers/<id> { HEADER: { HEADER: authorization:<access_token> } }`

Example

`http DELETE http://103.89.84.184:8000/customers/30 { HEADER: { HEADER: authorization:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjMzODg4NjMsInVzZXJfaWRlbnRpZmllciI6ImRhbmdoaWV1MTcwOUBzYW1wbGUudGVzdCJ9.YRrmTXN9wN-ewL_gA4wblU71NQAdsMk-ony6iLnwRKM} }`

Response

`{}`


