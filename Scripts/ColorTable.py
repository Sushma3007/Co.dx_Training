#Below Code is used to get the color table 
import pandas as pd

def get_color_table(df, show_searchbar=False, multiple_tables=False):
    """to get color table on co.dx UI. download button is a default feature for simple table.

    To add a color to a specific column (ex : column 'Population'), create another column suffixed with _bgcolor
    ex: Population_bgcolor, values of this column should be the name of the color for the corresponding row

    
    df = pd.DataFrame(datasets.load_diabetes().data)
    df.columns = datasets.load_diabetes().feature_names
    df.head(5)



    Args:
        df (pandas dataframe): input data
        show_searchbar (bool, optional): if True, this will render a search bar on UI. Defaults to False.
        multiple_tables (bool, optional): if true, this will render multiple table with single json. Defaults to False.

    Returns:
        dict: a table dictinary
    """

    actual_columns = df.columns[~df.columns.str.contains("_bgcolor")]
    bg_color_columns = df.columns[df.columns.str.contains("_bgcolor")]


    table_data = []
    for index, row in df[actual_columns].iterrows():
        row_list = []
        for col, value in row.items():
            if col + '_bgcolor' in bg_color_columns:
                row_dict = {}
                row_dict['value'] = value
                row_dict['bgColor'] = df[col + '_bgcolor'].iloc[index]
                row_list.append(row_dict)
            else:
                row_list.append(value)
        table_data.append(row_list)

    comp_dict = {}
    comp_dict['table_headers'] = df[actual_columns].columns.values.tolist()
    comp_dict['table_data'] = table_data
    comp_dict['show_searchbar'] = show_searchbar
    comp_dict['multiple_tables'] = multiple_tables
    return comp_dict

import json

from sklearn.datasets import load_iris
import pandas as pd
load_data = load_iris()

df = pd.DataFrame(load_data.data, columns=load_data.feature_names)
df['Type'] = load_data.target
df['Type'] = df['Type'].apply(lambda x: load_data.target_names[x].title())

color_dict = {'Setosa': 'red', 'Versicolor': 'Yellow', 'Virginica': 'green'}
df['Type_bgcolor'] = df['Type'].apply(lambda x : color_dict[x])


container_dict = {}
container_dict = get_color_table(df, show_searchbar=False, multiple_tables=False)

dynamic_outputs = json.dumps(container_dict)