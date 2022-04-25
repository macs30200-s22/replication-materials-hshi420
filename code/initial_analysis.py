import pandas as pd
import numpy as np

from scipy import stats

import matplotlib.pyplot as plt

def initial_analysis(file_name):
	r = pd.read_csv(file_name)

	pearson = stats.pearsonr(r.democrat_false, r.republican_false)

	print(f'Pearson correlation = {pearson[0]}, p = {person[1]}')

	coef = np.polyfit(r.democrat_false, r.republican_false, 1)

	poly1d_fn = np.poly1d(coef)
	
	plt.plot(r['democrat_false'],r['republican_false'], 'ro', r['democrat_false'], poly1d_fn(r['democrat_false']))

	plt.xlabel('proportion of democrat statement rated as false')
	plt.ylabel('proportion of republican statement rated as false')

	plt.savefig('initial_analysis.png', dpi = 100)

	return

def main():
	initial_analysis()

if __name__ == '__main__':
	main()