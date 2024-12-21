#!/bin/sh

if [ -f /app/env/service-account-file.json ]; then
  export SERVICE_ACCOUNT_FILE_CONTENT="$(cat /app/env/service-account-file.json)"
fi

exec "$@"