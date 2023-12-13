from typing import Dict, List


def contact_schema(contact) -> Dict:
    return {"id": str(contact["_id"]),
            "first_name": contact["first_name"],
            "last_name": contact["last_name"],
            "email": contact["email"],
            "subject": contact["subject"],
            "message": contact["message"]}


def contacts_schema(contacts) -> List:
    return [contact_schema(contact) for contact in contacts]
