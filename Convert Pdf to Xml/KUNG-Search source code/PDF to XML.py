import os
import asposepdfcloud
from asposepdfcloud.apis.pdf_api import PdfApi

# Get App key and App SID from https://cloud.aspose.com
pdf_api_client = asposepdfcloud.api_client.ApiClient(
    app_key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    app_sid='xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx')

pdf_api = PdfApi(pdf_api_client)
filename = '4pages.pdf'
remote_name = '4pages.pdf'
output_file= '4pages.xml'
#upload PDF file to storage
pdf_api.upload_file(remote_name,filename)
#Covert PDF to XML and save in Aspose default storage
response=pdf_api.put_pdf_in_storage_to_xml(remote_name,output_file)
print(response)