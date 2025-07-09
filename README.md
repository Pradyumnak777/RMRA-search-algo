# RMRA-search-algo

This code forms an integral part of our paper(under review, preprint not generated yet) - *A Leap-on-Success Exhaustive Search Method to Find Optimal Robust Minimum  Redundancy Arrays (RMRAs)*

We present a multi-core processing aided exhaustive search algorithm to find RMRA configurations. 

**Input:** Desired size of the linear antenna array*(n)*
**Output:** A single (valid) RMRA configuration is returned for every *L(aperture)*, ranging from L = n-1 (which is essentially a Uniform Linear Array) onwards. The upper bound of L can be set manually, as per requirements. As this program was developed to find optimal RMRA configurations that have not been previously reported, a suitably high L value (say 100) was chosen.
    
