import requests, json, os

schoolYear = '202526'
course = 260  # LEI

for language in ['PT', 'ENG']:
    url = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetCourseDetail'
    payload = {
        'language': language,
        'courseCode': course,
        'schoolYear': schoolYear
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    response_dict = response.json()

    with open(os.path.join('data', 'files', f"ULHT{course}-{language}.json"), "w", encoding="utf-8") as f:
        json.dump(response_dict, f, indent=4)

    for uc in response_dict['courseFlatPlan']:
        url_uc = 'https://secure.ensinolusofona.pt/dados-publicos-academicos/resources/GetSIGESCurricularUnitDetails'
        payload_uc = {
            'language': language,
            'curricularIUnitReadableCode': uc['curricularIUnitReadableCode'],
        }
        response_uc = requests.post(url_uc, json=payload_uc, headers=headers)
        response_uc_dict = response_uc.json()

        with open(os.path.join('data', 'files', f"{uc['curricularIUnitReadableCode']}-{language}.json"), "w", encoding="utf-8") as f:
            json.dump(response_uc_dict, f, indent=4)

print("Ficheiros descarregados!")