import os
from github import Github
from flask import Flask, Response
from utils.template_builder import TemplateBuilder
from utils.connect_db import Datastore

# First create a Github instance
g = Github(os.environ["ACCESS_TOKEN"])
org = os.environ["ORG"]

# Get Org
organization = g.get_organization(org)

# Database
db = Datastore()

# Initialize Flask
app = Flask(__name__)

@app.route("/health")
def health():
  return 'OK'

@app.route("/api/projects")
def fetchProjects():
  projects = db.return_all_records()
  return Response(projects, status=200, mimetype='application/json')

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

  db.insert_record(name, description)

# Create all projects

#createRepo('test', 'test description')
