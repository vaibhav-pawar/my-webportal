import os
from apps.home import blueprint
from flask import render_template, request, Flask, send_from_directory
from flask_login import login_required
from jinja2 import TemplateNotFound

@blueprint.route('/index')
@login_required
def index():
    return render_template('home/index.html', segment='index')

@blueprint.route('/direction/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None

# Availabilty Report - Daily + Monthly Report
@blueprint.route('/reports/Availabilityreport')
@login_required
def dailyreports():
    filenames = os.listdir('apps/logs/AvailabiltyReports/DailyReports/')
    return render_template('home/downloadavailabilityreport.html', files=filenames)

def dailyreports():
    filenames = os.listdir('apps/logs/AvailabiltyReports/DailyReports/')
    return render_template('home/downloadavailabilityreport.html', files=filenames)

@blueprint.route('/reports/Availabilityreport/<path:filename>')
@login_required
def dailyreport(filename):
    return send_from_directory(
        os.path.abspath('apps/logs/AvailabiltyReports/DailyReports/'),
        filename,
        as_attachment=True
    )

# Download Report of AP Negotating at 100Mbps
@blueprint.route('/reports/download100mbpsnegoreports')
@login_required
def hundreadmbpsreports():
    filenames1 = os.listdir('apps/logs/100mbps/')
    return render_template('home/download100mbpsnegoreports.html', files1=filenames1)
    
@blueprint.route('/reports/download100mbpsnegoreports/<path:filename>')
@login_required
def hundreadmbpsreport(filename1):
    return send_from_directory(
        os.path.abspath('apps/logs/100mbps/'),
        filename1,
        as_attachment=True
    )

# Download Report of AP Negotating at 1Gbps
@blueprint.route('/reports/download1gbpsnegoreports')
@login_required
def onegbpsreports():
    filenames = os.listdir('apps/logs/ap-negotiating-1gbps/')
    return render_template('home/download1gbpsnegoreports.html', files=filenames)
    
@blueprint.route('/reports/download1gbpsnegoreports/<path:filename>')
@login_required
def onegbpsreport(filename):
    return send_from_directory(
        os.path.abspath('apps/logs/ap-negotiating-1gbps/'),
        filename,
        as_attachment=True
    )

# Download Report of High CRC error switchports
@blueprint.route('/reports/downloadcrcerrorreports')
@login_required
def crcreports():
    filenames = os.listdir('apps/logs/CRCerrors/')
    return render_template('home/downloadcrcerrorreports.html', files=filenames)
    
@blueprint.route('/reports/downloadcrcerrorreports/<path:filename>')
@login_required
def crcreport(filename):
    return send_from_directory(
        os.path.abspath('apps/logs/CRCerrors/'),
        filename,
        as_attachment=True
    )

# Download Report of ServierGuestEnabledSites
@blueprint.route('/reports/downloadservierguestenabledsitereports')
@login_required
def servierguestenabledreports():
    filenames = os.listdir('apps/logs/Servier_guest_Enabled_sites/')
    return render_template('home/downloadservierguestenabledsitereports.html', files=filenames)
    
@blueprint.route('/reports/downloadservierguestenabledsitereports/<path:filename>')
@login_required
def servierguestenabledreport(filename):
    return send_from_directory(
        os.path.abspath('apps/logs/Servier_guest_Enabled_sites/'),
        filename,
        as_attachment=True
    )

# Download Report of ServierGuestDisabledSites
@blueprint.route('/reports/downloadservierguestdisabledsitereports')
@login_required
def servierguestdisabledreports():
    filenames = os.listdir('apps/logs/Servier_guest_Disabled_sites/')
    return render_template('home/downloadservierguestdisabledsitereports.html', files=filenames)
    
@blueprint.route('/reports/downloadservierguestdisabledsitereports/<path:filename>')
@login_required
def servierguestdisabledreport(filename):
    return send_from_directory(
        os.path.abspath('apps/logs/Servier_guest_Disabled_sites/'),
        filename,
        as_attachment=True
    )

# Download Report of | Find specific Tags On Switches and Core
@blueprint.route('/reports/downloadtagonswitchesandcorereports')
@login_required
def tagonswitchesandcorereports():
    filenames = os.listdir('apps/logs/Tag-filtering-on-Network-Devices/')
    return render_template('home/downloadtagonswitchesandcorereports.html', files=filenames)
    
@blueprint.route('/reports/downloadtagonswitchesandcorereports/<path:filename>')
@login_required
def tagonswitchesandcorereport(filename):
    return send_from_directory(
        os.path.abspath('apps/logs/Tag-filtering-on-Network-Devices/'),
        filename,
        as_attachment=True
    )

# Download Report of | Tag Filtering on MR or MS devices
@blueprint.route('/reports/downloadtagfilteringonDevicesreports')
@login_required
def tagfilteringonDevicesreports():
    filenames = os.listdir('apps/logs/Tag-filtering-on-Devices/')
    return render_template('home/downloadtagfilteringonDevicesreports.html', files=filenames)
    
@blueprint.route('/reports/downloadtagfilteringonDevicesreports/<path:filename>')
@login_required
def tagfilteringonDevicesreport(filename):
    return send_from_directory(
        os.path.abspath('apps/logs/Tag-filtering-on-Devices/'),
        filename,
        as_attachment=True
    )

# Download Report of | Tag Filtering on Switchports
@blueprint.route('/reports/downloadtagfilteringonswitchportsreports')
@login_required
def tagfilteringonswitchportsreports():
    filenames = os.listdir('apps/logs/Tag-filtering-on-switchports/')
    return render_template('home/downloadtagfilteringonswitchportsreports.html', files=filenames)
    
@blueprint.route('/reports/downloadtagfilteringonswitchportsreports/<path:filename>')
@login_required
def tagfilteringonswitchportsreport(filename):
    return send_from_directory(
        os.path.abspath('apps/logs/Tag-filtering-on-switchports/'),
        filename,
        as_attachment=True
    )

# Download Report of | DFS events detected on AP
@blueprint.route('/reports/downloaddfseventsreports')
@login_required
def dfseventsreports():
    filenames = os.listdir('apps/logs/dfs-events/')
    return render_template('home/downloaddfseventsreports.html', files=filenames)
    
@blueprint.route('/reports/downloaddfseventsreports/<path:filename>')
@login_required
def dfseventsreport(filename):
    return send_from_directory(
        os.path.abspath('apps/logs/dfs-events/'),
        filename,
        as_attachment=True
    )