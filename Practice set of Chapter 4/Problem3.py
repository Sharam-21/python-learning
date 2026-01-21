# Check that a type cannot changed in the python.


a = (22, 67, 21, 98, "Harry")
a[4] = "Shami"


'''a[4] = "Shami"
    ~^^^
TypeError: 'tuple' object does not support item assignment'''