Csound's [hrtfmove2](http://www.csounds.com/manual/html/hrtfmove2.html) opcode(?) allows one to create binaural 3d effects.

The initial code inside
- takes a modified version of hrtfmove2's example csound file  (modified instruments and score)
- generates it in python
- runs it in python

The goal is to make it easier to generate a new score from python inputs.

## Files that aren't mine
**hrtf-44100-right.dat** and **hrtf-44100-left.dat** are not my files.
I downloaded them from part of the
[Csound github](https://github.com/csound/csound/tree/720e99cd2ba1e30402db845d2d4251ec318c9dc3/samples).
They are necessary for creating binaural 3d sound files.

## Useful information for 3d audio endeavors
- [csound tutorial: panning and spatialization](http://files.csound-tutorial.net/floss_manual/Release03/Cs_FM_03_ScrapBook/b-panning-and-spatialization.html) This describes lots of what I'd like to know about the topic
- [Doppler Effect and Binaural Math](https://diamonddissertation.blogspot.com)

# About the scale refs
[Eq Tempered Scale Doc](http://pages.mtu.edu/~suits/notefreqs.html)
