def wInstrumentForematter(f,sr,ksmps,nchnls):
    """ Write forematter into file f
        sr - audio sample rate
        kr - contro rate
        ksmps = sr/kr
        nchnls - number of channels
    """
    f.write('sr = '+str(sr)+'\n')
    #f.write('kr = '+str(sr/ksmps)+'\n')
    f.write('ksmps = '+str(ksmps)+'\n')
    f.write('nchnls = '+str(nchnls)+'\n\n')

def sinInstr(f,n, kamp, iMidi, ifn, dur):
    """ Write an instrument, number n, that
    - outputs a sine wave
    - has amplitude kamp
    - has iMidi midi input number
    - is drawn from frequency table ifn
    """
    rampUp = 0.003
    coolDown = 0.007
    sum = rampUp + coolDown
    #initialize time exp. variables
    #f.write('gasrc'+str(n)+' init 0\n\n')
    # Make instr
    f.write('instr '+str(n)+'  \n\n')
    f.write('inote = '+str(iMidi)+'\n\n')
    #f.write('kcps =')
    f.write('  kamp = '+str(kamp)+'\n')
    f.write('  kcps = cpsmidinn(inote)\n')
    f.write('  ifn = '+str(ifn)+'\n\n')
    f.write('  a1 poscil kamp, kcps, ifn\n\n')
    f.write('  adeclick linseg 0, '+str(rampUp)+", ")
    f.write(   '1, '+str(dur)+' - '+str(sum)+", ")
    f.write(   '1, '+str(coolDown)+", 0\n")
    f.write('  a1 = a1 * adeclick\n')
    f.write('  chnmix a1, "buss"\n\n')
    f.write('endin\n\n')

def hrtfMove2ExInstr(f,n,sAz,eAz,durAz,sEl,eEl,durEl,sr,overlaps,headRadius): #4, 8.15
    instrNum = n*(10**1)
    f.write('instr '+str(instrNum)+'\n\n')
    f.write('  kaz	linseg '+str(sAz)+', '+str(durAz)+', '+str(eAz)+'\n')
    f.write('  kel	linseg '+str(sEl)+', '+str(durEl)+', '+str(eEl)+'\n\n')
    f.write('  abuss chnget "buss"\n')
    f.write('  aleft, aright hrtfmove2 abuss, kaz, kel, "hrtf-'
            +str(sr)+'-left.dat", "hrtf-'+str(sr)+'-right.dat", '+str(overlaps)
            +', '+str(headRadius)+', '+str(sr)+'\n\n')
    f.write('  outs	aleft, aright\n')
    f.write('  chnclear "buss"\n\n')
    f.write('endin\n\n')
