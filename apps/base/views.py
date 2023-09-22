from django.shortcuts import render
from faker import Faker

faker = Faker()


def index(request):
    return render(
        request=request,
        template_name="base/home_page.html",
        context={
            "greetings_text": " Hello! ",
            "title": "Home page",
        },
    )


def about_us_page(request):
    return render(
        request=request,
        template_name="base/about_us_page.html",
        context={
            "greetings_text": "Information about us",
            "title": "About us",
        },
    )


def contacts_page(request):
    user_name = faker.first_name()
    phone = faker.phone_number()
    email_domain = faker.domain_name()
    return render(
        request=request,
        template_name="base/contacts_page.html",
        context={
            "greetings_text": f"Our contacts: phone number: {phone}  email: {user_name}@{email_domain}"
            f"  address: Ukraine, Kyiv",
            "title": "Contacts",
        },
    )
