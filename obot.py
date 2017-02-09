app_id = ''
app_secret = ''
app_uri = 'http://127.0.0.1:65010/authorize_callback'
app_ua = 'VelvetBot 0.1'
app_scopes = 'account creddits edit flair history identity livemanage modconfig modcontributors modflair modlog modothers modposts modself modwiki mysubreddits privatemessages read report save submit subscribe vote wikiedit wikiread'
app_account_code = ''


import praw
import obot
r = praw.Reddit(obot.app_ua)
r.set_oauth_app_info(obot.app_id, obot.app_secret, obot.app_uri)
r.get_authorize_url("meh", obot.app_scopes, True)