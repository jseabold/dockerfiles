FROM jseabold/miniconda3:latest

RUN apt-get update && \
    apt-get install -y unzip gcc

RUN conda install -c conda-forge -c defaults --override-channels \
    cython \
    numpy \
    requests \
    scipy>=0.17.0

ADD https://github.com/lyst/lightfm/archive/master.zip /home/
RUN cd /home/ && \
    unzip master.zip && \
    mv lightfm-master lightfm
WORKDIR /home/lightfm
RUN pip install .
