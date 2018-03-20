<CsoundSynthesizer>

<CsOptions>
; Select flags here
; realtime audio out
-o dac 
</CsOptions>
<CsInstruments>

sr = 44100
kr = 4410
ksmps = 10
nchnls = 2

gasrc init 0

instr 1		;a sine wave

  kamp = p4
  kcps = p5
  ifn = 1

  a1 oscil kamp, kcps, ifn

  gasrc = a1

endin

instr 10	;uses output from instr1 as source

  kaz	linseg 720, p3, 0		;2 full rotations

  kel	linseg 10, p3, 0		;falling down through space

  aleft,aright hrtfmove2 gasrc, kaz, kel, "hrtf-44100-left.dat","hrtf-44100-right.dat"

  outs	aleft, aright

endin

</CsInstruments>
<CsScore>

;wavetable
f1 0 16384 10 1
; Play Instrument 1: a simple arpeggio
i1 0 .2 15000 440.00 
i1 + .2 15000 466.16 
i1 + .2 15000 493.88 
i1 + .2 15000 523.25 
i1 + .2 15000 587.33 
i1 + 1.5 15000 659.25 
i1 + 1.5 15000 698.46 
i1 + 1.5 15000 783.99 
i1 + 1.5 15000 880.00 
i1 + 1.5 15000 830.61 
i1 + 1.5 15000 783.99 

; Play Instrument 10 for 10 seconds.
i10 0 10

</CsScore>
</CsoundSynthesizer>