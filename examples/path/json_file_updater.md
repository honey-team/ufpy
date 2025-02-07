# `JsonFileUpdater`

## Introduction

`JsonFileUpdater` is class for simplifying working with JSON dictionaries. Using it you can write json dumped data to:
1. File
2. Stream
3. `io.BytesIO` object

## Create `JsonFileUpdater`

Import it:
```py
from ufpy import JsonFileUpdater
```

Create object and use it in `with`.

If you want to write to file:
```py
with JsonFileUpdater('test.json') as j: ...
```

If you want to write to your stream object:
```py
class TestStream:
    def write(self, something: str): ...
    def read(self) -> str: ...

with JsonFileUpdater(TestStream()) as j: ...
```

If you want to write to `io.BytesIO`:
```py
from io import BytesIO
b = BytesIO()
with JsonFileUpdater(b) as j: ...
```

## Get items

If you want to get item from json dictionary you can use `j` (or any another name) variable how python dictionary.

For example,

`test.json`
```json
{
  "hello": {
    "english": "hello",
    "german": "hallo",
    "russian": "privet"
  },
  "math": {
    "2+2": 4,
    "x^2 = x*x": true
  }
}
```

`main.py`
```py
with JsonFileUpdater('test.json') as j:
    print(j['hello']) # {"english": "hello", "german": "hallo", "russian": "privet"}
    print(j['hello']['russian']) # privet
    print(j['math']['2+2']) # 4
    print(j['math']['x^2 = x*x']) # True
```

Also for items of dictionaries which is in items of json dictionary you can use this format `{key1} / {key2} ...`.

For example:
```py
print(j['hello / russian']) # eq. of j['hello']['russian']
```

## Create or edit items

As with getting items, you can just use `JsonFileUpdater` how python dictionary.
```py
with JsonFileUpdater('test.json') as j:
    j['testing_something'] = 'successfully'
```

How you will get this `test.json` file:
```json
{
  "hello": {
    "english": "hello",
    "german": "hallo",
    "russian": "privet"
  },
  "math": {
    "2+2": 4,
    "x^2 = x*x": true
  },
  "testing_something": "successfully"
}
```

But there is a nuance.
If you want to change item of dictionary which is in main dictionary, you can't just change it this way.
Use `{key1} / {key2} ...` syntax

```py
with JsonFileUpdater('test.json') as j:
    j['hello / french'] = 'bonjour'
```

Now you will get updated json file:
```json
{
  "hello": {
    "english": "hello",
    "german": "hallo",
    "russian": "privet",
    "french": "bonjour"
  },
  "math": {
    "2+2": 4,
    "x^2 = x*x": true
  },
  "testing_something": "successfully"
}
```

