class CustomException(Exception):
    pass


def parse_email(address):
    """
    Extracts username and domain from address
    Raises ValueError for invalid email addresses
    """
    username, domain = address.split("@")
    if "." not in domain:
        raise ValueError("Invalid domain")
    return username, domain


if __name__ == "__main__":
    email_addresses = [
        "john.doe@email.com",
        "john@@email.com",
        "john@email",
        "johndoeemail.com",
    ]

    for email_address in email_addresses:
        try:
            user, dom = parse_email(email_address)
        except (ValueError, LookupError) as ex:
            print(f"Invalid address: {email_address}")
            # print(ex, type(ex))
        except RuntimeError:
            print("Do something different for this exception")
        else:
            print(f"Successfully parsed; domain={dom}, username={user}")
        finally:
            print("Executes every time")
