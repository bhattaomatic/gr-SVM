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
from sklearn.svm import SVC
from sklearn.externals import joblib
from sh import cd

class Test(gr.basic_block):
    """
    docstring for block Test
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="Test",
            in_sig=None,
            out_sig=None)
        self.message_port_register_out(pmt.intern("out"));
        self.message_port_register_out(pmt.intern("timestamp"));
        self.message_port_register_in(pmt.intern("data"));
        self.set_msg_handler(pmt.intern("data"), self.handler);


    def handler(self, msg):
        # get input from the port
        timestamp = pmt.car(msg)
        x = pmt.to_python(pmt.cdr(msg))
        cd('/home/abhishek/Git/gr-SVM/include/models/')
        mean = joblib.load('mean.pkl')
        standarddev = joblib.load('std.pkl')
        x = (x - mean)/standarddev
        X = x.reshape(1,-1)
        clf = joblib.load('svm_model.pkl')
        output = clf.predict(X)
        self.message_port_pub(pmt.intern("out"), pmt.cons(pmt.PMT_NIL, pmt.to_pmt(output)))
        self.message_port_pub(pmt.intern("timestamp"), pmt.cons(timestamp, pmt.PMT_NIL))

        
        
        
        
