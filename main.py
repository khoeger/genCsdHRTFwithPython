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
sr = 44100  # audio sample rate,
kr = 4410   # control rate
nchnls =2   # number of channels

# Create class object instances
cs = ctcsound.Csound()

# Write csnd file
with open(outCsndFile,'w') as f:

    # Open Csound synthesizer
    f.write('<CsoundSynthesizer>\n\n')

    # Decide on Options
    wCsOptions.writeCsOptions(f)

    # Start creating CsInstruments
    f.write('<CsInstruments>\n\n')
    wCsInstruments.wInstrumentForematter(f,sr,kr,nchnls)
    wCsInstruments.sinInstr(f,1,'p4','p5',1) # sine instr
    wCsInstruments.hrtfMove2ExInstr(f,1,720,0,'p3',-10,0,'p3') #hrtf instr
    f.write('</CsInstruments>\n')

    # Start creating CsScore
    f.write('<CsScore>\n\n')
    wCsScore.funcTable(f,1, 0, 16384, 10, [1])  # wavetable
    wCsScore.playNote(f, 1, 0, 0.2, [15000, 440.00] )
    #f.write('i1 0 .2 15000 440.00 \n')          # instrument 1
    f.write('i1 + .2 15000 466.16 \n')
    f.write('i1 + .2 15000 493.88 \n')
    f.write('i1 + .2 15000 523.25 \n')
    f.write('i1 + .2 15000 587.33 \n')
    f.write('i1 + 1.5 15000 659.25 \n')
    f.write('i1 + 1.5 15000 698.46 \n')
    f.write('i1 + 1.5 15000 783.99 \n')
    f.write('i1 + 1.5 15000 880.00 \n')
    f.write('i1 + 1.5 15000 830.61 \n')
    f.write('i1 + 1.5 15000 783.99 \n')
    f.write('i1 + 1.5 15000 987.77 \n')
    f.write('i1 + 4 15000 659.25\n\n')

    f.write('; Play Instrument 10 for 10 seconds.\n')
    f.write('i10 0 15\n\n')

    f.write('</CsScore>\n')
    f.write('</CsoundSynthesizer>')

# Play Play Csound file
#Csoundfile = "cSoundBook\\ambisonicsBinaural\\hrtfmove2_example_44100.csd"
ret = cs.compile_("csound", outCsndFile)
if ret == ctcsound.CSOUND_SUCCESS:
    cs.perform()
    cs.reset()
