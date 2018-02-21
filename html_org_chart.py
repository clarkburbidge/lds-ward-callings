import copy
import dominate
import os
import pdfkit
from dominate.tags import *
from org_chart import get_callings, fix_date


def get_pages():
    html_files = []
    org_chart = get_callings()
    unit_title = 'Foothill 1st Ward: '
    topnav = div()
    topnav['class'] = 'topnav'
    for org in org_chart:
        filename = org.replace(" ", "_") + '.html'
        topnav += a(org, href='%s' % filename)

    for org in org_chart:
        org_topnav = copy.deepcopy(topnav)
        filename = org.replace(" ", "_") + '.html'
        doc = dominate.document(title='LDS Callings Organization Display')
        with doc.head:
            link(rel='stylesheet', href='style.css')
        for item in org_topnav:
            if item.children[0] == org:
                item['class'] = 'active'
                break
        doc.add(org_topnav)
        with doc:
            h1(unit_title + org)
            for call in org_chart[org]:
                position = call['position']
                name = fix_name(call['name'])
                date = fix_date(call['activeDate'])
                try:
                    unit = call['unitName']
                except KeyError:
                    unit = None
                pos_name_date = get_pos_name_date(position, name, date, unit)
                h2(pos_name_date)
                try:
                    len(call['additionalCallings'])
                except KeyError:
                    pass
                else:
                    for ad_call in call['additionalCallings']:
                        ac_position = ad_call['position']
                        ac_date = fix_date(ad_call['activeDate'])
                        if 'unitName' in ad_call.keys():
                            ac_unit = ad_call['unitName']
                            h4('{0} ({1}) in {2}'.format(ac_position, ac_date, ac_unit))
                        else:
                            h4('{0} ({1})'.format(ac_position, ac_date))
                br()
        with open('html/' + filename, 'w+') as html:
            html.write(str(doc))
        html_files.append('html/' + filename)
    options = {'quiet': ''}
    options['user-style-sheet'] = 'file:///' + os.getcwd() + '\\html\\pdf.css'
    pdfkit.from_file(html_files, 'html\WardCallings.pdf', options=options)


def fix_name(name):
    if name is None:
        name = 'None'
    return name


def get_pos_name_date(pos, name, date, unit):
    if name == 'None':
        pos_name_date = pos + ': ' + name
    elif unit is None:
        pos_name_date = pos + ': ' + name + ' (' + date + ')'
    else:
        pos_name_date = pos + ': ' + name + ' (' + date + ') in the ' + unit
    return pos_name_date

if __name__ == "__main__":
    get_pages()
