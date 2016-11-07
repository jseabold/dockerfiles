FROM continuumio/miniconda3:4.1.11

# psmisc contains pstree
RUN apt-get update && apt-get install -y psmisc
RUN conda update -y conda && \
    conda install -y -c conda-forge -c defaults --show-channel-urls --override-channels \
    conda-build

COPY requirements.txt /bootstrap/requirements.txt
RUN conda install -y -c conda-forge -c defaults --file \
    /bootstrap/requirements.txt && \
    conda install -c damianavila82 rise && \
    conda clean -tipsy
RUN pip install --user graphviz
RUN jupyter nbextension enable --py widgetsnbextension && \ 
    jupyter nbextension install --py rise && \
    jupyter nbextension enable --py rise
EXPOSE 8888
