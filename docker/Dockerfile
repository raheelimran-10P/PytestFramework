FROM python:3.9-alpine

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

# upgrade pip
RUN pip install --upgrade pip

# Set the working directory
RUN mkdir /PytestFramework/
ADD .. /PytestFramework/
WORKDIR /PytestFramework/

# Set up virual env
RUN python3 -m venv PytestFrameworkEnv
RUN source PytestFrameworkEnv/bin/activate

# Install all dependencies
RUN pip install -r docker/requirements.txt

# This Dockerfile hasn't got any CMD or ENTRYPOINT so it doesn't do anything by its own.
# Check docker-compose.yml to see an implementation of the image

# ENTRYPOINT /bin/sh --privileged=true

# docker run -ti pytest-framework_container:1.0 /bin/sh --privileged=true
# docker build -f docker/Dockerfile -t pytest-framework_container:1.0 .