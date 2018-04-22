""" Refactor mod1HRTFMOVE2
    Make it my instrument!
    - changed instrument1 to simple sin wave
    - changed motion instrument to have y component too
"""
#  Import packages/libraries
import ctcsound
import numpy as np
import pandas as pd

import csScoreToPython
import wCsOptions
import wCsInstruments
import wCsScore



# Define variables
readFileName = "cabs_CsScore_v2.cs"
outCsndFile = "hrtfmove2.csd"
sr = 96000#44100  # audio sample rate,
ksmps = 1   # control rate
nchnls =2   # number of channels

tempo = 120
stftOverlaps = 4
headRadius = 8.15 #cm

fTableSize = 2**20

# Create class object instances
cs = ctcsound.Csound()

# Write csnd file
with open(outCsndFile,'w') as f:

    # -- Open Csound synthesizer
    f.write('<CsoundSynthesizer>\n\n')

    # -- Decide on Options
    #wCsOptions.writeCsOptions(f,savePath="movingSound_4_19_2018.wav")
    wCsOptions.writeCsOptions(f)

    # -- Start creating CsInstruments
    f.write('<CsInstruments>\n\n')

    wCsInstruments.wInstrumentForematter(f,sr,ksmps,nchnls)
    """
    f.write('massign 1, 1\n')
    f.write('massign 2, 1\n')
    f.write('massign 3, 1\n')
    f.write('massign 4, 1\n')
    f.write('massign 5, 1\n')
    f.write('massign 6, 1\n')
    f.write('massign 7, 1\n')
    f.write('massign 8, 1\n\n')"""

    wCsInstruments.sinInstr(f, 1,'p4','p5',1,'p3') # sine instr
    wCsInstruments.sinInstr(f, 2,'p4','p5',1,'p3')
    wCsInstruments.sinInstr(f, 3,'p4','p5',1,'p3')
    wCsInstruments.sinInstr(f, 4,'p4','p5',1,'p3')
    wCsInstruments.sinInstr(f, 5,'p4','p5',1,'p3')
    wCsInstruments.sinInstr(f, 6,'p4','p5',1,'p3')
    wCsInstruments.sinInstr(f, 7,'p4','p5',1,'p3')
    wCsInstruments.sinInstr(f, 8,'p4','p5',1,'p3')
    wCsInstruments.hrtfMove2ExInstr(f, 1, 720, 0, 'p3', -1000, 0, 'p3',
                                    sr, stftOverlaps, headRadius) #hrtf instr
    f.write('</CsInstruments>\n')

    # -- Start creating CsScore
    f.write('<CsScore>\n\n')
    # function table
    wCsScore.funcTable(f,1, 0, fTableSize, 10, [1])
    # verse 1 - named
    #f.write('\nm v1\n\n')
    f.write('\nt 0 '+str(tempo)+'\n\n')
    scoreLines = csScoreToPython.readScore(readFileName)
    npScoreLines = np.asarray(scoreLines)
    scoreDF = pd.DataFrame(npScoreLines,
                            columns = [ 'instrument number',
                                        'start time',
                                        'duration',
                                        'pitch',
                                        'note velocity'])
    #print(scoreDF[:10])
    for index, entry in scoreDF.iterrows():
        wCsScore.playNote(f,
                          entry['instrument number'],
                          entry['start time'],
                          entry['duration'],
                          [8000, entry['pitch']])
    """
    # instrument 1 - http://www.csounds.com/manual/html/ScoreStatements.html
    wCsScore.playNote(f, 1, 0.0, 0.2, [8000, 440.00] )
    wCsScore.playNote(f, 1, 0.2, 0.2, [8000, 466.16])
    wCsScore.playNote(f, 1, 0.4, 0.2, [8000, 493.88 ])
    wCsScore.playNote(f, 1, 0.6, 0.2, [8000, 523.25 ])
    wCsScore.playNote(f, 1, 0.8, 0.2, [8000, 587.33])
    wCsScore.playNote(f, 1, 1.0, 1.5, [8000, 659.25])
    wCsScore.playNote(f, 1, 2.5 ,1.5, [8000, 698.46])
    wCsScore.playNote(f, 1, 4.0, 1.5, [8000, 783.99])
    wCsScore.playNote(f, 1, 5.5, 1.5, [8000, 880.00])
    wCsScore.playNote(f, 1, 7.0, 1.5, [8000, 830.6])
    wCsScore.playNote(f, 1, 8.5, 1.5, [8000, 783.99])
    wCsScore.playNote(f, 1.1, 10.0, 1.5, [4000, 987.77])
    wCsScore.playNote(f, 1.2, 10.0, 1.5, [4000, 783.99])
    wCsScore.playNote(f, 1.1, 11.5, 4.0, [2000, 659.25])
    wCsScore.playNote(f, 1.2, 11.5, 4.0, [2000, 783.99])
    """
    f.write('\n')
    # instrument 10
    wCsScore.playNote(f, 10, '0', 75, [])
    f.write('\n')
    # repeat named verse http://www.csounds.com/manual/html/n.html
    #f.write('s\nn v1\n\n')
    f.write('e\n</CsScore>\n')

    # -- End writing Csound Synthesizer
    f.write('</CsoundSynthesizer>')

# -- Play Play Csound file
ret = cs.compile_("csound", outCsndFile)
if ret == ctcsound.CSOUND_SUCCESS:
    cs.perform()
    cs.reset()
