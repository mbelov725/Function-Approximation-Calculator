# Function Approximation Calculator
This project allows users to approximate mathematical functions using Legendre and Taylor polynomials,
with interactive visualization using the Desmos Graphing Calculator API

## Demo
<img width="1918" height="868" alt="image" src="https://github.com/user-attachments/assets/781bdcd1-793f-43f3-9c52-768d1fa944bb" />

## Overview 
This project uses Legendre polynomials to approximate a function $f(x)$ on an 
interval $[a, b]$ using a polynomial of degree $n$, $P_n(x)$. It does this by 
minimizing something called the $\ell^2$ norm, which can be thought of as the "distance" between two functions.
It is defined as:

<div align="center">

$$
\displaystyle \sqrt{\int_{a}^{b} \left[ f(x) - P_n(x) \right]^2 \, dx}
$$

</div>

A common assumption would be to use the Taylor 
polynomial of degree $n$, $T_n(x)$; however, this does not actually minimize the $\ell^2$ error on 
the interval.

### Vector Spaces
To find the optimal solution, we need to turn to linear algebra. It is useful to 
think of functions in terms of vector spaces. Consider a vector space consisting 
of all the functions continuous on $[a, b]$. One subspace of this vector space is 
non-polynomials, such as exponential, logarithmic, and trigonometric functions;
let's call this subspace $V$. Another subspace of this vector space would be all 
of the polynomials; let's call this subspace $U$. Now, let's say we take a vector $\vec{v}$ from
subspace $V$, i.e. a specific function, such as $\sin(x)$, and we want 
to find a vector $\vec{u}$ from subspace $U$, i.e. a polynomial, that minimizes the 
distance between the two vectors. The best option is something called an orthogonal
projection. This is kind of like casting a shadow of the vector $\vec{v}$ onto the
subspace $U$.

### Finding an Orthonormal Basis for the Non-Polynomials
First, we need to find an orthonormal basis for $U$. Orthonormal means that for any
two vectors in the subspace, their dot product is 0. Using an orthonormal basis allows our calculations
to be much simpler.

Defining the dot
product for functions is slightly more difficult. This can be done by computing 
the inner product of two functions $f(x)$ and $g(x)$: 

<div align="center">

$$
\displaystyle \langle f, g \rangle = \int_{a}^{b} f(x)g(x)dx
$$

</div>

### Legendre Polynomials

We will use the Legendre polynomials to construct our basis. 

For reference, the first few Legendre polynomials are:
| $n$ | $P_n(x)$ |
|---|--------|
| $0$ | $1$ |
| $1$ | $x$ |
| $2$ | $\frac{1}{2}\left( 3x^2 - 1 \right)$ |
| $3$ | $\frac{1}{2}\left( 5x^3 - 3x \right)$ |
| $4$ | $\frac{1}{8}\left( 35x^4 - 30x^2 + 3 \right)$ |
| $5$ | $\frac{1}{8}\left( 63x^5 - 70x^3 + 15x \right)$ |

These polynomials have the unique property that for any two polynomials $P_n(x)$ and $P_m(x)$ of degree $n$ and $m$,
respectively:

<div align="center">

$$
\displaystyle \int_{a}^{b} P_n(x)P_m(x)dx = 
\begin{cases}
0 & \text{if } n \ne m \\
\frac{2}{2n+1} & \text{if } n = m
\end{cases}
$$

</div>

### Finding the Best Approximation

Legendre polynomials are orthogonal on $t \in [-1, 1]$. To use them on an interval $x \in [a, b]$, we need to map
$x$ onto $t$ using:

<div align="center">

$$
t = \frac{2x - a - b}{b - a}.
$$

</div>

The best approximation $P_n(x)$, i.e. that minimizes the $\ell^2$ norm error, is represented as:
<div align="center">

$$
P_n(x) = \sum_{k=0}^{n} c_k P_k(t)
$$

</div>

where the coefficients $c_k$ are given by the orthogonal projection formula:

<div align="center">

$$
c_k = \frac{\langle f, P_k \rangle}{\langle P_k, P_k \rangle} 
= \frac{2k + 1}{b - a} \int_a^b f(x)P_k(t) dx
$$

</div>

Interestingly enough, if we look at the demo, the Legendre approximation for $\sin(x)$ has a significantly smaller $\ell^2$ norm error than the Taylor approximation

## Features
* Function input
  * Users can enter any mathematical function over a given interval
  * Note:
    * Prefix inverse trigonometric functions with ```-a```, e.g. write $\arcsin(x)$ as ```asin(x)```
    * For $e^x$, write ```exp(x)```
    * For $n^x$, write ```n**x```
    * For $\ln(x)$, wrtie ```log(x)```
    * Make sure that the function is defined on the given interval
    * You may need to modify some of the formatting in Desmos after
* Polynomial approximations
  * Taylor series approximation up to any user-specified degree
  * Legendre polynomial least-squares approximation up to any user-specified degree
* LaTeX conversion
  * Approximations are converted into Desmos-compatible LaTeX
  * Users can copy or view the exact formulas
* JSON export and HTML template
  * All generated functions, approximations, and interval info are saved to ```functions.json```
  * This data is updated to ```desmos_template.html```
* Desmos visualization
  * Interactive plotting of the original function and Taylor and Legendre approximations
  * Computes $\ell^2$ norm error for both approximations
  * Each curve is colour-coded, and the approximations have dashed lines
* Secure API handling
  * Users store their Desmos API key in a ```.env``` file
  * ```main.py``` inserts the key at runtime, so it is never stored in the repository

## Getting Started

1. Clone the repository
   ```bash
   git clone https://github.com/your-username/function-approximation.git
3. Install SymPy, SciPy, and dotenv if neccessary
   ```bash
   py -m pip install sympy
   py -m pip install scipy
   py -m pip install dotenv
4. Add Desmos API key
   
   Create a ```.env``` file in the project root
   
   Visit https://www.desmos.com/my-api and log in to access a free API key
   ```
   API_KEY=your_desmos_api_key_here
5. Run ```main.py```
   ```bash
   py src/main.py
    ```
   Input your function, right endpoint, left_endpoint, and the degree of your polynomial approximation
6. Run on a local server
   ```bash
   py -m http.server 8000
7. Visit ```http://localhost:8000/web/desmos.html``` to view your approximations
8. To stop the local server, press ```Ctrl + C```

