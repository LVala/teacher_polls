# Teacher Polls
### Web app for conducting polls about college teachers in 5 different categories, collecting this information and presenting the data in the form of pretty graphs
---
Created using **Python**, **Django** and **Matplotlib**.

### **How to setup for development**:
- Make sure you have [Python 3 and pip](https://www.python.org/downloads/) installed (at least 3.10)
- Clone this repository
- Create and activate virtual environment with [venv](https://docs.python.org/3/library/venv.html) (and do everything else inside created environment)
- Install dependencies with ```pip install -r requirements.txt```
- Set timezone in ```teacher_polls/polls_site/polls_site/settings.py```
  ```python
  TIME_ZONE = 'CET'  # by default
  ```
- Migrate Django models
  ```python
  # inside teacher_polls/polls_site directory
  python manage.py migrate
  ```
- Create admin user
  ```python
  # inside teacher_polls/polls_site directory
  python manage.py createsuperuser
  ```
