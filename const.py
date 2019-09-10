
# post method with params as json
LOGIN_URL = "http://htoa.tnebnet.org/oa-auth-service//tokens/login"
LOGIN_DATA = {"userName": "079204720584", "password": "", "appClientId": "OA"}

# get EDC mappings
EDC_URL = "http://htoa.tnebnet.org/oa-report-service/report/org-summaries?typeCode=EDC&fuelTypeCode=WIND"


# gen statment report id and pass Authorization header
GEN_STATEMENT_URL = """http://htoa.tnebnet.org/oa-service//api/gs/generationstatements?"""

PAYLOAD_GEN_STAT = {'dummy': '1', 'edc-id': '472', 'service-number': "079204720584", "statement-month": '08',
                    'statement-year': '2019'}

#  get reading using report id and pass auth_header
READINGS_URL = "http://htoa.tnebnet.org/oa-service//api/gs/generationstatement/{}"