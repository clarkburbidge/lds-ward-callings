from sub_orgs import abr_call, arrange_name, get_sub_orgs_callings
import creds


def get_callings():
    import json
    import lds_org
    with lds_org.session(creds.usr, creds.pwd) as lds:
        rv = lds.get('callings-with-dates')
        members = get_members_callings(rv)
        sub_orgs = get_sub_orgs_callings()
        org_chart = get_org_chart(rv, members)
        org_chart = merge_dicts(sub_orgs, org_chart)
    # with open('C:\\Dev\\Python\\LDSIO\\json_formats\\org_chart_dict.json', 'w+') as f1:
    #     json.dump(org_chart, f1, indent=4)
    return org_chart


def get_members_callings(rv):
    members = {}
    for member in rv.json():
        id = member['id']
        name = member['name']
        position = member['position']
        positionId = member['positionId']
        activeDate = member['activeDate']
        calling = {'position': position,
                   'positionId': positionId,
                   'activeDate': activeDate
                   }
        if member['stake']:
            calling['stake'] = 'Stake'
        if member['outOfUnit']:
            calling['unitName'] = member['unitName']
        if id in members:
            members[id].append(calling)
        else:
            members[id] = [calling]
    return members


def get_org_chart(rv, members):
    import operator
    import collections
    orgs = collections.OrderedDict()
    orgs['Bishopric'] = 'displaySequence'
    orgs['High Priests Group'] = 'displaySequence'
    orgs['Elders Quorum'] = 'displaySequence'
    orgs['Relief Society'] = 'displaySequence'
    orgs['Young Men'] = 'displaySequence'
    orgs['Young Women'] = 'displaySequence'
    orgs['Sunday School'] = ['displaySequence', 'subOrgId']
    orgs['Primary'] = ['displaySequence', 'subOrgId']
    orgs['Ward Missionaries'] = 'displaySequence'
    orgs['Full-Time Missionaries'] = 'displaySequence'
    orgs['Additional Callings'] = 'position'

    extra = collections.OrderedDict()
    extra['Stake'] = 'stake'
    extra['Out of Unit'] = 'outOfUnit'

    org_chart = collections.OrderedDict()
    for org, sort_crit in orgs.items():
        org_list = []
        for member in rv.json():
            if member['organization'] == org and not member['outOfUnit']:
                id = member['id']
                name = member['name']
                position = member['position']
                positionId = member['positionId']
                positionTypeId = member['positionTypeId']
                activeDate = member['activeDate']
                displaySequence = member['displaySequence'] if type(member['displaySequence']) is int else 9999
                subOrgId = member['subOrgId'] if type(member['subOrgId']) is int else 9999999
                subOrgTypeId = member['subOrgTypeId']
                calling = {'name': name,
                           'position': position,
                           'activeDate': activeDate,
                           'displaySequence': displaySequence,
                           'subOrgId': subOrgId,
                           'subOrgTypeId': subOrgTypeId,
                           'positionId': positionId,
                           'positionTypeId': positionTypeId,
                           'additionalCallings': additional_callings(members, id, positionId)
                           }
                org_list.append(calling)
        if type(sort_crit) is list:
            org_chart[org] = sorted(org_list, key=operator.itemgetter(sort_crit[0], sort_crit[1]))
        else:
            org_chart[org] = sorted(org_list, key=operator.itemgetter(sort_crit))

    for org, match in extra.items():
        org_list = []
        for member in rv.json():
            if member[match]:
                id = member['id']
                name = member['name']
                position = member['position']
                unitName = member['unitName']
                positionId = member['positionId']
                positionTypeId = member['positionTypeId']
                activeDate = member['activeDate']
                displaySequence = member['displaySequence']
                subOrgId = member['subOrgId']
                subOrgTypeId = member['subOrgTypeId']
                calling = {'name': name,
                           'position': position,
                           'activeDate': activeDate,
                           'unitName': unitName,
                           'displaySequence': displaySequence,
                           'subOrgId': subOrgId,
                           'subOrgTypeId': subOrgTypeId,
                           'positionId': positionId,
                           'positionTypeId': positionTypeId,
                           'additionalCallings': additional_callings(members, id, positionId)
                           }
                org_list.append(calling)
        org_chart[org] = org_list

    return org_chart


def merge_dicts(sub_orgs, org_chart):
    for org in sub_orgs:
        for call in sub_orgs[org]:
            if call['position'] not in [pos['position'] for pos in org_chart[org]]:
                org_chart[org].append(call)
    return org_chart


def print_org_cart(org_chart):
    for org in org_chart:
        print('\n{0}\n{1}'.format(org, '-------------------------------------'))
        for call in org_chart[org]:
            # position = abr_call(call['position'])
            position = call['position']
            name = call['name']
            date = fix_date(call['activeDate'])
            if 'unitName' in call.keys():
                # unit = abr_call(call['unitName'])
                unit = call['unitName']
                print('{0} - {1}:'.format(position, unit))
            else:
                print('{0}:'.format(position))
            print('\t{0} ({1})'.format(name, date))
            try:
                len(call['additionalCallings'])
            except KeyError:
                pass
            else:
                for calling in call['additionalCallings']:
                    # ac_position = abr_call(calling['position'])
                    ac_position = calling['position']
                    ac_date = fix_date(calling['activeDate'])
                    if 'unitName' in calling.keys():
                        # ac_unit = abr_call(calling['unitName'])
                        ac_unit = calling['unitName']
                        print('\t\t{0} ({1}) in {2}'.format(ac_position, ac_date, ac_unit))
                    else:
                        print('\t\t{0} ({1})'.format(ac_position, ac_date))


def additional_callings(members, id, positionId):
    ad_callings = []
    for memberID, callings in members.items():
        if id == memberID:
            for call in callings:
                if call['positionId'] != positionId:
                    ad_callings.append(call)
            break
    return ad_callings


def fix_date(d):
    try:
        year = d[:4]
        month = d[5:7]
        d = year + '/' + month
    except TypeError:
        pass
    return d


if __name__ == "__main__":
    get_callings()
