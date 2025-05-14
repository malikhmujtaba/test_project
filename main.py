import subprocess
import datetime
import random
from datetime import date, timedelta
import pdb
import os
# Define the path to the file you want to edit
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = f'./utils/console.py'
messages = ["Updated main.py", "Added print", "print hello added"]
# breakpoint() #for debugger
start_date = date(2024, 1, 1)
end_date = date(2024, 2, 28)
delta = timedelta(days=1)
count = 0
days = 0
while start_date <= end_date:
  days += 1
  if start_date.weekday() < 5:
    i = 0
    while i < random.randint(0, 25):
      count += 1
      # Open the file and make your edits
      with open(file_path, "a") as f:
        f.write("\n print('hello')")
      # # Set the commit date to a past date
      # Change this to the date you want
      past_date = datetime.datetime(
          start_date.year, start_date.month, start_date.day, 12, 0, 0)
      env = {"GIT_COMMITTER_DATE": past_date.strftime("%s %z")}
      # # Use Git to add and commit the changes to the file with past date
      subprocess.call(["git", "add", file_path])
      subprocess.call(["git", "commit", "--date", past_date.strftime("%c %z"),
                      "-m", random.sample(messages, 1)[0]], env=env)
      i += 1
  start_date += delta
  if days == 15:
    subprocess.call(["git", "push", "origin", "main"])
    days = 0
print(count, 'count')
# subprocess.call(["git", "push", "origin", "main"])
