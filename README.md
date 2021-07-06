# NTLM hash depersonificator

Turns this: \
`u4-netntlm::kNS:338d08f8e26de93300000000000000000000000000000000:9526fb8c23a90751cdd619b6cea564742e1e4bf33006ba41` \
Into something like this: \
`u4-netntlm::kNS:338d08f8*****300000000000000000000000000000000:9526fb8c23a90751cdd619*****e1e4bf33006ba41` \
\
Uses `hashes.txt` as input and `result.txt` as output