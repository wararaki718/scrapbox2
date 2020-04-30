FROM python:3.8

RUN apt update && \
    cd /tmp && \
    wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB && \
    apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB && \
    rm GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB && \
    apt update

RUN sh -c 'echo deb https://apt.repos.intel.com/mkl all main > /etc/apt/sources.list.d/intel-mkl.list' && \
    apt update && \
    apt install intel-mkl-2020.0-088 -y

COPY pip.config /root/.config/pip/pip.config
COPY .numpy-site.cfg /root/.numpy-site.cfg
COPY requirements.txt /tmp/requirements.txt
COPY show_config.py /app/show_config.py

RUN pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

WORKDIR /app

CMD ["python", "show_config.py"]
