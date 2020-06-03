# Email Checker
A web service that accepts http requests and returns responses based on the following problem statement.

It accepts a list of email addresses and returns an integer indicating the number of unique email addresses. 

"Unique" email addresses means they will be delivered to the same account using Gmail account matching. Specifically: Gmail will ignore the placement of "." in the username, and it will ignore any portion of the username after a "+".

## Examples:

test.email@gmail.com, test.email+spam@gmail.com and testemail@gmail.com will all go to the same address, and thus the result should be 1.

## Build and Run
In the project directory, 
```
$ docker-compose up
```
runs the app in the development mode.
Open http://localhost:5000/ to view it in the browser.

## Usage

You can add email addresses in the following formats:
```
{"email":"test.email@gmail.com"}
```

```
[
    {"email":"test.email@gmail.com"},
    {"email":"test.email+spam@gmail.com"}
]
```

```
{
    "email":[
        "test.email@gmail.com", 
        "test.email+spam@gmail.com"
    ]
}
```
To add a list of emails, 
```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"email":"test.email@gmail.com"}' http://localhost:5000/api/v1/emails

host:5000/api/v1/emails
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 42
Server: Werkzeug/1.0.0 Python/3.7.7
Date: Sun, 29 Mar 2020 05:57:36 GMT

[{"email":"test.email@gmail.com","id":1}]
```
```
$ curl -i -H "Content-Type: application/json" -X POST -d '[{"email":"test.email@gmail.com"},{"email":"test.email+spam@gmail.com"}]' http://localhost:5000/api/v1/emails

HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 127
Server: Werkzeug/1.0.0 Python/3.7.7
Date: Sun, 29 Mar 2020 05:58:18 GMT

[{"email":"test.email@gmail.com","id":1},{"email":"test.email@gmail.com","id":2},{"email":"test.email+spam@gmail.com","id":3}]
```

```
$ curl -i -H "Content-Type: application/json" -X POST -d '{"email":["test.email@gmail.com", "test.email+spam@gmail.com"]}' http://localhost:5000/api/v1/emails

HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 212
Server: Werkzeug/1.0.0 Python/3.7.7
Date: Sun, 29 Mar 2020 05:58:53 GMT

[{"email":"test.email@gmail.com","id":1},{"email":"test.email@gmail.com","id":2},{"email":"test.email+spam@gmail.com","id":3},{"email":"test.email@gmail.com","id":4},{"email":"test.email+spam@gmail.com","id":5}]
```

To see the number of unique email addresses, go to http://localhost:5000/api/v1/emails/unique.

Alternatively, you can do 
```
$ curl -i http://localhost:5000/api/v1/emails/unique

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 55
Server: Werkzeug/1.0.0 Python/3.7.7
Date: Sun, 29 Mar 2020 05:59:47 GMT

{"result":"1","unique emails":["testemail@gmail.com"]}
```

To view all the email addresses, go to http://localhost:5000/api/v1/emails.

Alternatively, you can do 
```
$ curl -i http://localhost:5000/api/v1/emails

HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 212
Server: Werkzeug/1.0.0 Python/3.7.7
Date: Sun, 29 Mar 2020 06:00:14 GMT

[{"email":"test.email@gmail.com","id":1},{"email":"test.email@gmail.com","id":2},{"email":"test.email+spam@gmail.com","id":3},{"email":"test.email@gmail.com","id":4},{"email":"test.email+spam@gmail.com","id":5}]

```

<!-- ```
docker ps -a
docker rm CONTAINER_ID
docker image ls -a
docker rmi IMAGE_ID
``` -->