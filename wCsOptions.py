def writeCsOptions(f):
    f.write('<CsOptions>\n')
    f.write('; Select flags here\n')
    f.write('; realtime audio out\n')
    f.write('-o dac \n')
    f.write('</CsOptions>\n')
