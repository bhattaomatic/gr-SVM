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

class prediction_printer(gr.basic_block):
    """
    docstring for block prediction_printer
    """
    def __init__(self, label1, label2, max_samples, threshold):
        gr.basic_block.__init__(self,
            name="prediction_printer",
            in_sig=None,
            out_sig=None)
        self.message_port_register_in(pmt.intern("in"));
        self.set_msg_handler(pmt.intern("in"), self.handler);
        self.max_samples = max_samples
        self.readings = []
        self.threshold = threshold
        self.label1 = label1
        self.label2 = label2

    def handler(self, msg):
        reading = pmt.to_python(pmt.cdr(msg))
        self.readings.append(reading)

        if len(self.readings) == self.max_samples:
            avg = numpy.mean(self.readings)
            if avg < self.threshold:
                print "Average of the blocks are: ", self.label1
                print "Label 1 Avg: ", avg
            else:
                print "Average of the blocks are: ", self.label2
                print "Label 2 Avg: ", avg
            self.readings = []
        
        
        
        
        
