from datetime import datetime
from pathlib import Path
from testrail_api import TestRailAPI

def main():
  api = TestRailAPI('https://example.testrail.com/', 'example@mail.com', 'password')

  new_milestone = api.milestones.add_milestone(
    project_id=1,
    name='New milestone',
    start_on=int(datetime.now().timestamp())
  )
  pass

if __name__ == "__main__":
  main()
