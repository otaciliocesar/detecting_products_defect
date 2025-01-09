# %%
import numpy as np
# %%
import scipy.stats as stats

# %%
## Task 1:
lam = 7
# %%
## Task 2:
print(stats.poisson.pmf(lam, lam))
# %%
## Task 3:
defect_day_4 = stats.poisson.cdf(4, lam)
print(defect_day_4)
# %%
# ## Task 4:
defect_day_9 = 1 - stats.poisson.cdf(9, lam)
print(defect_day_9)
# %% ## Task 4:
year_defects = stats.poisson.rvs(lam, size=365)
# %%
print(year_defects[0:20])
# %%
## Task 7:
print(lam*365)
# %%
## Task 8:
print(sum(year_defects))
# %%
## Task 9:
print(np.mean(year_defects))
# %%
## Task 10:
print(year_defects.max())
# %%
## Task 11:
print(1 - stats.poisson.cdf(year_defects.max(), lam))
# %%
## Task 12:
print(stats.poisson.ppf(0.9, lam))
# %%
## Task 13:
print(sum(year_defects > stats.poisson.ppf(0.9,lam))/len(year_defects))
# %%