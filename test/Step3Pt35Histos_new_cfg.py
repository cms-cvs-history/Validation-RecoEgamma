
import sys
import os

from Step3Pt35Histos_cfg import *

process.dqmSaver.workflow = '/Pt35/CMSSW_'+os.environ['TEST_RELEASE']+'/RECO'
