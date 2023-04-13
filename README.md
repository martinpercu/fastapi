# 1 Start

Here will start

```sh
python3 -m venv env
source/env/activate
pip3 install fastapi
pip3 install uvicorn
```


# 2 test working

Create a main.py file in root.

```sh
uvicorn main:app --reload
```
At this point in localhost:8000 we must get the return message

- To change to port 4800.... 
```sh
uvicorn main:app --reload --port 4800
```

- To see the app on net .... 
```sh
uvicorn main:app --reload --port 4800 --host 
```


# Start 3

```sh
etcetc
```

