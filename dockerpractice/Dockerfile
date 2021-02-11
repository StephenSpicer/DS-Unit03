

FROM ubuntu
ENV PYTHONBUFFER=1
RUN apt update && \
    apt upgrade -y && \
    apt install python3 python3-pip curl -y && \
    pip3 install numpy pandas

# FROM ubuntu:18.04
# COPY . /app
# RUN make /app
# CMD python /app/app.py