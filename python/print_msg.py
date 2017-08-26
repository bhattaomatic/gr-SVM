#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
import pmt

class print_msg(gr.basic_block):
    """
    docstring for block print_msg
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="print_msg",
            in_sig=None,
            out_sig=None)
        self.message_port_register_in(pmt.intern("in"));
        self.set_msg_handler(pmt.intern("in"), self.handler);

    def handler(self, msg):
        meta = pmt.car(msg)
        data = pmt.cdr(msg)
        print data
        
