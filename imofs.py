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

import argparse
import imap

def main():
    args = parsearg()
    args.subcommand(args)

def parsearg():
    parser = argparse.ArgumentParser(description='imofs - IMAP Based Online File Storage')
    sub = parser.add_subparsers(title='commands', help='Remote path format is user:password@host:port')

    cp = sub.add_parser('cp', help="copy a file in whatever direction")
    cp.add_argument('source', metavar='SOURCE', type=str, help='Source file path')
    cp.add_argument('dest', metavar='DEST', type=str, help='Destination path')
    cp.set_defaults(subcommand = lambda args: imap.cp(args))

    rm = sub.add_parser('rm', help='remove an online file')
    rm.add_argument('file', metavar='FILE', type=str, help='Full file path to remove')
    rm.set_defaults(subcommand = lambda args: imap.rm(args))

    mkdir = sub.add_parser('mkdir', help='create an online folder')
    mkdir.add_argument('file', metavar='FILE', type=str, help='Folder name')
    mkdir.set_defaults(subcommand = lambda args: imap.mkdir(args))

    parser.add_argument('-v', '--version', action='version',
                        version='imofs 0.0.1', help="prints the current program version")

    return parser.parse_args()

if __name__ == "__main__":
    main()
