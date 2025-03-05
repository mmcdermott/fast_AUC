# Faster AUC
[![python](https://img.shields.io/badge/-Python_3.10-blue?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Documentation Status](https://readthedocs.org/projects/fast-AUC/badge/?version=latest)](https://fast-AUC.readthedocs.io/en/latest/?badge=latest)
[![tests](https://github.com/mmcdermot/fast_AUC/actions/workflows/tests.yaml/badge.svg)](https://github.com/mmcdermot/fast_AUC/actions/workflows/tests.yaml)
[![codecov](https://codecov.io/gh/mmcdermot/fast_AUC/branch/main/graph/badge.svg?token=F9NYFEN5FX)](https://codecov.io/gh/mmcdermot/fast_AUC)
[![code-quality](https://github.com/mmcdermot/fast_AUC/actions/workflows/code-quality-main.yaml/badge.svg)](https://github.com/mmcdermot/fast_AUC/actions/workflows/code-quality-main.yaml)
[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/mmcdermot/fast_AUC#license)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/mmcdermot/fast_AUC/pulls)
[![contributors](https://img.shields.io/github/contributors/mmcdermot/fast_AUC.svg)](https://github.com/mmcdermot/fast_AUC/graphs/contributors)

A package for computing fast AUROC scores in python. This library is almost certainly not useful. Please see
the options [in this ChatGPT conversation](https://chatgpt.com/share/67c8865b-3f50-800c-9784-b6df935451d7) for
likely better options.

This package uses the probabilistic definition of AUC to provide a simple $O(n \log n)$ time complexity
algorithm to compute it that seems in practice to be faster than `sklearn.metrics.roc_auc_score`.

## Installation
First, download the repo. Then use

```bash
pip install -e .
```

## Usage
```python
from fast_AUC import auroc

...
auroc(y_true, y_score)
```
