# fastapi_test

For start program local run:
```sh
  uvicorn main:app --reload
```

Endpoint `/`
```
request:
/

response:
{"message": "Hello, World!"}
```


Endpoint `/items/{item_id}`
```
request:
/items/100?q=hello

response:
{"item_id":100,"q":"hello"}
```
