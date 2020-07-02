# -*- coding: utf-8 -*-
import struct

MAGIC_USER_ID = 2456938384156277127
HEADER_FORMAT = '>4sBI'
RECORD_FORMAT = '>cIQ' 
DOLLAR_FORMAT = '>d'

HEADER_LENGTH = 9
BASE_LENGTH = 13
DOLLAR_LENGTH = 8

RECORD_TYPES = {
    b'\x00': 'Debit',
    b'\x01': 'Credit',
    b'\x02': 'Start',
    b'\x03': 'End'
    }

class Proto:
    def __init__(self, filename):
        self.filename = filename
        self.parse_file(self.filename)

    def parse_file(self, filename):
        '''parse the given file and output the result'''
        with open(filename, 'rb') as binary_file:
            binary_content = binary_file.read()

        (log_format, version, num_records) = struct.unpack(HEADER_FORMAT, binary_content[0:HEADER_LENGTH])
 
        debit_total = 0
        credit_total = 0
        autopay_start = 0
        autopay_end = 0 
        user_balance = 0

        start_index = 0
        stop_index = 0
        start_index = start_index + HEADER_LENGTH
        
        for record in range(num_records):
            stop_index = start_index + BASE_LENGTH
            (type_raw, timestamp, user_id) = struct.unpack(RECORD_FORMAT, binary_content[start_index:stop_index])
            type = RECORD_TYPES[type_raw]

            start_index = stop_index
            if type in ['Debit', 'Credit']:
                stop_index = start_index + DOLLAR_LENGTH
                dollar_amount = struct.unpack(DOLLAR_FORMAT,binary_content[start_index:stop_index])[0] 
                start_index = stop_index
            
            # print(type + ' ' + str(timestamp) + ' ' + str(user_id) + ' ' + str(dollar_amount))
            if user_id == MAGIC_USER_ID:
                if type in ['Debit', 'Credit']:
                    user_balance = user_balance + dollar_amount
            
            if type == 'Credit':
                credit_total = credit_total + dollar_amount
            elif type == 'Debit':
                debit_total = debit_total + dollar_amount
            elif type == 'Start':
                autopay_start = autopay_start + 1
            elif type == 'End':
                autopay_end = autopay_end + 1
            else:
                print('type error')
                
        print('debit_total: ' + str(debit_total))
        print('credit_total: ' + str(credit_total))
        print('autopay_start: ' + str(autopay_start))
        print('autopay_end: ' + str(autopay_end))
        print('balance: ' + str(user_balance))