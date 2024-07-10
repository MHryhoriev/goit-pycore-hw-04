def add_contact(args, contacts):
    """
    Add a contact with the specified name and phone number to the contacts dictionary.

    Args:
    - args (list): A list containing two elements: name and phone.
    - contacts (dict): Dictionary containing contacts where the new contact will be added.

    Returns:
    - str: A message indicating whether the contact was successfully added or already exists.
    """

    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return "Contact already added."

def change_contact(args, contacts):
    """
    Change the phone number of an existing contact in the contacts dictionary.

    Args:
    - args (list): A list containing two elements: name and phone.
    - contacts (dict): Dictionary containing contacts where the contact will be updated.

    Returns:
    - str: A message indicating whether the contact was successfully updated or not found.
    """

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return f"Contact '{name}' not found."

def show_phone(name, contacts):
    """
    Retrieve the phone number of a contact from the contacts dictionary.

    Args:
    - name (str): The name of the contact to retrieve.
    - contacts (dict): Dictionary containing contacts.

    Returns:
    - str: The phone number of the contact, or a message indicating the contact was not found.
    """

    return contacts.get(name, f"Contact '{name}' not found.")

def show_all_contacts(contacts):
    """
    Retrieve a formatted string listing all contacts and their phone numbers.

    Args:
    - contacts (dict): Dictionary containing contacts to display.

    Returns:
    - str: A formatted string listing all contacts and their phone numbers, or a message indicating no contacts are available.
    """

    if contacts:
        contact_list = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
        return f"Contacts:\n{contact_list}"
    else:
        return "No contacts available."
