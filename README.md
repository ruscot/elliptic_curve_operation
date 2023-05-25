# Elliptic curve operation
This folder contain python script which perform basic elliptic curve operation such as
- Inverse of a point `inverse_element`
- Test if a point is on the curve `is_on_curve`
- Doubling operation P->2P `doubling`
- Addition in the function `__add__` so if you have the point P and Q you just have to do P+Q
- Scalar multiplication `__rmul__`
- A function that perform the Diffie-Hellman key exchange in `diffie_hellman`