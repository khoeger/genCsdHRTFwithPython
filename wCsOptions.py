def writeCsOptions(f, realtime=True,savePath = ""):
    f.write('<CsOptions>\n')
    f.write('; Select flags here\n')
    if realtime == True:
        f.write('; realtime audio out\n')
        f.write('-o dac \n')
    if savePath != "":
        f.write('; For Non-realtime ouput leave only the line below:\n')
        f.write(' -o '+savePath+'\n')

    f.write('</CsOptions>\n')
