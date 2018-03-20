def wInstrumentForematter(f,sr,kr,nchnls):
    """ Write forematter into file f
        sr - audio sample rate
        kr - contro rate
        nchnls - number of channels
    """
    f.write('sr = '+str(sr)+'\n')
    f.write('kr = '+str(kr)+'\n')
    f.write('ksmps = '+str(sr/kr)+'\n')
    f.write('nchnls = '+str(nchnls)+'\n\n')

def sinInstr(f,n, kamp, kcps, ifn):
    """ Write an instrument, number n, that
    - outputs a sine wave
    - has amplitude kamp
    - has kcps cycles per second
    - is drawn from frequency table ifn
    """
    #initialize time exp. variables
    f.write('gasrc'+str(n)+' init 0\n\n')
    # Make instr
    f.write('instr '+str(n)+'  \n\n')
    f.write('  kamp = '+str(kamp)+'\n')
    f.write('  kcps = '+str(kcps)+'\n')
    f.write('  ifn = '+str(ifn)+'\n\n')
    f.write('  a1 oscil kamp, kcps, ifn\n\n')
    f.write('  gasrc'+str(n)+' = a1\n\n')
    f.write('endin\n\n')

def hrtfMove2ExInstr(f,n,sAz,eAz,durAz,sEl,eEl,durEl):
    instrNum = n*(10**1)
    f.write('instr '+str(instrNum)+'\n\n')
    f.write('  kaz	linseg '+str(sAz)+', '+str(durAz)+', '+str(eAz)+'\n')
    f.write('  kel	linseg '+str(sEl)+', '+str(durEl)+', '+str(eEl)+'\n\n')
    f.write('  aleft, aright hrtfmove2 gasrc'+str(n)+', kaz, kel, "hrtf-44100-left.dat","hrtf-44100-right.dat"\n\n')
    f.write('  outs	aleft, aright\n\n')
    f.write('endin\n\n')
