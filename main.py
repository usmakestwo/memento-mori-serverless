import os
from github import Github
from template.template_builder import TemplateBuilder

# First create a Github instance
g = Github(os.environ["ACCESS_TOKEN"])
org = os.environ["ORG"]

# Get Org
organization = g.get_organization(org)

def createRepo(name="Sample", description="Learning A new skill"):
  github_name = name.replace(" ", "-").lower()
  print('Creating project ' + github_name)
  repo = organization.create_repo(
    name=github_name,
    allow_rebase_merge=True,
    auto_init=False,
    description=':school_satchel: ' + description,
    has_issues=True,
    has_projects=True,
    has_wiki=True,
    private=False,
  )
  
  repo = g.get_repo(org + "/" + name.replace(" ", "-"))
  commit_message = "chore :robot: automated init"
  
  repo.create_file("README.md", commit_message, TemplateBuilder().init_readme(name), branch="master")
  repo.create_file("resources/README.md", commit_message, TemplateBuilder().init_resource_readme(name), branch="master")
  repo.create_file("courses/README.md", commit_message, TemplateBuilder().init_courses_readme(name), branch="master")
  repo.create_file("praxi.yaml", commit_message, TemplateBuilder().init_praxi(github_name, name, description), branch="master")

# Create Repo

list_of_things = [
  {"name": "Learning French", "description": "Learning basic conversational french"},
  {"name": "Learning MySQL", "description": "Learning SQL best practices"},
  {"name": "Learning Statistics", "description": "Learning statistics"},
  {"name": "Learning next.js", "description": "Learning next.js"},
  {"name": "Learning Contentful", "description": "Learning how to use Contentful with ReactJS"},
  {"name": "Learning Cooking", "description": "Learning how to cook"},
  {"name": "Learning GCP", "description": "Learning how to use GCP and Terraform for analytics"},
  {"name": "Learning Python", "description": "Learning Python"},
  {"name": "Learning GraphQL", "description": "Learning GraphQL"},
  {"name": "Learning C Sharp", "description": "Learning C# for gaming and mobile development"},
  {"name": "Learning Game Dev", "description": "Learning game development with Unity"},
  {"name": "Learning to Play the Piano", "description": "Learning how to play the piano"},
  {"name": "Learning algebra", "description": "Learning alegrabra for statistics"},
  {"name": "Learning algorithms", "description": "Learning common algorithm and how to design one"},
  {"name": "Learning fitness", "description": "Tips and tools for a healthier body and nutrition"},
  {"name": "Learning hacking", "description": "Learning ethical hacking"},
  {"name": "Learning bash", "description": "Learning bash to automate everyday tasks"}
]

# Create all projects
for item in list_of_things:
  createRepo(item['name'], item['description'])
