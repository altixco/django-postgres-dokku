#!/bin/sh

env=${ENVIRONMENT:-"development"}
if [ $env = "production" ]; then
  npm run build
else
  npm run dev
fi
