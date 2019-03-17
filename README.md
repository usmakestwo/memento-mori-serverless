# Github Project Creation

A script to automate project creation on Github

## Install/Run Python Application

1. Activate shell `pipenv shell`

2. Install dependencies `pipenv install`

3. Populate *ACCESS_TOKEN* and *ORG* and *GCP Credentials *in init.sh and run exporting the variables

  `source ./config/init.sh`

4. Run application `python main.py`

## Install infrastructure

1. Run `terraform install`

2. Deploy infrastructure `terraform apply`