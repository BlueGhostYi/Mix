# MixRec

## Environment
```
python == 3.8.18
pytorch == 2.1.0 (cuda:12.1)
scipy == 1.10.1
numpy == 1.24.3
```

## Examples to run the codes
We adopt three widely used large-scale recommendation datasets: Douban-Book, Yelp, Tmall, and Amazon-Book. Most of MixRec's hyperparameters can be kept at their default values, the only one that needs to be adjusted is the weight of contrastive losses `ssl_lambda`.

Steps to run the code:
1. In the folder . /configure to configure the MixRec.txt file
2. Set the MixRec according to the following optimal parameters:

- Douban-Book:
```
dataset = douban-book
ssl_lambda = 0.1
```
- Amazon-Book:
```
dataset = amazon-book
ssl_lambda = 1.1
```
- Yelp:
```
dataset = yelp
ssl_lambda = 0.3
```
- Tmall:
```
dataset = tmall
ssl_lambda = 0.6
```

3. Run main.py.
