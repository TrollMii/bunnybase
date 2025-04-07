import pandas as pd
from PIL import Image
import numpy as np

from .hub import DataList
from . import Data, Hub
def hub_to_dataframe(hub: Hub) -> pd.DataFrame:
    data = hub.data
    categories = list(data.keys())
    h = dict[str, dict[tuple[str|int], list]]()
    for category in categories:
        for idx, ds in enumerate(data[category]):
            for k, v in ds.properties.items():
                if h.get(k) == None:
                    h[k] = {(category, idx): v}
                else:
                    h[k].update({(category, idx): v})
    
    df = pd.DataFrame(h)
    return df

def image_to_data(file, **metadata):
    image = Image.open(file)
    
    image_array = tuple(np.array(image).tolist())
    
    image_data = Data('image', image=image_array, **metadata)
    
    return image_data

def series_to_data(series: pd.Series, _name=None) -> Data:
    """Converts a pandas series into a bunny data object

    Args:
        series (pd.Series): Data Frame

    Returns:
        Data: Data object
    """
    keys = series.keys()
    
    properties = {str(keys[i]):series.iloc[i] for i in range(0, len(series))}
    name = series.name
    if name == None:
        name = _name
        if name == None:
            raise Exception("A data object need a category (Series name default), but the series has no name. You can also pass a name over the arguments")
    data = Data(str(name), **properties)
    return data
def dataframe_to_data(df: pd.DataFrame) -> DataList:
    """Converts a pandas dataframe into a bunny data object

    Args:
        df (pd.DataFrame): Your dataframe

    Returns:
        list[Data]: Your bunny data object
    """
    data = []
    for i in df.keys():
        _name = i
        if isinstance(i, int):
            name = f"i{i}"
        series = df[i]
        keys = series.keys()
    
        properties = {f'r{i}':series.iloc[i] for i in range(0, len(series))}
        name = series.name
        if name == None:
            name = _name
            if name == None:
                raise Exception("A data object need a category (Series name default), but the series has no name. You can also pass a name over the arguments")
        data.append(Data(str(name), **properties))
    return DataList(data)
