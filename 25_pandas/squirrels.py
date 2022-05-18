import pandas

data_squirrel = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data_squirrel["Primary Fur Color"].value_counts()



fur = fur_color.to_dict()
fur_df = {
    'fur color': ['grey', 'red', 'black'],
    'count': [fur['Gray'], fur['Cinnamon'], fur['Black']]
}
fur_df = pandas.DataFrame(fur_df)
fur_df.to_csv('fur_color.csv')