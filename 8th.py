import numpy as np

import matplotlib.pyplot as plt

list1=[[1500,2000,1800,1200,900],[1600,2100,1900,1300,950],[1700,2200,2000,1400,1000],[1650,2150,1950,1350,980],[1750,2250,2050,1450,1020],[1800,2300,2100,1500,1050],[1900,2400,2200,1600,1100]]
covid_data=np.array(list1)
print(covid_data)

countries=["country1","country2","country3","country4","country5"]
days=["day1","day2","day3","day4","day5","day6","day7"]
total_cases=np.sum(covid_data,axis=1)
print(total_cases)
country_with_max_cases=countries[np.argmax(total_cases)]
print(country_with_max_cases)
average_cases_per_day=np.mean(covid_data,axis=0)
print(average_cases_per_day)
day_with_max_cases=days[np.argmax(average_cases_per_day)]
print(day_with_max_cases)
percentage_change_in_cases=np.diff(total_cases)/total_cases[:-1]
print(percentage_change_in_cases)
country_with_max_percentage_change=countries[np.argmax(percentage_change_in_cases)]
print(country_with_max_percentage_change)
noramlized_covid_data=(covid_data-np.mean(covid_data))/np.std(covid_data)
print(noramlized_covid_data)
plt.plot(days, noramlized_covid_data)
plt.xlabel('Days')
plt.ylabel('Number of Cases')
plt.title('COVID-19 Cases Over Time')
plt.legend(countries)
plt.show()