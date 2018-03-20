def wInstrumentForematter(f,sr,kr,nchnls):
    f.write('sr = '+str(sr)+'\n')
    f.write('kr = '+str(kr)+'\n')
    f.write('ksmps = '+str(sr/kr)+'\n')
    f.write('nchnls = '+str(nchnls)+'\n\n')
