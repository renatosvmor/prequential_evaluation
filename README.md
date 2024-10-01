This repository provides a sample script that can be used in experiments with online learning.

The file **prequential_evaluation.py** includes the function **prequential_learning**, which, given an input dataset, performs online training using the prequential approach (also known as interleaved test-then-train).

This training pipeline has been used in the following papers:

- **Silva, R. M., Pires, P. R., & Almeida, T. A. (2023)**. *Incremental learning for fake news detection*. Journal of Information and Data Management, 13(6). [https://doi.org/10.5753/jidm.2022.2542](https://doi.org/10.5753/jidm.2022.2542)

- **Silva, R. M., & Almeida, T. A. (2021)**. How concept drift can impair the classification of fake news. In *Proceedings of the 9th Symposium on Knowledge Discovery, Mining and Learning (KDMiLe'21)* (pp. 1–8). Brazilian Computing Society. [https://doi.org/10.5753/kdmile.2021.17469](https://doi.org/10.5753/kdmile.2021.17469)

- **Bittencourt, M. M., Silva, R. M., & Almeida, T. A. (2020)**. *ML-MDLText: An efficient and lightweight multilabel text classifier with incremental learning*. Applied Soft Computing, 96, 106699. [https://doi.org/10.1016/j.asoc.2020.106699](https://doi.org/10.1016/j.asoc.2020.106699)


The BibTeX entries for these papers are provided below.

```
@article{silva-jdim:2023_incrementalFakeNews, 
  title={Incremental Learning for Fake News Detection}, 
  volume={13}, 
  url={https://sol.sbc.org.br/journals/index.php/jidm/article/view/2542}, 
  doi={10.5753/jidm.2022.2542},
  number={6}, 
  journal={Journal of Information and Data Management}, 
  author={Renato Moraes Silva and Pedro Reis Pires and Tiago A. Almeida}, 
  year={2023}, 
  issn = {2178-7107},
  month=jan
}
```

```
@inproceedings{silva-kdmile:2021_fakeNews,
    author = {Renato M. Silva and Tiago A. Almeida},
    title = {How concept drift can impair the classification of fake news},
    booktitle={Proceedings of the 9th Symposium on Knowledge Discovery, Mining and Learning (KDMiLe'21)}, 
	year={2021},
	month=oct,
	address = {Rio de Janeiro, RJ, Brazil},
	publisher= {Brazilian Computing Society},
    doi={10.5753/kdmile.2021.17469},
	pages={1--8},
	issn={2763-8944}
}
```

```
@article{bittencourt-asoc:2020_MLMDLText,
    author = {Marciele M. Bittencourt and Renato M. Silva and Tiago A. Almeida},
    title = {{ML-MDLText}: An efficient and lightweight multilabel text classifier with incremental learning},
    journal = {Applied Soft Computing},
    volume = {96},
    pages = {106699},
    year = {2020},
    month = {nov},
    issn = {1568-4946},
    publisher = {Elsevier},
    doi = {10.1016/j.asoc.2020.106699}
}
```


