# nn-hero-zero-solutions

Working through Andrej Karpathy's [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html).

## Chapters

- micrograd
- [makemore1](./makemore1.ipynb)

Author's notebooks from video lectures are available [here](https://github.com/karpathy/nn-zero-to-hero).

## Run

Extended [`scipy-notebook`](https://hub.docker.com/r/jupyter/scipy-notebook/) image is used [with additional `pytorch` package](./Dockerfile).

To build and run:

```sh
docker build -t pytorch-notebook:latest

docker run --rm -it -p 8888:8888 -v <this_folder>:/home/jovyan pytorch-notebook:latest
```
