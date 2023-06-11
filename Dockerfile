FROM jupyter/scipy-notebook:lab-3.6.2
USER root
# RUN apt-get update && apt-get install -y graphviz && rm -rf /var/lib/apt/lists/*
RUN apt-get update --yes && apt-get install --yes --no-install-recommends graphviz && apt-get clean && rm -rf /var/lib/apt/lists/*
USER ${NB_UID}
RUN pip install --no-cache-dir torch graphviz
