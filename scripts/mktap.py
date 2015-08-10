#!c:\mozilla-build\buildbotve\Scripts\python.exe
# Copyright (c) 2001-2009 Twisted Matrix Laboratories.
# See LICENSE for details.


### Twisted Preamble
# This makes sure that users don't have to set up their environment
# specially in order to run these programs from bin/.
import sys, os, string
if string.find(os.path.abspath(sys.argv[0]), os.sep+'Twisted') != -1:
    sys.path.insert(0, os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]), os.pardir, os.pardir)))
if not hasattr(os, "getuid") or os.getuid() != 0:
    sys.path.insert(0, os.getcwd())
### end of preamble

from twisted.scripts.mktap import run
run()

