import frappe


@frappe.whitelist()
def create_uprofile(
    first_name,
    middle_name,
    last_name,
    gender,
    email,
    username,
    date_of_birth,
):
    uprofile = frappe.new_doc("UProfile")
    uprofile.user = frappe.session.user
    uprofile.first_name = first_name
    uprofile.middle_name = middle_name
    uprofile.last_name = last_name
    uprofile.gender = gender
    uprofile.email = email
    uprofile.username = username
    uprofile.date_of_birth = date_of_birth
    uprofile.insert(ignore_permissions=True)

    return "UProfile created successfully"



