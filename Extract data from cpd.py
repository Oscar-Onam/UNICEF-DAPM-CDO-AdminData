import requests
import pandas as pd
from bs4 import BeautifulSoup
import PyPDF2

"""
Set up URL of UNICEF Executive Board & send an HTTP GET request.
The URL contains Country programme document archive of country 
programme requests to be presented to the Executive Board in 2023 and 2024
"""

url = "https://www.unicef.org/executiveboard/country-programme-documents"

response = requests.get(url)
if response.status_code == 200:
  soup = BeautifulSoup(response.content, 'html.parser') # Create a BeautifulSoup object to parse the HTML content
  table = soup.find('table') # Find the table element containing the data
else:
 # print('The request was NOT successful')
  print(response.status_code)

# Initialize lists to store extracted data on URL
country_names = []
implementation_periods = []
en_document_urls = []
text = []
start_year = []
end_year = []

# Create a data frame to store the extracted data
data_frame = {'Country': country_names,
              'Implementation Period': implementation_periods,
              'URL': en_document_urls,
              'Text from CPD': text,
              'Start year of implementation period': start_year,
              'End year of implementation period': end_year}

# Check if the table element is None
if table is not None:
    # Iterate through the rows in the table
     for row in table.find_all('tr')[1:]:
      columns = row.find_all('td')

      if len(columns) >= 2:
    # Extract 'country' and 'Programme documents' text
        country = columns[0].get_text()
        documents_cell = columns[1]

    # Extract the implementation period (e.g., '[2015-2025]')
        implementation_period = documents_cell.get_text()

    # Extract links of CPDs written in English
        en_links = documents_cell.find_all('a', text='EN')
        en_document_urls.extend([link['href'] for link in en_links])

    # Append data to the respective lists
        country_names.append(country)
        implementation_periods.append(implementation_period)
"""
# Define a function to extract text from a PDF document
def extract_text_from_pdf(pdf_url):
    pdf_file = PyPDF2.PdfFileReader(pdf_url)
    text = ""
    for page in pdf_file.pages:
        text += page.extractText()
    return text
"""

# Iterate over the 'Implementation Period' column and split each string
for period in data_frame['Implementation Period']:
    start_year, end_year = period.split('-')

    # Append the start and end years to the respective lists
    start_years.append(start_year)
    end_years.append(end_year)

# Create new columns in the data frame to store the start and end years
data_frame['start_year'] = start_years
data_frame['end_year'] = end_years

print(data_frame)
