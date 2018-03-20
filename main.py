""" Refactor mod1HRTFMOVE2
    Make it my instrument!
    - changed instrument1 to simple sin wave
    - changed motion instrument to have y component too
"""
#  Import packages/libraries
import ctcsound

# Define variables
outCsndFile = "2_Hrtfmove2.csd"

# Create class object instances
cs = ctcsound.Csound()

# Write csnd file
with open(outCsndFile,'w') as f:

    # Open Csound synthesizer
    f.write('<CsoundSynthesizer>\n\n')

    # Decide on Options
    f.write('<CsOptions>\n')
    f.write('; Select flags here\n')
    f.write('; realtime audio out\n')
    f.write('-o dac \n')
    f.write('</CsOptions>\n')

    # Start creating CsInstruments
    f.write('<CsInstruments>\n\n')
    f.write('sr = 44100\n')
    f.write('kr = 4410\n')
    f.write('ksmps = 10\n')
    f.write('nchnls = 2\n\n')

    f.write('gasrc init 0\n\n')

    f.write('instr 1		;a sine wave\n\n')

    f.write('  kamp = p4\n')
    f.write('  kcps = p5\n')
    #f.write('  icps = 442\n')
    f.write('  ifn = 1\n\n')
#    f.write('  a1 pluck kamp, kcps, icps, 0, 1\n\n')
    f.write('  a1 oscil kamp, kcps, ifn\n\n')
    f.write('  gasrc = a1\n\n')
    f.write('endin\n\n')

    f.write('instr 10	;uses output from instr1 as source\n\n')
    f.write('  kaz	linseg 720, p3, 0		;2 full rotations\n\n')
    f.write('  kel	linseg 10, p3, 0		;falling down through space\n\n')
    f.write('  aleft,aright hrtfmove2 gasrc, kaz, kel, "hrtf-44100-left.dat","hrtf-44100-right.dat"\n\n')
    f.write('  outs	aleft, aright\n\n')
    f.write('endin\n\n')

    f.write('</CsInstruments>\n')
    f.write('<CsScore>\n\n')
    f.write(';wavetable\n')
    f.write('f1 0 16384 10 1\n')
    f.write('; Play Instrument 1: a simple arpeggio\n')
    f.write('i1 0 .2 15000 440.00 \n')
    f.write('i1 + .2 15000 466.16 \n')
    f.write('i1 + .2 15000 493.88 \n')
    f.write('i1 + .2 15000 523.25 \n')
    f.write('i1 + .2 15000 587.33 \n')
    f.write('i1 + 1.5 15000 659.25 \n')
    f.write('i1 + 1.5 15000 698.46 \n')
    f.write('i1 + 1.5 15000 783.99 \n')
    f.write('i1 + 1.5 15000 880.00 \n')
    f.write('i1 + 1.5 15000 830.61 \n')
    f.write('i1 + 1.5 15000 783.99 \n\n')

    f.write('; Play Instrument 10 for 10 seconds.\n')
    f.write('i10 0 10\n\n')

    f.write('</CsScore>\n')
    f.write('</CsoundSynthesizer>')

# Play Play Csound file
#Csoundfile = "cSoundBook\\ambisonicsBinaural\\hrtfmove2_example_44100.csd"
ret = cs.compile_("csound", outCsndFile)
if ret == ctcsound.CSOUND_SUCCESS:
    cs.perform()
    cs.reset()
