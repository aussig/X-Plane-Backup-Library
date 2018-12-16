#!/usr/bin/python
######################################################################
#
#   Module:  pcrt
#   Version: $Id$
#   Author:  Jeffrey Clement <jclement@bluesine.com>
#   Targets: Win32, Unix
#   Web:     http://jclement.ca/
#
# Python CRT Library.  A really, really simply way to get colored
# output, cursor positioning, etc for Python when an ANSI driver is
# present.
#
# -------------------------------------------------------------------
#
# $Log: pcrt.py,v $
# Revision 1.1.1.1  2003/10/20 18:59:50  jsc
#
#
# -------------------------------------------------------------------
#
# Copyright (c) 2003, Jeffrey Clement All rights reserved. 
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions 
# are met: 
#
# * Redistributions of source code must retain the above copyright notice, 
#   this list of conditions and the following disclaimer. 
# * Redistributions in binary form must reproduce the above copyright 
#   notice, this list of conditions and the following disclaimer in the 
#   documentation and/or other materials provided with the distribution. 
# * Neither the name of the Bluesine nor the names of its contributors 
#   may be used to endorse or promote products derived from this software 
#   without specific prior written permission. 
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED 
# TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR 
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR 
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING 
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import sys

RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4
MAGENTA = 5
CYAN = 6
WHITE = 7

C_ESC=chr(27)

def myPrint(str):
    """
    special print function to not add spaces!  Just writes IO directly
    to stdout.  Required by all below functions so that we don't end up
    with spaces after every command.
    """
    sys.stdout.write(str)
    return str

def fg(clr):
    """
    set the foreground color using DOSish 0-16.  Colors are out
    of order but that's ok.  live with it!
    """
    if clr < 8:
        return myPrint ("%s[%im" % (C_ESC,clr+30))
    else:
        return myPrint ("%s[1,%im" % (C_ESC,clr-8+30))

def bg(clr):
    """
    set the background color using DOSish 0-7 (can not
    use high color backgrounds )  colors are not in dos
    order
    """
    return myPrint ("%s[%im" % (C_ESC,clr+40))

def reset():
    """
    set all color codes and whatnot!  only way to turn of underline!
    """
    return myPrint ("%s[0m" % (C_ESC))

def gotoxy(row,col):
    """
    goto a specific cursor position (1,1) = top left
    """
    return myPrint ("%s[%i,%i" % (C_ESC,row,col))

def clrscr():
    """
    clear the screen and return cursor to top left
    """
    return myPrint ("%s[2J" % C_ESC) + gotoxy(1,1)

def underline():
    """
    turn on underlining
    """
    return myPrint ("%s[4m" % C_ESC)
    
if __name__=='__main__':
    clrscr()                  # clear the screen
    underline()               # turn on underlining
    for i in range(16):       # display all the colors and show of gotoxy
        fg(i)
        gotoxy(i,i)
        print "Color %i" % i
    reset()








