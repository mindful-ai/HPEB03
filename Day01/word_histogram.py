text = '''
Look at the stars
Look how they shine for you
And everything you do
Yeah they were all yellow
I came along
I wrote a song for you
And all the things you do
And it was called "Yellow"
So then I took my turn
Oh what a thing to have done
And it was all yellow
Your skin
Oh yeah, your skin and bones
Turn into something beautiful
You know, you know I love you so
You know I love you so
I swam across
I jumped across for you
Oh what a thing to do
'Cause you were all yellow
I drew a line
I drew a line for you
Oh what a thing to do
And it was all yellow
Your skin
Oh yeah your skin and bones
Turn into something beautiful
And you know
For you I'd bleed myself dry
For you I'd bleed myself dry
It's true
Look how they shine for you
Look how they shine for you
Look how they shine for
Look how they shine for you
Look how they shine for you
Look how they shine
Look at the stars
Look how they shine for you
And all the things that you do

'''


words = text.split()

uwords = set(words)

print(words)
print('\n\n')


print(uwords)

D = {}
for uword in uwords:
    #print(uword + ' ---------> ' + str(words.count(uword)))
    D.setdefault(uword, words.count(uword))

print('\n\n')


print(D)
