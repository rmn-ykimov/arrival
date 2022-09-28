# Dockerfile to build switcher container images
# Based on Alpine
FROM python:3.10-alpine3.16
LABEL maintainer="rmn-ykimov"
RUN apk update && apk upgrade
CMD ["python", "./switcher.py"]