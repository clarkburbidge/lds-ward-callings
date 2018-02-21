

def get_sub_orgs_callings():
    import lds_org
    import creds
    import json
    d = {}
    with lds_org.session(creds.usr, creds.pwd) as lds:
        rv = lds.get('https://lds.org/mls/mbr/services/orgs/sub-orgs-with-callings?lang=eng')
        for org in rv.json():
            orgName = org_name_replace(org['defaultOrgName'])
            d[orgName] = []
            # print('\n{0}\n{1}'.format(orgName, '-------------------------------------'))
            for call in org['callings']:
                # print_calling(call)
                dict_calling(d, orgName, call)
            for suborg in org['children']:
                for call in suborg['callings']:
                    # print_calling(call)
                    dict_calling(d, orgName, call)

    # with open('C:\\Dev\\Python\\LDSIO\\json_formats\\subOrgDict.json', 'w+') as f1:
    #     json.dump(d, f1, indent=4)
    return d


def dict_calling(d, orgName, call):
    name = call['memberName']
    position = call['position']
    positionId = call['positionId']
    activeDate = call['activeDate']
    displaySequence = call['positionDisplayOrder'] if type(call['positionDisplayOrder']) is int else 9999
    subOrgId = call['subOrgId'] if type(call['subOrgId']) is int else 9999999
    subOrgTypeId = call['subOrgTypeId']
    positionTypeId = call['positionTypeId']
    calling = {'name': name,
               'position': position,
               'activeDate': activeDate,
               'displaySequence': displaySequence,
               'subOrgId': subOrgId,
               'subOrgTypeId': subOrgTypeId,
               'positionId': positionId,
               'positionTypeId': positionTypeId
               }
    d[orgName].append(calling)


def print_calling(call):
    position = abr_call(call['position'])
    if call['memberName'] is None:
        print('{0}: NONE'.format(position))
    else:
        date = fix_date(call['activeDate'])
        name = arrange_name(call['memberName'])
        print('{0}: {1} - ({2})'.format(position, name, date))


def arrange_name(n):
    last = n.split(',')[0]
    first = n.split(',')[1].strip().split(' ')[0]
    return first + ' ' + last


def fix_date(d):
    year = d[:4]
    month = d[4:6]
    d = year + '/' + month
    return d


def org_name_replace(name):
    replace_values = {
        'Other Callings': 'Additional Callings'
    }
    for key, value in replace_values.items():
        if key in name:
            name = name.replace(key, value)
    return name


def abr_call(c):
    bulk = {
        'First Counselor': '1stC',
        'Second Counselor': '2ndC',
        'Secretary': 'Sec',
        'Assistant': 'Asst',
        'Leader': 'Ldr',
        'Group': 'Grp',
        'First Assistant': '1stAsst',
        'Second Assistant': '2ndAsst',
        'Instructor': 'Instr',
        'President': 'Pres',
        'Coordinator': 'Coord',
        'Member': 'Mbr',
        'Meeting': 'Mtg',
        'Committee': 'Cmt',
        'Service': 'Srvc',
        'Quorum': 'Q',
        'Adviser': 'Advsr',
        'Chairman': 'Chair',
        'Stake': 'Stk',
        'Director': 'Dir',
        'Specialist': 'Spec',
        'Activity': 'Actv',
        'Teacher': 'Tchr'
    }
    specific = {
        'Ward Executive Secretary': 'Exct Sec',
        'Ward Assistant Clerk': 'Asst Clerk',
        'Ward Assistant Clerk--Membership': 'Memb Clerk',
        'Ward Assistant Clerk--Finance': 'Fnc Clerk',
        'Assistant Ward Executive Secretary': 'Asst Exct Sec',
        'District Supervisor': 'DS',
        'Committee Member': 'CmtMbr',
        'Compassionate Service Coordinator': 'CSC',
        'Compassionate Service Assistant Coordinator': 'AsstCSC',
        'Asst Sctmstr': '',
        'Executive Officer': 'Scout ExO',
        'Chartered Organization Representative': 'Scout CRO',
        'Youth Committee Member': 'YCM',
        'Sports Coach': 'Coach',
        'Youth Committee': 'YC',
        'Eleven-Year-Old': '11YO',
        'Activity Days': 'AD',
        'Ward Mission Leader': 'WML',
        'Ward Missionary': 'WM',
        'Missionary': 'FTM',
        'Adviser to Young Single Adult Sisters': 'YSA Advsr',
        'Ward Temple and Family History Consultant': 'WT&FHC',
        'Website Administrator': 'Web Admin',
        'High Councilor': 'HC'
    }
    group = {
        'Bishopric': 'Bric',
        'High Priests': 'HP',
        'Home Teaching': 'HT',
        'Elders Quorum': 'EQ',
        'Relief Society': 'RS',
        'Visiting Teaching': 'VT',
        'Young Men': 'YM',
        'Priests Quorum': 'PQ',
        'Teachers Quorum': 'TQ',
        'Deacons Quorum': 'DQ',
        'Scouting': 'Scout',
        'Young Women': 'YW',
        'Sunday School': 'SS',
        'Primary': 'Prim',
        'Young Single Adult': 'YSA'
    }
    custom = {
        'Duty to God': 'DTG',
        'Service Missionary': 'Srvc Mssnry',
        'Salt Lake Foothill Stake': 'SL FH Stk'
    }

    for key, value in custom.items():
        if key in c:
            c = c.replace(key, value)

    for key, value in group.items():
        if key in c:
            c = c.replace(key, value)

    for key, value in specific.items():
        if key in c:
            c = c.replace(key, value)

    for key, value in bulk.items():
        if key in c:
            c = c.replace(key, value)

    return c


if __name__ == "__main__":
    get_sub_orgs_callings()
