
import sys
import os

from Step3QcdHistos_cfg import *

process.dqmSaver.workflow = '/Qcd/CMSSW_'+os.environ['TEST_RELEASE']+'/RECO'
