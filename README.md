# nn-hero-zero-solutions

Working through Andrej Karpathy's [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html).

## Lessons

### 1. micrograd

Solution: [micrograd.ipynb](./micrograd.ipynb)

Links:

- [micrograd repo](https://github.com/karpathy/micrograd)
- [Jupyter notebooks](https://github.com/karpathy/nn-zero-to-hero/tree/master/lectures/micrograd)

#### Exercises:

- [x] Complete the [following Google Collab notebook](https://colab.research.google.com/drive/1FPTx1RXtBfc4MaTkf7viZZD4U2F9gtKN?usp=sharing). [My solution](./micrograd_exercises.ipynb).

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

### 4. makemore 3: Activations & Gradients, BatchNorm

[Notebook](./makemore3.ipynb)

Links:

- [YouTube](https://www.youtube.com/watch?v=P6sfmUTpUmc)
- [Jupyter notebook](https://github.com/karpathy/nn-zero-to-hero/blob/master/lectures/makemore/makemore_part3_bn.ipynb)
- [collab notebook](https://colab.research.google.com/drive/1H5CSy-OnisagUgDUXhHwo1ng2pjKHYSN)

Useful links:

- ["Kaiming init" paper](https://arxiv.org/abs/1502.01852)
- [BatchNorm paper](https://arxiv.org/abs/1502.03167)
- [Good paper](https://arxiv.org/abs/2105.07576) illustrating some of the problems with batchnorm in practice

Exercises:

- [ ] E01: I did not get around to seeing what happens when you initialize all weights and biases to zero. Try this and train the neural net. You might think either that 1) the network trains just fine or 2) the network doesn't train at all, but actually it is 3) the network trains but only partially, and achieves a pretty bad final performance. Inspect the gradients and activations to figure out what is happening and why the network is only partially training, and what part is being trained exactly.
- [ ] E02: BatchNorm, unlike other normalization layers like LayerNorm/GroupNorm etc. has the big advantage that after training, the batchnorm gamma/beta can be "folded into" the weights of the preceeding Linear layers, effectively erasing the need to forward it at test time. Set up a small 3-layer MLP with batchnorms, train the network, then "fold" the batchnorm gamma/beta into the preceeding Linear layer's W,b by creating a new W2, b2 and erasing the batch norm. Verify that this gives the same forward pass during inference. i.e. we see that the batchnorm is there just for stabilizing the training, and can be thrown out after training is done! pretty cool.

## Run

Extended [`scipy-notebook`](https://hub.docker.com/r/jupyter/scipy-notebook/) image is used [with additional `pytorch` package](./Dockerfile).

To build and run:

```sh
docker build -t pytorch-notebook:latest

docker run --rm -it -p 8888:8888 -v <this_folder>:/home/jovyan pytorch-notebook:latest

# or

./start.sh
```
