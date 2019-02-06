#!/usr/bin/env python
# -*- coding: utf-8 -*-
############################################################################################################################################################################
#  ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄     ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄
# ▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌   ▐░░░░░░░░░░░▌▐░▌       ▐░▌
# ▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀    ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌
# ▐░▌       ▐░▌    ▐░▌          ▐░▌     ▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌             ▐░▌       ▐░▌▐░▌       ▐░▌
# ▐░█▄▄▄▄▄▄▄█░▌    ▐░▌          ▐░▌     ▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▄▄▄▄▄▄▄▄    ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
# ▐░░░░░░░░░░▌     ▐░▌          ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌▐░░░░░░░░▌   ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
# ▐░█▀▀▀▀▀▀▀█░▌    ▐░▌          ▐░▌     ▐░▌   ▀   ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌▐░▌ ▀▀▀▀▀▀█░▌   ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀
# ▐░▌       ▐░▌    ▐░▌          ▐░▌     ▐░▌       ▐░▌          ▐░▌▐░▌       ▐░▌   ▐░▌               ▐░▌
# ▐░█▄▄▄▄▄▄▄█░▌▄▄▄▄█░█▄▄▄▄      ▐░▌     ▐░▌       ▐░▌ ▄▄▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌ ▄ ▐░▌               ▐░▌
# ▐░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌▐░▌               ▐░▌
#  ▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀  ▀                 ▀
#
############################################################################################################################################################################
#  pip install redis pycrypto
import sys
import os
import pdb
import json
import uuid
import datetime
import shelve
import redis

try:
    from Crypto.PublicKey import RSA
    from Crypto import Random
except:
    print('[ERROR] you need: pip install pycrypto')
    raise

############################################################################################################################################################################
#  ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
# ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
# ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀
# ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌
# ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄
# ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
# ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀  ▀▀▀▀▀▀▀▀▀█░▌
# ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌          ▐░▌     ▐░▌            ▐░▌
# ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌  ▄▄▄▄▄▄▄▄▄█░▌
# ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
#  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀
############################################################################################################################################################################


def isprintable(s, codec='utf8'):
    """ returns true if s is printable; used to test if decryption was successful """
    try:
        s.decode(codec)
    except UnicodeDecodeError:
        return False
    return True


def color(string, code):
    """Return with the colorer string accroding to color code if coloring is
    enabled, or the original string otherwise. Color is one of the colors
    define in the following dictionary (using ANSI codes):
    """
    colors = {
        'normal':       '0',
        'bold':         '1',
        'cyan':         '0;36',
        'bold-cyan':    '1;36',
        'red':          '0;31',
        'bold-red':     '1;31',
        'green':        '0;32',
        'bold-green':   '1;32',
        'yellow':       '0;33',
        'bold-yellow':  '1;33',
        'blue':         '0;34',
        'bold-blue':    '1;34',
        'gray':         '1;30',
    }

    col = colors.get(code)
    if col:
        return '\033[%sm%s\033[0m' % (col, str(string))
    return str(string)


def get_local_uuid_for_key(identifier):
    """ compute the key redis needs for client side """
    return ':'.join(map(str, (
        'bitmsg.py',
        'V1',
        COMPUTER_UUID,
        PARENT_PID,  # parent pid
        identifier,
    )))

############################################################################################################################################################################
#  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
# ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
# ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀
# ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌               ▐░▌     ▐░▌       ▐░▌▐░▌▐░▌    ▐░▌     ▐░▌     ▐░▌
# ▐░▌          ▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄
# ▐░▌          ▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌
# ▐░▌          ▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌     ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌
# ▐░▌          ▐░▌       ▐░▌▐░▌    ▐░▌▐░▌          ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌    ▐░▌▐░▌     ▐░▌               ▐░▌
# ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌ ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌▐░▌     ▐░▐░▌     ▐░▌      ▄▄▄▄▄▄▄▄▄█░▌
# ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░▌      ▐░░▌     ▐░▌     ▐░░░░░░░░░░░▌
#  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀         ▀  ▀        ▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀
############################################################################################################################################################################


COMPUTER_UUID = hex(uuid.getnode())
SERVER_MSG_POOL_KEY = '_server_msg_pool_ka2wxp'
NO_NEW_MESSAGES = '\n* There are no messages\n'
FOUND_NEW_MESSAGES = '\n* You have {} message(s)\n'
PARENT_PID = os.getppid()


############################################################################################################################################################################
#  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄
# ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌
# ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀
# ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌               ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌
# ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌▐░▌               ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄
# ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░▌               ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌
# ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌▐░▌               ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌ ▀▀▀▀▀▀▀▀▀█░▌
# ▐░▌          ▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌               ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░▌    ▐░▌▐░▌          ▐░▌
# ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌      ▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌ ▄▄▄▄▄▄▄▄▄█░▌
# ▐░▌          ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌
#  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀
############################################################################################################################################################################

def gen_addr():
    """ generate and return a new public/private key pair """
    random_generator = Random.new().read
    private_key = RSA.generate(2048, random_generator)
    return private_key.publickey().exportKey('PEM'), private_key.exportKey('PEM')


def get_user_feedback(msg):
    """ prompt user for single line text input """
    print(msg)
    print color('(bitmsg) ', 'green'),
    return sys.stdin.readline().strip()


def make_safe_filename(s):
    def safe_char(c):
        if c.isalnum():
            return c
        else:
            return "_"
    return "".join(safe_char(c) for c in s).rstrip("_")


def get_user_multiline_feedback(msg):
    """ prompt user for multiple lines of text, must be exited with ctrl+d """
    print(msg)
    print('Ctrl-D to save')

    contents = []
    while True:
        try:
            line = raw_input("")
        except EOFError:
            break
        contents.append(line)

    return '\n'.join(contents)


def download_enc_messages():
    """ return all messages from server pool """
    ret = redis_server.lrange(SERVER_MSG_POOL_KEY, 0, -1)
    # print('[DEBUG] downloaded {} encrypted messages from server pool'.format(len(ret)))
    return ret[::-1]  # sort by date


def attempt_read_messages(enc_messages, user):
    """ try to decrypt every message in the pool """

    # nothing to do
    if not enc_messages:
        return []

    print('[DEBUG] checking entire pool of {} messages, this can take awhile...'.format(len(enc_messages)))
    key = RSA.importKey(user['priv'])

    ret = []
    for message in enc_messages:
        # attempt decryption
        try:
            check = key.decrypt(message)
            if check and isprintable(check):
                ret.append(check.strip())
        except Exception as e:
            # print('[DEBUG] failed to dec message, error was: {}'.format(e))
            pass

    # print('[DEBUG] {} messages were read successfully'.format(len(ret)))
    return ret


def lookup_my_local_user():
    key = get_local_uuid_for_key('username')
    try:
        user_data = json.loads(local_store.get(key))
    except (ValueError, TypeError):
        # json syntax error, or no data
        user_data = None

    return user_data


def create_user_account():
    print('You do not have an account. We will now create one.')

    un = get_user_feedback('Enter a username: ')
    if not un:
        raise ValueError('failed to enter a valid username during registration')

    user_key = get_local_uuid_for_key('username')
    pub, priv = gen_addr()

    user_data = {
        'un': un,
        'pub': pub,
        'priv': priv,
    }

    local_store[user_key] = json.dumps(user_data)

    print('\nWelcome {}! A keypair has been generated for you.'.format(un))
    print('To reach you, users must send messages to address: \n\n{}\n'.format(pub))
    print('Please externally exchange this with users with whom you wish to pseudo-securely communicate\n')

    return user_data


def get_address_book():
    key = get_local_uuid_for_key('address_book')
    try:
        address_book = json.loads(local_store.get(key))
    except (ValueError, TypeError):
        # json syntax error, or no data
        address_book = []
    return address_book


############################################################################################################################################################################
#  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
# ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
# ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀
# ▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌▐░▌               ▐░▌     ▐░▌               ▐░▌     ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌          ▐░▌
# ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░▌          ▐░█▄▄▄▄▄▄▄▄▄
# ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌          ▐░░░░░░░░░░░▌
# ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀  ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌          ▐░█▀▀▀▀▀▀▀▀▀
# ▐░▌          ▐░▌          ▐░▌     ▐░▌            ▐░▌     ▐░▌               ▐░▌     ▐░▌     ▐░▌          ▐░▌    ▐░▌▐░▌▐░▌          ▐░▌
# ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌  ▄▄▄▄▄▄▄▄▄█░▌ ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄
# ▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
#  ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀
############################################################################################################################################################################

local_store = shelve.open(make_safe_filename('.local.{}.shelf'.format(get_local_uuid_for_key('lstore'))))

try:
    redis_server = redis.Redis(host='172.20.3.176', port=6379, db=1)
except:
    print('[ERROR] unable to connect to remote redis, you may need lagu-wifi, non-public')
    raise


############################################################################################################################################################################
# ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
#▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
#▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀
#▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌
#▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌          ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄
#▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌          ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
#▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀█░█▀▀ ▐░▌       ▐░▌▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀█░▌
#▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌                    ▐░▌
#▐░▌          ▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌
#▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
# ▀            ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀
############################################################################################################################################################################

def add_to_address_book(username, pubkey):
    current_book = get_address_book()
    current_book.append({
        'un': username,
        'pub': pubkey,
    })
    # write new entry
    key = get_local_uuid_for_key('address_book')
    local_store[key] = json.dumps(current_book)


def prompt_send_message(user):

    who = None

    address_book = get_address_book()
    if address_book:
        print('\nWould you like to message one of the users in your address book?')
        print('Enter a number to select a user, or Enter to add a new user\n')

        for idx, user_data in enumerate(address_book):
            alias = user_data['un']
            print('{} {}'.format(
                color(str(idx + 1)+'.', 'bold-blue'),
                alias,
            ))

        selected_idx = get_user_feedback('\n')
        try:
            who = address_book[int(selected_idx) - 1]['pub']
        except (TypeError, ValueError):
            # user skipped selection
            pass

    if not who:
        who = get_user_multiline_feedback('\nPlease enter the user address {} to send to:'.format(color('(PUBKEY)', 'bold')))

        # do we already have a address entry for them that just wasnt selected?
        if who not in {x['un'] for x in address_book}:

            add_them = get_user_feedback('\nThis user is not in your address book. Would you like to add them? (y/n)')
            if add_them.lower() == 'y':
                entered_name = get_user_feedback('\nPlease enter a name for this contact:')

                add_to_address_book(username=entered_name, pubkey=who)

    if who:
        msg = get_user_feedback('\nPlease enter the message:')
        if msg:
            print('ok. we will send\n\n\t{}\n\nto this address.\n'.format(msg))

            # inject sender info
            msg = '{header}\nFrom: {sender}\nDate: {date}\n{header}\n{message}'.format(
                header='-'*26,
                sender='N/A',
                date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %z"),
                message=msg,
            )

            # sometimes who has this weird byte, remove it if it exists
            who = who.strip('\x01')

            enc_message = RSA.importKey(who).encrypt(msg, 33)[0]

            publish_msg_to_server(enc_message)


def show_menu(user):
    """ return value of False means we should exit program """

    print('######## MAIN MENU ########')
    print('1. Send Message')
    print('2. Check Messages')
    print('3. Print My Address')
    print('4. Quit')
    print('###########################')
    try:
        check = int(str(get_user_feedback('\nPlease choose an option (1-4): \n')))
    except (ValueError, TypeError):
        # just quit on bad user value
        check = 4

    if check == 1:
        # send msg
        prompt_send_message(user)
        print('\n')
    elif check == 2:
        # check msg
        check_for_messages(user)
        print('\n')

    elif check == 3:
        # print addr
        print('Users may send you messages at:\n\n{}\n\n'.format(user['pub']))
        print('\n')
    else:
        # exit
        print('\n')
        return False

    return True


def check_for_messages(user):
    my_messages = attempt_read_messages(download_enc_messages(), user)
    if my_messages:
        print(FOUND_NEW_MESSAGES.format(len(my_messages)))
        for idx, message in enumerate(my_messages):
            idx_str = str(idx + 1).zfill(3)
            print(color('<BEGIN_MESSAGE_{}>'.format(idx_str), 'gray'))
            print('{msg}\n'.format(
                msg=message,
            ))
            # print(color('<END_MESSAGE_{}>\n'.format(idx_str), 'gray'))
    else:
        print(NO_NEW_MESSAGES)


def publish_msg_to_server(msg):
    if not msg:
        raise ValueError
    pool_count = redis_server.lpush(SERVER_MSG_POOL_KEY, msg)
    redis_server.expire(SERVER_MSG_POOL_KEY, 604800)  # expire pool after one week of inactivity
    print('A message has been published! Currently {} messages exist in pool.'.format(pool_count))


def main():

    # we are connected
    print('Connected to server {}, in channel {}\n'.format(
        color('172.20.3.176', 'green'),
        color('General Chat', 'green'),
    ))

    # lookup a saved account
    local_user = lookup_my_local_user()

    if local_user:
        # greet user
        print('Welcome back {}!'.format(local_user['un']))
    else:
        # register user locally
        local_user = create_user_account()

    check_for_messages(local_user)

    while 1:
        if show_menu(local_user) is False:
            break



if __name__ == '__main__':
    main()
    local_store.close()
    print('Goodbye!\n')
