# LOCAL QWEN ATOMIC WORKER — CASEIFICIO PRICE-002

Produce ONLY price_eur.py containing ONE top-level function:

def format_eur(cents):

Inputs:
- Accept only exact integers. bool is NOT an integer for this contract; reject True/False, floats, strings and None.
- Valid inclusive range 0 to 999999999 cents.
- Invalid input must raise ValueError.

Output:
- Format the full number of euro cents as a string, prefix the literal euro symbol €.
- Use a dot for every thousands group of the whole-euro portion.
- Use one decimal comma and ALWAYS exactly two digits for the cent portion.
- Never include spaces.
- Example outputs: 0 -> €0,00; 1 -> €0,01; 105 -> €1,05; 123456 -> €1.234,56; 999999999 -> €9.999.999,99.

Engineering directions:
- Separate euros and remaining cents using INTEGER division and modulo 100; do not convert amounts to float.
- Use the Python standard thousands grouping on the whole-euros integer, then replace its grouping comma with a dot.
- Format the cent remainder to exactly 2 digits.
- Use an explicit exact type check instead of isinstance because bool is an int subclass.

Restrictions:
- Python 3.8 source, no imports, only one function. No file access, network, OS calls, credentials, Git interactions, subprocess or side effects.
- No classes, helpers, decorators, module-level example calls, dynamic evaluation, or hidden tests.
- Return ONLY source code. The original 16 test cases on a separate MacBook are not available to you.
