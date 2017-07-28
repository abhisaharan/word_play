fin = open("words.txt", "r")
ctr = 0
w_ctr = 0
for line in fin :
    word = line.strip()
    w_ctr += 1
    if not ( 'e' in word or 'E' in word ) :
#        print "%s does not contain the letter 'e'" % word  # This takes too long, but is useful for debugging
        ctr += 1
