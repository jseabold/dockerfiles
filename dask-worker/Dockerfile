FROM continuumio/miniconda3:4.1.11

RUN conda update -y conda && \
    conda install -y -q -c conda-forge -c defaults --show-channel-urls --override-channels \
    conda-build \
    dask=0.11.1 && \
    conda clean -tipsy

COPY requirements.txt /bootstrap/requirements.txt

RUN conda install -y -q -c conda-forge -c defaults --file \
    /bootstrap/requirements.txt && \
    conda clean -tipsy
