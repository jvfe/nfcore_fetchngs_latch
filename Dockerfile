FROM 812206152185.dkr.ecr.us-west-2.amazonaws.com/latch-base:dd8f-main

RUN apt-get update -y && \
    apt-get install -y curl unzip git

# Install Nextflow
RUN apt-get install -y default-jre-headless
RUN curl -s https://get.nextflow.io | bash && \
    mv nextflow /usr/bin/ && \
    chmod 777 /usr/bin/nextflow &&\
    chmod -R 777 /root/.nextflow/ &&\
    chmod -R 777 /root/.cache/

# Install miniconda
RUN curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    --output miniconda.sh &&\
    bash miniconda.sh -b -p /opt/conda
ENV CONDA_DIR /opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH
RUN conda config --add channels defaults &&\
    conda config --add channels bioconda &&\
    conda config --add channels conda-forge &&\
    conda config --set channel_priority strict &&\
    chmod -R 777 /root/.conda/


# STOP HERE:
# The following lines are needed to ensure your build environement works
# correctly with latch.
RUN python3 -m pip install --upgrade latch
COPY wf /root/wf
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
WORKDIR /root