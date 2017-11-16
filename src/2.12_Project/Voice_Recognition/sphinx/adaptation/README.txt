https://cmusphinx.github.io/wiki/tutorialadapt/
https://sourceforge.net/p/cmusphinx/discussion/help/thread/49e34dff/
./bw \
 -hmmdir en-us \
 -moddeffn en-us/mdef.txt \
 -feat 1s_c_d_dd \
 -ts2cbfn .cont. \
 -cmn current \
 -agc none \
 -dictfn cmudict-en-us.dict \
 -ctlfn arctic20.fileids \
 -lsnfn arctic20.transcription \
 -accumdir .

 in en-us