class OrderData:
    # first_name_error_message = "Error: First Name is required"
    # last_name_error_message = "Error: Last Name is required"
    # postal_code_error_message = "Error: Postal Code is required"

    user_data = [["", " Ivso", "54321", "Error: First Name is required"],
                 ["Den", "", "54321", "Error: Last Name is required"],
                 ["Den", " Ivso", "", "Error: Postal Code is required"]]

    user_data_with_valid_credential = ["Den", " Ivso", "54321"]
    successful_massage = "Thank you for your order!"
