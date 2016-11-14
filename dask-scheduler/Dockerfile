FROM continuumio/miniconda3:4.1.11

RUN conda update -y conda && \
    conda install -q -y -c conda-forge -c defaults --show-channel-urls --override-channels \
    conda-build \
    dask=0.11.1 && \
    conda clean -tipsy
