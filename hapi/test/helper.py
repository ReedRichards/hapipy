import os
import json


def get_options():
    filename = 'test_credentials.json'
    path = os.path.join(os.path.dirname(__file__), filename)
    options = {'api_key':'demo'}
    #options = {'access_token':'demooooo-oooo-oooo-oooo-oooooooooooo', 'refresh_token':'e218c2f9-6ca6-11e1-8233-5d869850b536', 'client_id':'78c3b7b1-1b88-11e1-829a-3b413536dd4c'}
    if os.path.exists(path):
        try:
            raw_text = open(path).read()
        except IOError:
            raise Exception, """
                Unable to open '%s' for integration tests.\n
                If this file exists, then you are indicating you want to override the standard 'demo' creds with your own.\n
                However, it is currently inaccessible so that is a problem.""" % filename
        try:
            options = json.loads(raw_text)
        except ValueError:
            raise Exception, """
                '%s' doesn't appear to be valid json!\n
                If this file exists, then you are indicating you want to override the standard 'demo' creds with your own.\n
                However, if I can't understand the json inside of it, then that is a problem.""" % filename

        if not options.get('api_key') and not options.get('hapikey'):
            raise Exception, """
                '%s' seems to have no 'api_key' or 'access_token' specified!\n
                If this file exists, then you are indicating you want to override the standard 'demo' creds with your own.\n
                However, I'll need at least an API key to work with, or it definitely won't work.""" % filename
        options['api_key'] = options.get('api_key') or options.get('hapikey')

    return options
    

