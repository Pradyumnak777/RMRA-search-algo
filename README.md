# RMRA-search-algo

We present a multi-core processing aided exhaustive search algorithm to find optimal Robust Minimum Redundancy Arrays. 

### Input: 
Desired size of the linear antenna array **(n)**

### Output:
A single (valid) RMRA configuration is returned for every aperture **(L)**, ranging from **L = n-1** (which is essentially a Uniform Linear Array) onwards.

### Customizations:
- The upper bound of **L** can be set manually, as per requirements. As this program was developed to find optimal RMRA configurations that have not been previously reported, a suitably high **L** value (say 100) was chosen.

- The number of processes can also be changed, to ease the load on the CPU.


### Future Work
This algorithm can also be extrapolated to search for optimal configurations of k-Fold redundant sparse arrays.
    
