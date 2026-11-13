def format_eur(cents):
    if not isinstance(cents, int) or cents < 0:
        raise ValueError("cents must be a nonnegative integer")
    
    euros = cents // 100
    cents %= 100
    
    # Format the euros part with thousands grouping and one comma before exactly two decimal digits
    euros_str = f"{euros:,.2f}"
    
    # Add the euro symbol at the beginning
    formatted_price = f"€{euros_str}"
    
    return formatted_price
