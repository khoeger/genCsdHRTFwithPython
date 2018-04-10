def writeCsOptions(f, realtime=True,savePath = ""):
    f.write('<CsOptions>\n')
    f.write('; Select flags here\n')
    if realtime == True:
        f.write('; realtime audio out\n')
        f.write('-o dac \n')# -o dac: Write sound to the host audio output device
        f.write('-m35\n')   # -m35 =? -m 35 = -m 1+2+32 = note applitude message, samples out of range message, & no colors
        f.write('-d\n')     # -d: surpresses displays
    if savePath != "":
        f.write('; For Non-realtime ouput leave only the line below:\n')
        f.write(' -o '+savePath+'\n')

    f.write('</CsOptions>\n')
