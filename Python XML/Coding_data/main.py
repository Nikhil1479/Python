import re
import xml.etree.ElementTree as ET
from datetime import datetime
# tree = ET.parse('./customer14235_loan14235_crif_report.xml')

# date_time_str = '18/09/19 01:55:19'

# date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')


# print("The type of the date is now",  type(date_time_obj))
# print("The date is", date_time_obj)
# root = tree.getroot(/)

customer_details = {
    '1': 'customer1113697_loan1115483_crif_report.html.xml',
    '2': 'customer1129550_loan1131339_crif_report.html.xml',
    '3': 'customer1195586_loan1197471_crif_report.html.xml',
    '4': 'customer14235_loan14235_crif_report.xml',
    '5': 'customer16475_loan16475_crif_report.html.xml',
    '6': 'customer773504_loan774538_crif_report.html.xml',
    '7': './customer40409_loan40409_crif_report.html.xml',
    '8': 'customer787561_loan788638_crif_report.html.xml',
    '9': 'customer794397_loan795497_crif_report.html.xml',
    '10': 'customer898231_loan899591_crif_report.html.xml'
}
for key in customer_details:
    tree = ET.parse(customer_details[key])
    root = tree.getroot()
    for loans in root.iter('LOAN-DETAILS'):
        dis_date = loans.find('DISBURSED-DATE').text
        date = loans.find('COMBINED-PAYMENT-HISTORY').text
        date_split = date.split('|')
        # date_regex = re.compile(r'(\d\d\d):(\d\d\d),(\d\d\d\d)')

        # for i in range(len(date_split)):
        #     mo = date_regex.search(date_split[i])
        #     print(mo.groups())
