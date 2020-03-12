from CRABClient.UserUtilities import config
import os
import getpass

config = config()

aMass = "0_5"

pwd = os.getcwd()
usn = getpass.getuser()

outlfnd = "/store/user/{}/aGun_Generation/a{}".format(usn, aMass) 

config.General.requestName = 'aGun_a{}'.format(aMass)
config.General.workArea = '{}/crab_projects'.format(pwd)

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '{}/GunSafe/aGun_a{}.py'.format(pwd, aMass)

config.Data.outputPrimaryDataset = 'aGun_Generation'

config.Data.outLFNDirBase = outlfnd
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100 #FIXME get these numbers
NJOBS = 2
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = False
config.Data.outputDatasetTag = 'GENSIM'
config.Site.storageSite = 'T3_US_FNALLPC'
