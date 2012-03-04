#
# This file is part of the IMAP Based Online File Storage tool (imofs)
#
# Copyright (c) 2012 by Pavlo Baron (pb[at]pbit[dot]org)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import re
import imaplib
import os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def login(f):
    match = re.search(r"(.+):(.+)@(.+):(\d+)/(.*)", f)
    if match is not None:
        user = match.group(1)
        password = match.group(2)
        host = match.group(3)
        port = match.group(4)

        M = imaplib.IMAP4(host, port)
        if M is not None:
            res = M.login(user, password)
            if res[0] == 'OK':
                return M, match.group(5)

    return None, None

def cp(args):
    M, source = login(args.source)
    r = True
    if M is None:
        M, dest = login(args.dest)
        r = False
        if M is None:
            print "cannot connect to the server"
            exit(1)
    
    if r:
        pass
    else:
        msg = MIMEMultipart()
        msg['From'] = 'santa@northpole.com'
        msg['To'] = 'mrssanta@northpole.com'
        msg['Date'] = formatdate(localtime = True)
        msg['Subject'] = 'file: %s' % args.source
        msg.attach(MIMEText('nada'))
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(args.source, "rb").read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(args.source))
        msg.attach(part)

        M.append(dest, None, None, msg.as_string())

def rm(args):
    print "----"

def mkdir(args):
    M, folder = login(args.file)
    if M is not None:
        if M.create(folder)[0] != 'OK':
            print "cannot create the folder"
            exit(1)
    else:
        print "cannot connect to the server"
        exit(1)
