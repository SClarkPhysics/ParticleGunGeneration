from CRABClient.UserUtilities import config
import os
import getpass

config = config()

aMass = "0_5"

pwd = os.getcwd()
usn = getpass.getuser()

#outlfnd = "/store/user/{}/aGun_Generation/a{}".format(usn, aMass) 
outlfnd = "/store/local/aGun_Generation/a{}".format(aMass) 

config.General.requestName = 'aGun_a{}_RAWSIM'.format(aMass)
config.General.workArea = '{}/crab_projects'.format(pwd)

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '{}/StepFiles/step1_aGun_a{}_RAWSIM.py'.format(pwd, aMass)

config.Data.userInputFiles = open('{}/genFiles/genfiles_a{}.txt'.format(pwd, aMass)).readlines()

config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 2 #FIXME

config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = False
config.Data.outputDatasetTag = 'RAWSIM'
config.Data.outputPrimaryDataset = 'aGun_Generation'
config.Data.outLFNDirBase = outlfnd

config.Site.storageSite = 'T3_US_FNALLPC'

