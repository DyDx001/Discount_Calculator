# ------------------ DISCOUNT CALCULATOR PROGRAM ------------------

# Function to calculate the final price after discount
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, it is applied.
    Otherwise, the original price is returned.
    """
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price


# --- MAIN PROGRAM ---

# 1. Ask the user for the original price
price = float(input("Enter the original price of the item: "))

# 2. Ask the user for the discount percentage
discount_percent = float(input("Enter the discount percentage: "))

# 3. Call the function to calculate the final price
final_price = calculate_discount(price, discount_percent)

# 4. Display the result
if discount_percent >= 20:
    print(f"\n💰 The final price after {discount_percent}% discount is: ${final_price:.2f}")
else:
    print(f"\nℹ️ No discount applied. The price remains: #{final_price:.2f}")

# -------------------- END OF PROGRAM --------------------
