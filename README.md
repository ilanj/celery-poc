<h2> celery </h2>

<h6> pre requisites </h6>

 *  pip install -r requirememnts.txt
 *  sudo sh sys_requirements.sh

<h6> steps </h6>

* run app.py
* run "celery -A task worker --pool=solo --loglevel=info" from terminal
* hit `http://localhost:5000/`


