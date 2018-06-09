FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    python3-dev \
    python3-pip \
    python3-wheel \
    python3-setuptools \
    python3-tk && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN pip3 install -U pip
RUN pip3 install Cython
RUN pip3 install numpy
# RUN pip3 install tensorflow-gpu keras scikit-image scipy Pillow h5py scikit-learn joblib ipython jupyter
RUN pip3 install scikit-image scipy Pillow h5py joblib ipython jupyter
RUN pip3 install RISE
RUN jupyter-nbextension install rise --py --sys-prefix
RUN jupyter-nbextension enable rise --py --sys-prefix

ENV USER root
