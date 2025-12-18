# Calculating the effects of floods

## Unix
```
  python -m venv .venv
  source ./venv/bin/activate
``` 
## Windows
```
    python -m venv .venv
   .venv\Scripts\activate.bat
```
## Install
```
  pip install -r requirements.txt
  pip install uvicorn[standard]
  pip install Jinja2
```
## Launch  
``` 
  uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
