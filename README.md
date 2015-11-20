# django-sessioninfo

[![Build Status](https://travis-ci.org/arteria/django-sessioninfo.svg?branch=master)](https://travis-ci.org/arteria/django-sessioninfo)

* https://pypi.python.org/pypi/django-sessioninfo
* https://github.com/arteria/django-sessioninfo 

## Quickstart

* Run `pip install sessioninfo`
 
* Add `'sessioninfo'` to your `INSTALLED_APPS`.

In order to activate the Session Admin, set `SHOW_SESSIONS_IN_ADMIN==True` in your project settings.

The management command `kill_sessions` can be used to log out all users at once.
 
## Features

* Give detailled info about the sessions of your users.
* Find users by session key (`utils.get_session_user`)
* Logging out users mechanism.

