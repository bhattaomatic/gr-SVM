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

class Training(gr.basic_block):
    """
    docstring for block Training
    """
    def __init__(self, label1, label2):
        gr.basic_block.__init__(self,
            name="Training",
            in_sig=None,
            out_sig=None)
        self.message_port_register_in(pmt.intern("Data1"))
        self.message_port_register_in(pmt.intern("Data2"))
        self.set_msg_handler(pmt.intern("Data1"), self.handle1)
        self.set_msg_handler(pmt.intern("Data2"), self.handle2)
        self.label1 = label1
        self.label2 = label2
        self.general_work()


    def general_work(self):
        print self.handle1
        print self.handle2
        
    
    
    def handle1(self, msg):
        data = pmt.to_python(pmt.cdr(msg))
        #print data
        return data
        
    def handle2(self, msg):
        data = pmt.to_python(pmt.cdr(msg))
        return data
        

