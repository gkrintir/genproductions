import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/afs/cern.ch/user/s/sqian/public/updated_ggmm_gridpack.tar.xz'),
    nEvents = cms.untracked.uint32(1),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    generateConcurrently = cms.untracked.bool(True),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

#Link to datacards:
#https://github.com/cms-sw/genproductions/blob/master/bin/Starlight/production/PbPb_5p36TeV/starlight_dimuon.in
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *
generator = cms.EDFilter("Pythia8ConcurrentHadronizerFilter",
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8PSweightsSettingsBlock,
        skip_hadronization = cms.vstring(
            'Photon:ProcessType = 4',
            'Beams:idA = 22',
'Beams:idB = 22',
'Check:event = off',
'PartonLevel:MPI = off',
'Photon:sampleQ2 = off', # Disable kT smearing if needed
'Photon:Wmin force= 0.',
'PartonLevel:ISR = off',
'PartonLevel:MPI = off',
'PartonLevel:Remnants = off',
'ProcessLevel:ResonanceDecays = off',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings','pythia8PSweightsSettings','skip_hadronization')
    ),
    comEnergy = cms.double(5362.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(100),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


