def format_eur(cents):
    if not isinstance(cents, int) or cents < 0 or cents > 999999999:
        raise ValueError("Invalid input. Please provide an integer between 0 and 999999999.")
    
    euros = cents // 100
    remainder_cents = cents % 100
    
    formatted_euros = f"{euros:,}"
    formatted_remainder_cents = "{:02d}".format(remainder_cents)
    
    return f"€{formatted_euros}.{formatted_remainder_cents}"
