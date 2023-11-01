# Research Computing Public Documentation Builder Container

This builder container is to make the HTML version of the Research Computing's RTD without having to construct a virtual environment to installing the required python 
libraries. To use it, you will need to have Docker or Podman installed and run the following commands:  

```bash
cd rc-public-documentation/
docker/podman build --platform=linux/x86_64 -t rtd-builder:latest -f container/Dockerfile .
docker/podman run --rm --platform=linux/x86_64 -v $PWD:/rtd -it rtd-builder:latest
```
