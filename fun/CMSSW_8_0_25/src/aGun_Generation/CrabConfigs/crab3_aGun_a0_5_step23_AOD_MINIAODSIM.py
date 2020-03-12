from CRABClient.UserUtilities import config
import os
import getpass

config = config()

aMass = "0_5"

pwd = os.getcwd()
usn = getpass.getuser()

outlfnd = "/store/user/{}/aGun_Generation/a{}".format(usn, aMass) 

config.General.requestName = 'aGun_a{}_MINIAODSIM'.format(aMass)
config.General.workArea = '{}/crab_projects'.format(pwd)

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '{}/StepFiles/step23_aGun_a{}_MiniAOD.py'.format(pwd, aMass)

config.Data.userInputFiles = open('{}/rawsimFiles/rawfiles_a{}.txt'.format(pwd, aMass)).readlines()
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 2 #FIXME
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag = 'MINIAOD'
config.Data.outputPrimaryDataset = 'aGun_Generation'
config.Data.outLFNDirBase = outlfnd

config.Site.storageSite = 'T3_US_FNALLPC'

