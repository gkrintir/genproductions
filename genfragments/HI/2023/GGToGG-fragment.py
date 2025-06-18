import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/afs/cern.ch/work/g/gkrintir/private/lbyl_Run3/CMSSW_14_1_7/src/GGToGG_madgraphLO_el8_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    generateConcurrently = cms.untracked.bool(True),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

#Link to datacards:
#https://github.com/cms-sw/genproductions/blob/master/bin/UPCgen/production/PbPb_5p36TeV/upcgen_LbyL.in

generator = cms.EDFilter("Pythia8ConcurrentHadronizerFilter",
    PythiaParameters = cms.PSet(
        skip_hadronization = cms.vstring(
            'ProcessLevel:all = off',
            'Check:event = off'
        ),
        parameterSets = cms.vstring('skip_hadronization')
    ),
    comEnergy = cms.double(5362.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)

ProductionFilterSequence = cms.Sequence(generator)

phophogenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinEt = cms.untracked.vdouble(1.0, 1.0.),
    MaxEta = cms.untracked.vdouble(3.5, 3.5),
    MinEta = cms.untracked.vdouble(-3.5, -3.5),
    ParticleCharge = cms.untracked.int32(0),
    ParticleID1 = cms.untracked.vint32(22),
    ParticleID2 = cms.untracked.vint32(22)
)

ProductionFilterSequence = cms.Sequence(generator*phophogenfilter)
