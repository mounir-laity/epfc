import numpy as np
import pandas as pd

def has_vowels(ser):
    vowels = "aeiouy"
    elements_with_vowels = []
    for element in ser:
        cpt = 0
        for letter in element:
            if letter in vowels:
                cpt += 1
                if cpt >= 2:
                    elements_with_vowels.append(element)
    return elements_with_vowels

color_series = pd.Series(['Red', 'Green', 'Orange', 'Pink', 'Yellow','White'])
elements_with_vowels = has_vowels(color_series)
print(elements_with_vowels)
print(color_series[~color_series.isin(elements_with_vowels)])