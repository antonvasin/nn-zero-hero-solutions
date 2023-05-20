# nn-hero-zero-solutions

Working through Andrej Karpathy's [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html).

## Lessons

### 1. micrograd

### 2. makemore 1: bigram model

Solution: [makemore1.ipynb](./makemore1.ipynb).

Links:

- [Jupyter notebook](https://github.com/karpathy/nn-zero-to-hero/blob/master/lectures/makemore/makemore_part1_bigrams.ipynb)
- Python + Numpy tutorial from [CS231n](https://cs231n.github.io/python-numpy-tutorial/). We use `torch.tensor` instead of `numpy.array` in this video. Their design (e.g. broadcasting, data types, etc.) is so similar that practicing one is basically practicing the other, just be careful with some of the APIs - how various functions are named, what arguments they take, etc. - these details can vary.
- PyTorch [tutorial on Tensor](https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)
- Another [PyTorch intro to Tensor](https://pytorch.org/tutorials/beginner/nlp/pytorch_tutorial.html)

#### Exercises

[Solution](./makemore1_exercises.ipynb)

- [x] Read about [Broadcasting Semantics](https://pytorch.org/docs/stable/notes/broadcasting.html)
- [x] E01: train a trigram language model, i.e. take two characters as an input to predict the 3rd one. Feel free to use either counting or a neural net. Evaluate the loss; Did it improve over a bigram model?
- [ ] E02: split up the dataset randomly into 80% train set, 10% dev set, 10% test set. Train the bigram and trigram models only on the training set. Evaluate them on dev and test splits. What can you see?
- [ ] E03: use the dev set to tune the strength of smoothing (or regularization) for the trigram model - i.e. try many possibilities and see which one works best based on the dev set loss. What patterns can you see in the train and dev set loss as you tune this strength? Take the best setting of the smoothing and evaluate on the test set once and at the end. How good of a loss do you achieve?
- [ ] E04: we saw that our 1-hot vectors merely select a row of W, so producing these vectors explicitly feels wasteful. Can you delete our use of F.one_hot in favor of simply indexing into rows of W?
- [ ] E05: look up and use F.cross_entropy instead. You should achieve the same result. Can you think of why we'd prefer to use F.cross_entropy instead?
- [ ] E06: meta-exercise! Think of a fun/interesting exercise and complete it.

### 3. makemore 2: MLP

[Notebook](./makemore2.ipynb)

Links:

- [YouTube lecture](https://www.youtube.com/watch?v=TCH_1BHY58I)
- [Jupyter notebook](https://github.com/karpathy/nn-zero-to-hero/blob/master/lectures/makemore/makemore_part2_mlp.ipynb)
- [Bengio et al, 2003 MLP Paper](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf)
- [PyTorch internals ref](http://blog.ezyang.com/2019/05/pytorch-internals/)
- [Google Collab notebook](https://colab.research.google.com/drive/1YIfmkftLrz6MPTOO9Vwqrop2Q5llHIGK?usp=sharing)

#### Exercises

- [x] E01: Tune the hyperparameters of the training to beat my best validation loss of 2.2
- [ ] E02: I was not careful with the intialization of the network in this video.
  - 1. What is the loss you'd get if the predicted probabilities at initialization were perfectly uniform? What loss do we achieve?
  - 2. Can you tune the initialization to get a starting loss that is much more similar to (1)?
- [ ] E03: Read the Bengio et al 2003 paper (link above), implement and try any idea from the paper. Did it work?

## Run

Extended [`scipy-notebook`](https://hub.docker.com/r/jupyter/scipy-notebook/) image is used [with additional `pytorch` package](./Dockerfile).

To build and run:

```sh
docker build -t pytorch-notebook:latest

docker run --rm -it -p 8888:8888 -v <this_folder>:/home/jovyan pytorch-notebook:latest

# or

./start.sh
```
