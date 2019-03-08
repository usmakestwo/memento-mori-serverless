import os
from github import Github

# First create a Github instance:
g = Github(os.environ['ACCESS_TOKEN'])
org = os.environ['ORG']

# Get Org
organization = g.get_organization(org)

def createRepo(name='sample_repo', description=':school_satchel: Learning French'):
  repo = organization.create_repo(
    name,
    allow_rebase_merge=True,
    auto_init=False,
    description=description,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    private=False,
  )
  print(repo)
  repo = g.get_repo(org + '/sample_repo')
  text = """
  # Sample Repo

  Lets see if this works, it it does, that is very cool!

  This is a code:

  `var a = {}`

  And this is a *Bold*.

  """
  repo.create_file("README.md", "ci: :robot: automated init", text, branch="master")
  repo.create_file("resources/README.md", "ci: :robot: automated init", "test", branch="master")
  repo.create_file("courses/README.md", "ci: :robot: automated init", "test", branch="master")

# Create Repo
createRepo()