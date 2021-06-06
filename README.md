# Binclone python

Original implementation by the authors in c++ can be found [here](https://github.com/BinSigma/BinClone).

Paper for this code can be found [here](https://ieeexplore.ieee.org/document/6895418).

# How to use

Put the query asm file in `query.S` in the following format

```





00000000 <query_func>:
  4087ed:	c9                   	leave      // the query must start from here (8th line)
  4087ee:	c2 24 00             	ret    0x24
  4087f1:	55                   	push   ebp
  ...
```

Put the asm files that you wish to make database into some folder, such as `/data`. Run the following script (or, in case of this folder, running `region_detector_function_wise` will create database with `malware.txt` & run query.)

```python
from region_detector_fuction_wise import *
from glob import glob

assign_median_boundary(glob("./data/*"))
create_features_per_window(glob("./data/*"))
finding_matchings('query.S')
```

Normalizing conditions should be recored in `norm.json`, median boundaries will be automatically generated to `med_bounds.json` on calling `assing_median_boundary`.
