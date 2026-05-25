def get_simple_interest(principal, rate, time):
    """
    Calculate and return simple interest.

    Args:
        principal: The initial amount of money
        rate: The annual interest rate (in percentage)
        time: The time period (in years)

    Returns:
        The calculated simple interest
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest


# Test the function
if __name__ == "__main__":
    # Example 1: Principal = 1000, Rate = 5%, Time = 2 years
    principal = 1000
    rate = 5
    time = 2
    si = get_simple_interest(principal, rate, time)
    print(f"Principal: {principal}, Rate: {rate}%, Time: {time} years")
    print(f"Simple Interest: {si}")

    # Example 2: Principal = 5000, Rate = 8%, Time = 3 years
    si2 = get_simple_interest(5000, 8, 3)
    print(f"\nSimple Interest for 5000 at 8% for 3 years: {si2}")
