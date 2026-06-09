atm_vault_balance = 50000000
user_account_balance = 10000000


def display_balances():
    """Display user balance and ATM vault balance"""
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money(amount):
    """
    Deposit money into account and ATM vault
    return: bool
    """
    global atm_vault_balance, user_account_balance

    if amount <= 0:
        print("Số tiền không hợp lệ")
        return False

    user_account_balance += amount
    atm_vault_balance += amount

    print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VND.")
    return True


def check_withdrawal_rules(amount):
    """
    Check withdrawal conditions
    return: status string
    """
    global atm_vault_balance, user_account_balance

    fee = 1100
    total_deduction = amount + fee

    if amount <= 0:
        return "INVALID"

    if amount % 50000 != 0:
        return "NOT_MULTIPLE"

    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"

    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"

    return "OK"


def execute_withdrawal(amount):
    """
    Execute withdrawal transaction
    """
    global atm_vault_balance, user_account_balance

    fee = 1100
    total_deduction = amount + fee

    atm_vault_balance -= amount
    user_account_balance -= total_deduction

    print("--- RÚT TIỀN ---")
    print(f"Phí giao dịch: {fee:,} VND")
    print(f"Bạn đã rút thành công {amount:,} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND.")


def main():
    while True:
        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")

        choice = input("Vui lòng chọn giao dịch (1-4): ")

        if choice == "1":
            display_balances()

        elif choice == "2":
            try:
                amount = int(input("--- NẠP TIỀN ---\nNhập số tiền muốn nạp: "))
                deposit_money(amount)
            except:
                print("Số tiền không hợp lệ")

        elif choice == "3":
            try:
                amount = int(input("--- RÚT TIỀN ---\nNhập số tiền cần rút: "))
                status = check_withdrawal_rules(amount)

                if status == "INVALID":
                    print("Số tiền không hợp lệ")

                elif status == "NOT_MULTIPLE":
                    print("Số tiền rút phải là bội số của 50,000")

                elif status == "INSUFFICIENT_FUNDS":
                    print("Không đủ số dư tài khoản")

                elif status == "ATM_OUT_OF_CASH":
                    print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")

                else:
                    print("Giao dịch đang xử lý...")
                    execute_withdrawal(amount)

            except:
                print("Số tiền không hợp lệ")

        elif choice == "4":
            print("Cảm ơn quý khách đã sử dụng dịch vụ!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()