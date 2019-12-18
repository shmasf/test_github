# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + slideshow={"slide_type": "subslide"}
import pandas as pd
import numpy as np



# + cell_style="center" slideshow={"slide_type": "subslide"}
arr = np.ndarray(shape=[60], dtype=int)
display('Array', arr)
df = pd.DataFrame(arr, columns=['data'])
df.head()

# + [markdown] cell_style="center" slideshow={"slide_type": "subslide"}
# ### More code is coming...
#

# + cell_style="center" slideshow={"slide_type": "subslide"}
import qgrid
qgrid.show_grid(df)
# -

df





