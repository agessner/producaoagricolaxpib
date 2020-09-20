#!/bin/bash


python -u main.py & ./cloud_sql_proxy --dir=$DB_SOCKET_DIR --instances=$INSTANCE_CONNECTION_NAME --credential_file=$GOOGLE_APPLICATION_CREDENTIALS
