"""
Add custom field parsing by subclassing FieldParser.
"""

from dbfreaddm import DBF, FieldParser

class CustomFieldParser(FieldParser):
    def parseC(self, field, data):
        # Return strings reversed.
        return data.rstrip(b' 0').decode()[::-1]

for record in DBF('files/people.dbf', parserclass=CustomFieldParser):
    print(record['NAME'])
