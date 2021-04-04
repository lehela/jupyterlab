FROM python:3.9 AS base

LABEL created_by=https://github.com/lehela/jupyter-notebooks.git

ARG wheels=https://github.com/lehela/jupyterlab/raw/main/wheels

# Install base OS dependencies
RUN apt-get update && apt-get install -yq --no-install-recommends \
    build-essential \
    vim-tiny \
    htop \
    glances \
    git \   
    tzdata \
    unzip \
    wget \
    bzip2 \
    ca-certificates \
    locales \
    pandoc \
    python-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen

# Install other OS dependencies
# https://github.com/jupyter/docker-stacks/blob/master/minimal-notebook/Dockerfile
# RUN apt-get update && apt-get install -yq --no-install-recommends \
    # inkscape \
    # jed \
    # libsm6 \
    # libxext-dev \
    # libxrender1 \
    # lmodern \
    # netcat \
    # texlive-fonts-extra \
    # texlive-fonts-recommended \
    # texlive-generic-recommended \
    # texlive-latex-base \
    # texlive-latex-extra \
    # texlive-xetex \
    # libblas-dev \
    # liblapack-dev \ 
    # && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install --disable-pip-version-check \
    $wheels/numpy-1.20.2-cp39-cp39-manylinux2014_aarch64.whl \
    $wheels/pandas-1.2.3-cp39-cp39-linux_aarch64.whl \
    $wheels/bokeh-2.3.0-py3-none-any.whl \
    $wheels/matplotlib-3.4.1-cp39-cp39-manylinux2014_aarch64.whl \
    $wheels/seaborn-0.11.1-py3-none-any.whl \
    --upgrade jupyterlab \
    && rm -rf /tmp/pip-tmp


# Install more packages if needed (taken from jupyter/scipy-notebook)

# RUN pip3 install --disable-pip-version-check \
#     beautifulsoup4 \
#     bottleneck \
#     cloudpickle \
#     cython \
#     dask \
#     dill \
#     h5py \
#     ipywidgets \
#     ipympl \
#     numba \
#     numexpr \
#     patsy \
#     protobuf \
#     tables \
#     scikit-image \
#     scikit-learn \
#     scipy \
#     sqlalchemy \
#     statsmodels \
#     sympy \
#     vincent \
#     widgetsnbextension\
#     xlrd 

COPY scripts/*.sh /usr/bin/

RUN chmod 755 /usr/bin/*.sh \ 
    && build_script.sh 

WORKDIR /root

EXPOSE 8888

ENTRYPOINT [ "start_jupyterlab.sh" ]

