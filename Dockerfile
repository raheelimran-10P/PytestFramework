##################################
### Set the Pytest environment ###
##################################
FROM python:3.10-alpine

# Set the working directory
RUN mkdir /PytestFramework/
ADD . /PytestFramework/
WORKDIR /PytestFramework/

# Copy the folder with the tests into the container
ENV PIP_ROOT_USER_ACTION=ignore
RUN python3 -m venv PytestFrameworkEnv
RUN source PytestFrameworkEnv/bin/activate

## Copy the waiter
#COPY --from=curl wait-for-it.sh wait-for-it.sh
#RUN chmod +x wait-for-it.sh
#RUN apk add bash

# Install all dependencies
RUN pip install -r requirements.txt
#RUN pip install --default-timeout=1000 --no-cache-dir --upgrade -r requirements.txt

# This Dockerfile hasn't got any CMD or ENTRYPOINT so it doesn't do anything by its own.
# Check docker-compose.yml to see an implementation of the image

# docker run -ti pytest-framework_container:1.0 /bin/sh
# docker build -t pytest-framework_container:1.0 .