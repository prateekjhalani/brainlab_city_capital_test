# Import necessary libraries
import requests
from django.db import migrations, models

# Define the API URL
API_URL = "https://countriesnow.space/api/v0.1/countries/capital"


def fetch_countries_data(apps, schema_editor):
    # Import the Country model
    Country = apps.get_model("quiz", "Country")

    try:
        # Make a GET request to the API
        response = requests.get(API_URL)
        country_data = []
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()["data"]

            # Iterate through the data and create Country objects
            for item in data:
                country_data.append(Country(
                    name=item["name"],
                    capital=item["capital"],
                    iso2=item["iso2"],
                    iso3=item["iso3"]
                ))

        # Bulk create country data into database.
        Country.objects.bulk_create(country_data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data from the API: {e}")


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(fetch_countries_data),
    ]
