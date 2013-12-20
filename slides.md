## yt unit benchmarks

Nathan Goldbaum (Original credit Trevor Bekolay) <br>
[bekolay.org/scipy2013-quantities](http://bekolay.org/scipy2013-quantities)




## Creating a quantity

1. Multiply magnitude by unit <span data-icon="&#xe007;" class="fragment"></span>
```python
length = 5.0 * q.meter
```
2. Quantity constructor with unit argument (string or unit)
```python
length = q.Quantity(5.0, units='meter')
length = q.Quantity(5.0, units=q.meter)
```


<div id="syntax" class="table-container"></div>



# Compatibility


## NumPy magnitudes

```python
length = np.ones((3, 3)) * q.meter

length = q.Quantity(np.ones((3, 3)),
                    units='meter')
length = q.Quantity(np.ones((3, 3)),
                    units=q.units.meter)
```


<div id="compatibility-syntax" class="table-container"></div>


## Python operators

* Unary (e.g., `-length`)
* Binary (e.g., `length * other_length`)
  * `length` and `other_length` have same units
  * `length` and `other_length` have compatible units
  * `length` and `other_length` have different units


<div id="compatibility-unary_ops" class="table-container"></div>


<div id="compatibility-binary_same_ops" class="table-container"></div>
Binary operators, same units


<div id="compatibility-binary_compatible_ops" class="table-container"></div>
Binary operators, compatible units


<div id="compatibility-binary_different_ops" class="table-container"></div>
Binary operators, different units



# Speed


<div id="speed"><svg></svg></div>



