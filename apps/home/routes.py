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

@blueprint.route('/reports/Availabilityreport')
@login_required
def dailyreports():
    filenames = os.listdir('apps/logs/AvailabiltyReports/DailyReports/')
    return render_template('home/downloadavailabilityreport.html', files=filenames)

def monthlyreports():
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

def monthlyreport(filename):
    return send_from_directory(
        os.path.abspath('apps/logs/AvailabiltyReports/DailyReports/'),
        filename,
        as_attachment=True
    )