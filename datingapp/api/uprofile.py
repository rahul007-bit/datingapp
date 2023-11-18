import frappe



@frappe.whitelist()
def hi():
    return "hi"


@frappe.whitelist()
def create_uprofile(first_name, middle_name, last_name, gender, email, username, date_of_birth,
                    picture_one=None, picture_two=None, picture_three=None, picture_four=None, picture_five=None):
    uprofile = frappe.new_doc("UProfile")
    uprofile.user = frappe.session.user
    uprofile.first_name = first_name
    uprofile.middle_name = middle_name
    uprofile.last_name = last_name
    uprofile.gender = gender
    uprofile.email = email
    uprofile.username = username
    uprofile.date_of_birth = date_of_birth
    uprofile.picture_one = picture_one
    uprofile.picture_two = picture_two
    uprofile.picture_three = picture_three
    uprofile.picture_four = picture_four
    uprofile.picture_five = picture_five

    uprofile.insert(ignore_permissions=True)

    return ("UProfile created successfully")