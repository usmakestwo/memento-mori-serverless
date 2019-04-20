import os
from github import Github
from utils.template_builder import TemplateBuilder

class GithubClient():
  def __init__(self):
    # First create a Github instance
    self.git = Github(os.environ["ACCESS_TOKEN"])
    self.org = os.environ["ORG"]
    # Get Org
    self.organization = self.git.get_organization(self.org)

  def createRepo(self, name="Sample", description="Learning A new skill"):
    github_name = name.replace(" ", "-").lower()
    github_path = self.org + "/" + name.replace(" ", "-")
    print('Creating project ' + github_name)
    try:
      repo = self.organization.create_repo(
        name=github_name,
        allow_rebase_merge=True,
        auto_init=False,
        description=':school_satchel: ' + description,
        has_issues=True,
        has_projects=True,
        has_wiki=True,
        private=False,
      )
      repo = self.git.get_repo(github_path)
      commit_message = "chore :robot: automated init"
      print(github_path)
      repo.create_file("README.md", commit_message, TemplateBuilder().init_readme(name), branch="master")
      repo.create_file("resources/README.md", commit_message, TemplateBuilder().init_resource_readme(name), branch="master")
      repo.create_file("courses/README.md", commit_message, TemplateBuilder().init_courses_readme(name), branch="master")
      repo.create_file("praxi.yaml", commit_message, TemplateBuilder().init_praxi(github_name, name, description), branch="master")
      return github_path
    except Exception as e:
      print(e)
