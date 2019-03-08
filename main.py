import os
from github import Github

# First create a Github instance:
g = Github(os.environ['ACCESS_TOKEN'])

# Get user
user = g.get_user()

def createEmptyRepo(name='sample_repo', description='some description'):
  # Create empty repo
  repo = user.create_repo(
    name,
    allow_rebase_merge=True,
    auto_init=False,
    description=description,
    has_issues=True,
    has_projects=True,
    has_wiki=False,
    private=True,
  )
  print(repo)
  repo = g.get_repo('gonzalovazquez/sample_repo')
  text = """
  # Sample Repo

  Lets see if this works, it it does, that is very cool!

  This is a code:

  `var a = {}`

  And this is a *Bold*.

  """
  repo.create_file("README.md", "ci(scaffold): add Readme.md", text, branch="master")
  repo.create_file("resources/README.md", "ci(scaffold): automated", "test", branch="master")

# Create Empty Repo
createEmptyRepo()