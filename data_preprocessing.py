import pandas as pd


#%% Load covid19 and owid data into pandas DatafFrame.
covid_data_path = "data/covid19.json"
covid_data = pd.read_json(covid_data_path)
covid_data = covid_data.from_dict(covid_data.records.to_list(), orient="columns")
covid_data.dateRep = pd.to_datetime(covid_data.dateRep)


owid_path = "data/owid-covid-data.xlsx"
owid_data = pd.read_excel(owid_path)
owid_data.date = pd.to_datetime(owid_data.date)

#%% Merge DataFrames on country names included in covid19

data = pd.merge(covid_data,
                owid_data,
                how="left",
                left_on=["countriesAndTerritories", "dateRep"],
                right_on=["location", "date"])