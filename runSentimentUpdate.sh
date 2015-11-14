#!/bin/bash
. venv/bin/activate

MONGOURL="mongodb://localhost:27017/"

./requirements.sh

python sentiment_update.py

deactivate
