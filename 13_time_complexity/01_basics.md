- "Polynomial time" describes any run time that does not increase faster than n^k, which includes,
constant time (n^0),
logarithmic time (log base 2 of n),
linear time (n^1),
quadratic time (n^2),
and other higher degree polynomials like (n^3)
 
- "Superpolynomial time" describes any run time that does increase faster than n^k, which includes,
exponential time (2^n),
factorial time (n!),
and anything else faster.

- Examples:


1. (n/6) -> O(n)
it is a linear function, where the number of steps is always one sixth of the input size. Linear functions are polynomial.


2. (n^2 + 6n) -> O(n^2)
it is a quadratic function, where the number of steps is the input size squared plus 6 times the input size. Quadratic functions are polynomial.

3. (6n^6) -> (n^6)
 it is a high degree polynomial function, where the number of steps is the input size raised to the 6th power, multiplied by 6. It is a very fast growing polynomial function.

4. (6n) -> O(n)
it is an exponential function, where the number of steps is 6 raised to the power of n. Exponential functions are superpolynomial.

5. (6^2n^2) -> O(36^n^2)
it is also an exponential function, where the number of steps is 6 raised to the power of 2n^2. Exponential functions are superpolynomial.

6. n/10 -> polynomial, beceause it's a linear function

7. n! -> superpolynomial

8. n^10 -> polynomial, beceause it's an quadratic function

9. 10n^2 -> polynomial, beceause it's an quadratic function

10. 10^n -> superpolynomial, maybe because we don't know the power i.e (n)