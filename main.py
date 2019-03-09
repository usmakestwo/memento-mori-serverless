import os
from github import Github
from template.template_builder import TemplateBuilder

# First create a Github instance:
g = Github(os.environ["ACCESS_TOKEN"])
org = os.environ["ORG"]

# Get Org
organization = g.get_organization(org)

def createRepo(name="Sample", description=":school_satchel: Learning Something New"):
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
  repo = g.get_repo(org + "/" + name)
  commit_message = "chore :robot: automated init"
  
  repo.create_file("README.md", commit_message, TemplateBuilder().init_readme(name), branch="master")
  repo.create_file("resources/README.md", commit_message, TemplateBuilder().init_resource_readme(name), branch="master")
  repo.create_file("courses/README.md", commit_message, TemplateBuilder().init_courses_readme(name), branch="master")
  repo.create_file(".school.yml", commit_message, "test", branch="master")

# Create Repo
createRepo()