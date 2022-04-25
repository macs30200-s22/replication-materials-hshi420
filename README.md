[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6481847.svg)](https://doi.org/10.5281/zenodo.6481847)
# replication-materials-hshi420
The code is written in Python 3.9.7 and all of its dependencies can be installed by running the following in the terminal (with the ``requirements.txt`` file included in this repository): 
```
pip install -r requirements.txt
```
Then you can import the initial_analysis module located in ``code`` directory.
```
import initial_analysis #make sure that you are in the code directory
```
The initial analysis uses preprocessed data ``left_leaning_factcheckers.csv`` located in the the ``processed_data`` directory. Run the following code to replicate the results.
```
initial_analysis.initial_analysis('../processed_data/left_leaning_factcheckers.csv')
```
The processed_data directory only contains the processed data that is used in initial process, and the code for preprocessing data are in ``analysis.ipynb`` located in the ``code`` directory. The raw data is too large to be uploaded to github, and I have uploaded them to Google drive.
</br></br>
link to data: https://drive.google.com/drive/folders/1KMN5FP7Oytbm5zefKjAaYp-LuMoLDdV8?usp=sharing
</br></br>
### Initial Analysis Results:
Correlation between proportion of Democrat statement rated as false and proportion of Republican statement rated as false: </br>
*Pearson correlation* = -0.5511132959504763, *p* = 2.639847472009231e-30
![plot](README_file/initial_analysis.png) </br>
In this plot, each data point represents a factchecker. </br></br>

We can see that the proportion of Democrat statement rated as false and proportion of Republican statement rated as false are negatively correlated. Our first research question that whether there is difference (I might modify the question to whether they are negatively correlated) between the proportion of Democrat statement rated as false and proportion of Republican statement rated as false is answered. With this test of our first hypothesis, we can continue to explore the mechanisms behind this negative correlation.

