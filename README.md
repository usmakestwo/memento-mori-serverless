# Github Project Creation

An application to automate project creation on Github


## Architecture

![Memento Mori Universitas](https://user-images.githubusercontent.com/1566236/55802093-82148f80-5aa5-11e9-9002-f30c169b6fbf.png)

## Install/Run Python Application - Locally

1. Activate shell `pipenv shell`

2. Install dependencies `pipenv install`

3. Populate *ACCESS_TOKEN* and *ORG* and *GCP Credentials *in init.sh and run exporting the variables

  `source ./config/init.sh`

4. Run application `python main.py`

## Run infrastructure - Cloud Functions

1. Run `source ./config/init.sh`

2. Run `terraform install`

3. Deploy infrastructure `terraform apply`

4. The following services will be available

#### Fetch records

`GET https://us-east1-memento-mori-universitas.cloudfunctions.net/gcp-read-courses-cf`

#### Save records

```
POST https://us-east1-memento-mori-universitas.cloudfunctions.net/gcp-write-courses-cf -d '{"name": "Learning Something", "description": "What or why are we learning this"}'
```
