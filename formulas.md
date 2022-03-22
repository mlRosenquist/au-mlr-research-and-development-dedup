## Definitions

$n$: number of samples

$c(n)$: average path length of unsuccessfull search - constant given n

$H(i)$: harmonic number - estimated by $ln(i) + e$

$h(x)$: path length - number of edges x traverses an itree from the root node

$n$: amount of instances/nodes - amount of bases in our situation

$s$: anomaly score - 
$s(x,n)=2^{\frac{-E(h(x))}{c(n)}}$

$E(h(x))$: average of $h(x)$ from a collection of isolation trees. 

$f_{base}=\log_2(n_{base})$ 

---

## Deriving equations
$\log_2(s)\cdot x \cdot c(n)=-E(h(x))$


$\log_2(s)=-\frac{E(h(x))+\log_2(f_{base})}{c(n_{samples})}$

$\log_2(s)\cdot x \cdot c(n) = -E(h(x))$

$\log_2(s) = -\frac{E(h(x))+\log_2(f_{base})}{c(n_{samples})}$


---


