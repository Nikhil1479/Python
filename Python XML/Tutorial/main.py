import xml.etree.ElementTree as ET

tree = ET.parse('./books.xml')
tree2 = ET.parse('./customer14235_loan14235_crif_report.xml')

root = tree.getroot()
root2 = tree2.getroot()


# for details in root2.findall('LOAN-DETAILS'):
#     acct = details.find('ACCT-NUMBER').text
#     print(acct)

# for books in root:
#     print(books.attrib)

# for details in root2.findall('INDV-REPORT-FILE'):
#     print(details.tag)
for loans in root2.iter('LOAN-DETAILS'):
    print(loans.find('DISBURSED-DATE').text)
