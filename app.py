from flask import Flask, render_template, url_for, request, send_file
from flask_restful import Resource, Api
from twython import Twython
from flask_mysqldb import MySQL
import csv


app = Flask(__name__)
api = Api(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'
 
mysql = MySQL(app)

# routing to the about page
@app.route('/templates/about.html')
def about():
    return render_template('about.html')


#routing to the contact page
@app.route('/templates/contact.html')
def contact():
    return render_template('contact.html')


# planet classroom
@app.route('/', methods=['POST', 'GET'])
def getPC():
    # creating a Twython instance using keys. 
    # keys taken out for security/privacy
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'PlanetClassroom'

    # telling Twitter what username I want to get the data from, and looking them up through their lookup_user method
    users = t.lookup_user(screen_name=names)
    # the fields variable is every piece of Twitter data I want to retrieve. 
    # split the string in order to get the JSON equivalent for each user
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']
            
            followerCount = r['followers_count']
            followingCount=r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']
            

    # returning HTML for that dedicated user, and setting 2 variables to get follower/following count in HTML
    return render_template('pc.html', followers=followerCount, following=followingCount)


# all around the globe
@app.route('/templates/all_globe.html')
def getAATG():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')


    names = 'all_globe'
    
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('all_globe.html', followers=followerCount, following=followingCount)


# cmrubinworld
@app.route('/templates/CMRubinWorld.html')
def getCMRubinWorld():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'cmrubinworld'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('CMRubinWorld.html', followers=followerCount, following=followingCount)


# dee wineceller
@app.route('/templates/deewineceller.html')
def getDeewineceller():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'deewineceller'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('deewineceller.html', followers=followerCount, following=followingCount)


# generation z
@app.route('/templates/GenerationZ.html')
def getGenZ():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'Meet_Gen_Z'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('GenerationZ.html', followers=followerCount, following=followingCount)


# global search
@app.route('/templates/globalsearch4ed.html')
def getGlobalSearch():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'globalsearch4ed'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']
 
    return render_template('globalsearch4ed.html', followers=followerCount, following=followingCount)


# the global search for education
@app.route('/templates/gsinnovation.html')
def getGlobalSearchForEd():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'gsinnovation'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('gsinnovation.html', followers=followerCount, following=followingCount)


# Lifelonglearning4All
@app.route('/templates/Lifelonglearning4All.html')
def getLearning4All():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'learning4_all'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('Lifelonglearning4All.html', followers=followerCount, following=followingCount)


# Millennial Bloggers
@app.route('/templates/MillenialsBlg.html')
def getMillenialsBlg():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'MillenialsBlg'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('MillenialsBlg.html', followers=followerCount, following=followingCount)


# MoeMathTeacher
@app.route('/templates/MoeMathTeacher.html')
def getMoeMathTeacher():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'MoeMathTeacher'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('MoeMathTeacher.html', followers=followerCount, following=followingCount)


# MoreArtsPlease
@app.route('/templates/MoreArtsPlease.html')
def getMoreArtsPlease():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'MoreArtsPlease'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('MoreArtsPlease.html', followers=followerCount, following=followingCount)


# ORB
@app.route('/templates/OrbKnows.html')
def getOrb():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'OrbKnows'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('OrbKnows.html', followers=followerCount, following=followingCount)


# Real Alice
@app.route('/templates/OurRealAlice.html')
def getRealAlice():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'OurRealAlice'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('OurRealAlice.html', followers=followerCount, following=followingCount)


# PatrickScientist
@app.route('/templates/PatrickScientis.html')
def getPatrickScientis():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'PatrickScientis'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('PatrickScientis.html', followers=followerCount, following=followingCount)


# STEAMCulture
@app.route('/templates/STEAMCulture.html')
def getSTEAMCulture():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'STEAMCulture'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('STEAMCulture.html', followers=followerCount, following=followingCount)


# STEMbyThomas
@app.route('/templates/STEMbyThomas.html')
def getSTEMbyThomas():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'STEMbyThomas'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('STEMbyThomas.html', followers=followerCount, following=followingCount)


# TopGlobalTeacherBlog
@app.route('/templates/teachers_global.html')
def getTeachersGlobal():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'teachers_global'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('teachers_global.html', followers=followerCount, following=followingCount)


# harry rubin
@app.route('/templates/vefour.html')
def getVefour():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'vefour'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('vefour.html', followers=followerCount, following=followingCount)


# World of Learners
@app.route('/templates/worldoflearners.html')
def getWorldOfLearners():
    t = Twython(app_key='',
                app_secret='',
                oauth_token='',
                oauth_token_secret='')

    names = 'worldoflearners'
    users = t.lookup_user(screen_name=names)
    fields = "id screen_name name friends_count followers_count".split()
    r = {}
    info = {}
    for entry in users:
        for f in fields:
            r[f] = ""
            r['id'] = entry['id']
            r['screen_name'] = entry['screen_name']
            r['name'] = entry['name']
            r['friends_count'] = entry['friends_count']
            r['followers_count'] = entry['followers_count']

            followerCount = r['followers_count']
            followingCount = r['friends_count']
            userID = r['id']
            screen_name = r['screen_name']
            name = r['name']

    return render_template('worldoflearners.html', followers=followerCount, following=followingCount)

if __name__ == '__main__':
    app.run(debug=True)
