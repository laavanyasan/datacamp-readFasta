def read_fasta(filename):
    sequence = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line:
            # Append to the last sequence
            sequence = sequence + line
    f.close()
    return sequence

<<<<<<< HEAD
print(read_fasta('ae.fa'))
=======
print(read_fasta(sys.argv[1]))
>>>>>>> parent of 75a514b... There is adding an arguement to check for whether there is a file name added or not.
