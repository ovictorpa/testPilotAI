from truncate_number import *
Here are some possible edge cases and scenarios for the `truncate_number` function:

* Input: A positive floating point number that is an integer (e.g., 3.0)
	+ Output: 0.0
* Input: A positive floating point number that has no decimal part (e.g., 5.0)
	+ Output: 0.0
* Input: A negative floating point number that is an integer (e.g., -3.0)
	+ Output: -0.0
* Input: A negative floating point number that has no decimal part (e.g., -5.0)
	+ Output: -0.0
* Input: A floating point number that is too large to be represented as an integer (e.g., 10000000000000000000000000000000