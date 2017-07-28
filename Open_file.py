fin = open("words.txt", "r")
ctr = 0
w_ctr = 0
for line in fin :
    word = line.strip()
    w_ctr += 1
    if not ( 'e' in word or 'E' in word ) :
#        print "%s does not contain the letter 'e'" % word  # This takes too long, but is useful for debugging
        ctr += 1
print ("There are {} words that do not contain the letter 'e' out of {} words".format(ctr, w_ctr))
print ("That is {}.2f%%".format(( 100.0 * float(ctr)/float(w_ctr) ),))
fin.close()