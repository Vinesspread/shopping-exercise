def apply_student_discount(total, is_student):
    if is_student:
        return total * 0.90
    return total

if __name__ == "__main__":
    original_total = 2500
    print(f"Original total: {original_total}")
    discounted = apply_student_discount(original_total, True)
    print(f"Price after student discount: {discounted}")
    # checkout.py
def calculate_price(original_price, is_student):
    if is_student:
        return original_price * 0.9  # 学生10%折扣
    else:
        return original_price

if __name__ == "__main__":
    print(calculate_price(100, True))
    print(calculate_price(100, False))
