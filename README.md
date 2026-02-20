# fastapi_test

For start program local run on http://localhost:8000/:
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

Endpoint `/list_items`
```
request:
/list_items?items=1&items=2&items=3&q=hello

response:
{"items_len":3,"q":"hello"}
```
