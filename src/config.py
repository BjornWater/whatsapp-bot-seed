"""
    Credentials to connect on Whatsapp Servers.
    (phone number, whatsapp key)

    To extract key use the yowsup-cli (using a python venv with yowsup installed):

    > yowsup-cli registration -C <CountryCode> -r sms -p <Phone Number with Country Code>
    ex.:
    yowsup-cli registration -C 55 -r sms -p 554899998888

    Then whatsapp will send a key via sms to the phone.
    Get that key then run:

    > yowsup-cli registration -C 55 -R <sms-key> -p 554899998888

    status: ok
    kind: free
    > pw: njH+QGBqGXXXXXXXOFa+Wth5riM=
    price: US$0.99
    price_expiration: 1444272405
    currency: USD
    cost: 0.99
    > login: 554899998888
    type: existing
    expiration: 1472404969

    Now just get the login and pw, and replace bellow.

    If have any problem on registragion with yowsup, you can always register with
    https://github.com/mgp25/Chat-API/wiki/Extracting-password-from-device#using-apk

"""
import os, logging

defaults = {
    "WHATSAPP_LOGIN": 31621640081,
    "WHATSAPP_PW":"EIGLqdiC6EhDcLV6y1ktT0tSE2U",
    "WHATSAPP_ADMIN": "",
    "BING_API_KEY": ""
}

auth = ("31621640081","UptWxGXB8WJLgGIvwzXpbq1eVC4=")

# If filter_groups is True, the bot only stays
# at groups that there is at least one admin on it.
# Otherwise will leave instantly if added.
filter_groups = False
admins = [os.environ.get('WHATSAPP_ADMIN', defaults['WHATSAPP_ADMIN']), ]

# Bing API for image search
bing_api = "nwuGCVvu+0VoCfl+9xKssSfEIxTeghMmTJikVY5IU2k"

# Path to download the media requests
# (audio recordings, printscreens, media and youtube videos)
media_storage_path = "/tmp/"

# Session shelve db path
session_db_path = "/tmp/sessions.db"

# Logging configuration.
# By default only logs the command messages.
# If logging_level set to logging.DEBUG, yowsup will log every protocoll message exchange with server.
log_format = '_%(filename)s_\t[%(levelname)s][%(asctime)-15s] %(message)s'
logging_level = logging.INFO
profile_picture = "/home/bjorn/whatsapp/profile.jpg"
status_message = "Arbeit macht frei"