# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/Generator/python/ayyGunBasic.py --eventcontent RAWSIM --conditions auto:mc --datatier GEN-SIM-RAW --step GEN,SIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --fileout file:EXO-RunIISummer1 --mc --no_exec -n 20 --python_filename ayyGunBasic.py
import FWCore.ParameterSet.Config as cms
import sys, os
import random
from Configuration.StandardSequences.Eras import eras

process = cms.Process('SIM')
process = cms.Process('HLT',eras.Run2_25ns)


# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

nevents = 10

aMass = 0.5
ptMin = 10 * aMass
ptMax = 100 * aMass

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(nevents)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/Generator/python/ayyGunBasic.py nevts:20'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition


foutName = "aGun_a{}_pt{}to{}.root".format(str(aMass).replace(".","_"), str(ptMin).replace(".","_"), str(ptMax).replace(".","_"))

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),

    fileName = cms.untracked.string(foutName),

    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)


# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

process.generator = cms.EDFilter("Pythia8PtGun",
    PGunParameters = cms.PSet(
        AddAntiParticle = cms.bool(False),
        
        ParticleID = cms.vint32(25),

        MinPt = cms.double(ptMin),
        MaxPt = cms.double(ptMax),

        MinEta = cms.double(-3.),
        MaxEta = cms.double(3.),

        MinPhi = cms.double(-3.14159265359),
        MaxPhi = cms.double(3.14159265359)
    ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8_mycmd'),
        pythia8_mycmd = cms.vstring('Higgs:useBSM = off', 
            'HiggsBSM:allH2 = offHiggsBSM:gg2H2 = off', 
            'HiggsBSM:ffbar2H2 =off', 
            'HiggsBSM:gmgm2H2=off', 
            'HiggsBSM:ffbar2H2Z=off', 
            'HiggsBSM:ffbar2H2W=off', 
            'HiggsBSM:ff2H2ff(t:ZZ)=off', 
            'HiggsBSM:ff2H2ff(t:WW)=off', 
            'HiggsBSM:gg2H2ttbar=off', 
            'HiggsBSM:qqbar2H2ttbar=off', 
            '25:m0        = {}'.format(aMass), 
            '25:mMin      = {}'.format(aMass-0.1), 
            '25:mMax      = {}'.format(aMass+0.1),
            '25:mWidth    = 0.01', 
            '25:tau0      = 025:0:bRatio  = 0.0', 
            '25:1:bRatio  = 0.0', 
            '25:2:bRatio  = 0.000', 
            '25:3:bRatio  = 0.00', 
            '25:4:bRatio  = 0.0', 
            '25:5:bRatio  = 0.0', 
            '25:6:bRatio  = 0.0', 
            '25:7:bRatio  = 0.000', 
            '25:8:bRatio  = 0.0', 
            '25:9:bRatio  = 0.0', 
            '25:10:bRatio = 1.00', 
            '25:11:bRatio = 0.00', 
            '25:12:bRatio = 0.0', 
            '25:13:bRatio = 0.0', 
            '25:0:meMode  = 100', 
            '25:1:meMode  = 100', 
            '25:2:meMode  = 100', 
            '25:3:meMode  = 100', 
            '25:4:meMode  = 100', 
            '25:5:meMode  = 100', 
            '25:6:meMode  = 100', 
            '25:7:meMode  = 100', 
            '25:8:meMode  = 100', 
            '25:9:meMode  = 100', 
            '25:10:meMode = 100', 
            '25:11:meMode = 100', 
            '25:12:meMode = 100', 
            '25:13:meMode = 100', 
            '35:m0        = 100', 
            '35:mWidth    = 0.00403', 
            '35:0:bRatio  = 0.0', 
            '35:1:bRatio  = 0.0', 
            '35:2:bRatio  = 0.0', 
            '35:3:bRatio  = 0.0', 
            '35:4:bRatio  = 0.0', 
            '35:5:bRatio  = 0.0', 
            '35:6:bRatio  = 0.0', 
            '35:7:bRatio  = 0.0', 
            '35:8:bRatio  = 0.0', 
            '35:9:bRatio  = 0.0', 
            '35:10:bRatio  = 0.0', 
            '35:11:bRatio  = 0.0', 
            '35:12:bRatio  = 0.0', 
            '35:13:bRatio  = 0.0', 
            '35:14:bRatio  = 0.0', 
            '35:15:bRatio  = 1.0', 
            '35:16:bRatio  = 0.0', 
            '35:17:bRatio  = 0.0', 
            '35:18:bRatio  = 0.0', 
            '35:19:bRatio  = 0.0', 
            '35:20:bRatio  = 0.0', 
            '35:0:meMode  = 100', 
            '35:1:meMode  = 100', 
            '35:2:meMode  = 100', 
            '35:3:meMode  = 100', 
            '35:4:meMode  = 100', 
            '35:5:meMode  = 100', 
            '35:6:meMode  = 100', 
            '35:7:meMode  = 100', 
            '35:8:meMode  = 100', 
            '35:9:meMode  = 100', 
            '35:10:meMode = 100', 
            '35:11:meMode  = 100', 
            '35:12:meMode  = 100', 
            '35:13:meMode  = 100', 
            '35:14:meMode  = 100', 
            '35:15:meMode  = 100', 
            '35:16:meMode  = 100', 
            '35:17:meMode  = 100', 
            '35:18:meMode  = 100', 
            '35:19:meMode  = 100', 
            '35:20:meMode = 100')
    ),
    Verbosity = cms.untracked.int32(0),
    firstRun = cms.untracked.uint32(1),
    psethack = cms.string('a to gamma gamma basic')
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
#process = customisePostLS1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

