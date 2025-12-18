# Calculating the effects of floods

# unix
  ## python -m venv .venv
  ## source ./venv/bin/activate
# windows
    python -m venv .venv
   ./venv\Scripts\activate.bat
##Install
  pip install -r requirements.txt
  uvicorn main:app --host=0.0.0.0 --post=8000 --reload
