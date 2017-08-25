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
    def __init__(self, label):
        gr.basic_block.__init__(self,
            name="Test",
            in_sig=None,
            out_sig=None)
        self.message_port_register_in(pmt.intern("data"));
        self.set_msg_handler(pmt.intern("data"), self.handler);
        self.label = label
        #print label

    def handler(self, msg):
        # get input from the port
        timestamp = pmt.car(msg)
        x = pmt.to_python(pmt.cdr(msg))
        #print x.shape
        X = x.reshape(1,-1)
        #veclabel = [self.label, 1]
        #print X.shape
        #C = 1 # SVM regularization parameter
        #clf = SVC(kernel= 'linear', verbose=False, C=C)
        #output = clf.fit(X, veclabel)
        cd('/home/abhishek/GNURadio/python_test/gr-SVM/include/models/')
        clf = joblib.load('svm_model.pkl')
        output = clf.predict(X)
        
        print output
        
        
        
        
