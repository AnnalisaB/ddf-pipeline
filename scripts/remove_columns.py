#!/usr/bin/env python

import sys
from remove_bootstrap import remove_columns

remove_columns(sys.argv[1],['SCALED_DATA','PREDICT_DATA','DD_PREDICT','DATA_DI_CORRECTED'])
