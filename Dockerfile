# Use the latest Python 3 docker image
#FROM condaforge/mambaforge:latest as base
FROM antsx/antspy:v0.5.2 as base

ENV HOME=/root/
ENV FLYWHEEL="/flywheel/v0"
WORKDIR $FLYWHEEL
RUN mkdir -p $FLYWHEEL/input $FLYWHEEL/output


RUN apt-get update && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN python3 -m pip install --upgrade pip && \
    pip install flywheel-sdk && install flywheeel-gear-toolkit

# Configure entrypoint
RUN bash -c 'chmod +rx $FLYWHEEL/run.py' && \
    bash -c 'chmod +rx $FLYWHEEL/start.sh' && \
    bash -c 'chmod +rx $FLYWHEEL/app/'

# Installing the current project (most likely to change, above layer can be cached)
COPY ./ $CODE/

ENTRYPOINT ["bash","/flywheel/v0/run.py"] 


