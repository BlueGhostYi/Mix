The folder provides the training logs of SimGCL on four datasets. The suffix_1 indicates that `torch.unique` was used, while the suffix _2 indicates that `torch.unique` was not used.

**Hyperparameter settings:**
- Douban-Book:
```
ssl_lambda = 0.2
temperature = 0.2
epsilon = 0.2
```
- Amazon-Book:
```
ssl_lambda = 2.0
temperature = 0.2
epsilon = 0.1
```
- Yelp:
```
ssl_lambda = 0.5
temperature = 0.2
epsilon = 0.05
```
- Tmall:
```
ssl_lambda = 0.1
temperature = 0.2
epsilon = 0.1
```
