class InvalidEmailException(Exception):
    pass


def parse_email(address):
    username, domain = address.split("@")
    if not username or not domain:
        raise InvalidEmailException("Username or domain empty")
    return username, domain


if __name__ == "__main__":
    emails = [
        "john.doe@test.com",
        "john@doe@test.com",
        "jane.doe@email.com",
        "jane.doe",
        "@test.com",
    ]

    for email in emails:
        try:
            parse_email(email)
        except ValueError:
            print(f"Invalid email address: {email}")
        except InvalidEmailException as ex:
            print(f"{ex}: {email}")
        except Exception as ex:
            print(f"Another exception occurred: {ex}, {type(ex)}")
        else:
            print(f"Valid address: {email}")
        finally:
            print("Executes every time")
