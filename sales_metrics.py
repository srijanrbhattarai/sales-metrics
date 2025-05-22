def apply_discount(sales, discount=0.1):
    """
    Applies a discount to each sale item.
    """
    return [round(sale * (1 - discount), 2) for sale in sales]

def filter_sales(sales, threshold=100):
    """
    Filters out sales below a given threshold.
    """
    return [sale for sale in sales if sale >= threshold]

def calculate_daily_sales(sales):
    return sum(sales)

if __name__ == "__main__":
    sample_sales = [50, 100, 200, 75, 150]
    filtered = filter_sales(sample_sales, threshold=100)
    discounted = apply_discount(filtered, discount=0.2)
    print("Filtered Sales:", filtered)
    print("Discounted Filtered Sales:", discounted)
    print("Total Discounted Filtered Sales:", calculate_daily_sales(discounted))