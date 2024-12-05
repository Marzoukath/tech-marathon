import filecmp
print ("IDENTIQUE:", "oui" if filecmp.cmp("output.txt", "out.official.txt", shallow=False) else "non")
