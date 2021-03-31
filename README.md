# CodingChallenge

This program can convert positive integers to Roman numerals and can convert Roman numerals to integers as well.

To run, enter either a valid Roman numeral or a positive integer as a command line argument 

Examples

python3 main.py XCIX

or 

python3 main.py 1234

I spent the full 4 hours working on this assignment and testing it. Based on the spec, I was not sure if V could precede L in a valid roman numeral. Ex. 45 = VL or 45 = XLV. I chose to assume that it could, meaning that 45 = VL would be valid. If this is not correct, a simple change would need to be made to the validPrecedingCharacters dictionary
