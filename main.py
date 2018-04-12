""" Refactor mod1HRTFMOVE2
    Make it my instrument!
    - changed instrument1 to simple sin wave
    - changed motion instrument to have y component too
"""
#  Import packages/libraries
import ctcsound
import wCsOptions
import wCsInstruments
import wCsScore

# Define variables
outCsndFile = "hrtfmove2.csd"
sr = 96000#44100  # audio sample rate,
ksmps = 1   # control rate
nchnls =2   # number of channels

# Create class object instances
cs = ctcsound.Csound()

# Write csnd file
with open(outCsndFile,'w') as f:

    # -- Open Csound synthesizer
    f.write('<CsoundSynthesizer>\n\n')

    # -- Decide on Options
    #wCsOptions.writeCsOptions(f,savePath="hrtfSinVersion.wav")
    wCsOptions.writeCsOptions(f)

    # -- Start creating CsInstruments
    f.write('<CsInstruments>\n\n')
    wCsInstruments.wInstrumentForematter(f,sr,ksmps,nchnls)
    wCsInstruments.sinInstr(f,1,'p4','p5',1,'p3') # sine instr
    wCsInstruments.hrtfMove2ExInstr(f,1,720,0,'p3',-10,0,'p3') #hrtf instr
    f.write('</CsInstruments>\n')

    # -- Start creating CsScore
    f.write('<CsScore>\n\n')
    # function table
    wCsScore.funcTable(f,1, 0, 2**20, 10, [1])
    # verse 1 - named
    f.write('\nm v1\n\n')
    # instrument 1 - http://www.csounds.com/manual/html/ScoreStatements.html
    wCsScore.playNote(f, 1, 0.0, 0.2, [15000, 440.00] )
    wCsScore.playNote(f, 1, 0.2, 0.2, [15000, 466.16])
    wCsScore.playNote(f, 1, 0.4, 0.2, [15000, 493.88 ])
    wCsScore.playNote(f, 1, 0.6, 0.2, [15000, 523.25 ])
    wCsScore.playNote(f, 1, 0.8, 0.2, [15000, 587.33])
    wCsScore.playNote(f, 1, 1.0, 1.5, [15000, 659.25])
    wCsScore.playNote(f, 1, 2.5 ,1.5, [15000, 698.46])
    wCsScore.playNote(f, 1, 4.0, 1.5, [15000, 783.99])
    wCsScore.playNote(f, 1, 5.5, 1.5, [15000, 880.00])
    wCsScore.playNote(f, 1, 7.0, 1.5, [15000, 830.6])
    wCsScore.playNote(f, 1, 8.5, 1.5, [15000, 783.99])
    wCsScore.playNote(f, 1.1, 10.0, 1.5, [7500, 987.77])
    wCsScore.playNote(f, 1.2, 10.0, 1.5, [7500, 783.99])
    wCsScore.playNote(f, 1.1, 11.5, 4.0, [7500, 659.25])
    wCsScore.playNote(f, 1.2, 11.5, 4.0, [7500, 783.99])
    f.write('\n')
    # instrument 10
    wCsScore.playNote(f, 10, '0', 15.5, [])
    f.write('\n')
    # repeat named verse http://www.csounds.com/manual/html/n.html
    f.write('s\nn v1\n\n')
    f.write('e\n</CsScore>\n')

    # -- End writing Csound Synthesizer
    f.write('</CsoundSynthesizer>')

# -- Play Play Csound file
ret = cs.compile_("csound", outCsndFile)
if ret == ctcsound.CSOUND_SUCCESS:
    cs.perform()
    cs.reset()
