import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 3


# gets an array of numbers
# returns - average, variance, standard deviation, covariance, median and interquartile range.
def get_stats(ndarray):
    avg = average(ndarray)
    var = variance(ndarray)
    standard_devi = std(ndarray)
    co_v = cov(ndarray)
    medi = median(ndarray)
    interquartile_range_ = interquartile_range(ndarray)

    return avg, var, standard_devi, co_v, medi, interquartile_range_


# utils

def average(df):
    return np.sum(df) / np.size(df)


def variance(df):
    return sum((df - average(df)) ** 2) / (np.size(df) - 1)


def std(df):
    return variance(df) ** 0.5


def cov(df):
    return std(df) / average(df)


def median(df):
    length = np.size(df)
    x = sorted(df)

    if length % 2 == 1:
        return x[(length + 1) // 2 - 1]
    return average([x[length // 2 - 1], x[length // 2]])


def interquartile_range(df):
    length = np.size(df)
    x = sorted(df)
    return median(x[(length - 1) // 2: length]) - median(x[: (length - 1) // 2 + 1])


# # 4
df = pd.read_csv("education_Data.csv", usecols=["TIME", "GEO", "Value"], na_values=":").dropna()

country_list = ['Ireland', 'Germany (until 1990 former territory of the FRG)', 'Estonia', 'Czech Republic', 'Denmark',
                'Belgium', 'Bulgaria',
                'Latvia', 'Lithuania', 'Luxembourg', 'Hungary', 'Greece', 'Spain', 'France', 'Italy',
                'Cyprus',
                'Slovenia', 'Slovakia', 'Netherlands', 'Austria', 'Poland', 'Portugal', 'Romania',
                'Malta', 'Finland']

means = np.zeros(len(country_list))
stds = np.zeros(len(country_list))
medians = np.zeros(len(country_list))
n = 0
for country in country_list:
    values = df[df.GEO == country].values[:, 2]

    avg, var, standard_devi, co_v, medi, interquartile_range_ = get_stats(values)
    min = np.min(values)
    max = np.max(values)
    means[n] = avg
    stds[n] = standard_devi
    medians[n] = medi
    n += 1

fig, ax = plt.subplots(2, figsize=(10, 10))
ax[0].barh(country_list, means, xerr=stds, color='Green', ecolor="red", label="Means")
ax[0].legend()

ax[1].barh(country_list, medians, color="purple", label="Medians")
ax[1].legend()
plt.show()

5


def print_stats(df, name):
    print("Data For ", name, ":")
    print("mean = ", average(df), "\n",
          "median = ", median(df), "\n",
          "std = ", std(df), "\n",
          "Interquartile range = ", interquartile_range(df), "\n")


adult = pd.read_csv("adult.csv", na_values=':').dropna()

fm_hr = adult[adult["sex"] == 'Female']['hr_per_week'].values
ml_hr = adult[adult["sex"] == 'Male']['hr_per_week'].values

print_stats(fm_hr, "Female hours of work")
print_stats(ml_hr, "Male hours of work")

fig, ax = plt.subplots(3, 1)
ax[0].hist([fm_hr, ml_hr], label=["Female", "Male"], color=['Pink', 'Blue'], density=False, bins=20)
ax[0].legend()
ax[0].set_title("Hours per week (Male/Female)")

ax[1].hist([fm_hr, ml_hr], label=["Female normed", "Male normed"], color=['Pink', 'Blue'], density=True, bins=20)
ax[1].legend()
ax[2].hist([fm_hr, ml_hr], label=["Female", "Male"], color=['Pink', 'Blue'], density=False, bins=20, cumulative=True)
ax[2].legend()
plt.show()

fm_hr_highest = adult[(adult["sex"] == 'Female') & (adult["income"] == ">50K\n")]['hr_per_week']
ml_hr_highest = adult[(adult["sex"] == 'Male') & (adult["income"] == ">50K\n")]['hr_per_week']

print_stats(fm_hr_highest, "Female hours of work - High Salary")
print_stats(ml_hr_highest, "Male hours of work - High Salary")

fig, ax = plt.subplots(3, 1)
ax[0].hist([fm_hr_highest, ml_hr_highest], label=["Female", "Male"], color=['Pink', 'Blue'], density=False, bins=20)
ax[0].legend()
ax[0].set_title("Hours per week (Male/Female) - Highest Salaries")

ax[1].hist([fm_hr_highest, ml_hr_highest], label=["Female normed", "Male normed"], color=['Pink', 'Blue'], density=True,
           bins=20)
ax[1].legend()
ax[2].hist([fm_hr_highest, ml_hr_highest], label=["Female", "Male"], color=['Pink', 'Blue'], density=True, bins=20,
           cumulative=True)
ax[2].legend()
plt.show()

#
print("for now the scientist seems to be right.")
#
clean_data = adult.drop(adult.index[((adult['hr_per_week'] > adult['hr_per_week'].mean() + (2.5 * adult['hr_per_week'].std())) | (adult['hr_per_week'] < adult['hr_per_week'].mean() - (2.5 * adult['hr_per_week'].std())))])

fm_hr_clean = clean_data[clean_data["sex"] == 'Female']['hr_per_week'].values
ml_hr_clean = clean_data[clean_data["sex"] == 'Male']['hr_per_week'].values

print_stats(fm_hr_clean, "Female hours of work : cleaned")
print_stats(ml_hr_clean, "Male hours of work : cleaned")

fig, ax = plt.subplots(3, 1)
ax[0].hist([fm_hr_clean, ml_hr_clean], label=["Female", "Male"], color=['Pink', 'Blue'], density=False, bins=20)
ax[0].legend()
ax[0].set_title("Hours per week (Male/Female) : clean data")

ax[1].hist([fm_hr_clean, ml_hr_clean], label=["Female normed", "Male normed"], color=['Pink', 'Blue'], density=True, bins=20)
ax[1].legend()
ax[2].hist([fm_hr_clean, ml_hr_clean], label=["Female", "Male"], color=['Pink', 'Blue'], density=True, bins=20, cumulative=True)
ax[2].legend()
plt.show()
