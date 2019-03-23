export ACCESS_TOKEN='xxx'
export ORG='xxx'
export MONGO_USER='xxx'
export MONGO_PASS='xxx'
export GOOGLE_CLOUD_KEYFILE_JSON='xxx'
export GOOGLE_APPLICATION_CREDENTIALS='xxx'

# Terraform
export TF_VAR_ACCESS_TOKEN='xxx'
export TF_VAR_ORG='xxx'
export TF_VAR_UN='xxx'
export TF_VAR_PW='xxx'

echo 'Access token initialized: '$ACCESS_TOKEN
echo 'Organization set to:' $ORG
echo 'GCP Credentials set to:' $GOOGLE_APPLICATION_CREDENTIALS
echo 'GCP APP Credentials set to:' $GOOGLE_APPLICATION_CREDENTIALS

export FLASK_APP=main.py
export FLASK_ENV=production
.venv/bin/python3.7 -m flask run