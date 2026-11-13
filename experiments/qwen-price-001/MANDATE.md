# QWEN LOCAL WORKER — CASEIFICIO-PRICE-001

## Task
Create exactly one source file price_eur.py, Python 3.8-compatible, implementing exactly one top-level pure function:

    def format_eur(cents):

The argument is an exact Python int, excluding bool, in the inclusive range 0..999999999. Otherwise raise ValueError. Interpret the argument as a nonnegative price in euro cents. Return a Python string formatted as euros using:
- the literal euro symbol € as a prefix;
- dots as thousands grouping for euros;
- one comma before exactly two decimal digits;
- no spaces.

Examples: format_eur(0)="€0,00"; format_eur(105)="€1,05"; format_eur(123456)="€1.234,56".

## Strict constraints
Only Python source. One function and no other top-level code.
Do not import modules, print, access environment, files, network, Git, secrets, system tools or runtime state.
No class, decorators, recursive function, dynamic evaluation, unsafe APIs or function definitions nested inside.
Use only builtin str, int, type, isinstance, divmod, or format, if needed.
No additional dependencies. Return only source code, with no explanations or markdown fences.
The frozen independent tests are withheld from the model.
This is an isolated noncommercial task. The result must be judged independently before any publication.
