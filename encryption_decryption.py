import binascii

def RSA_EncInt(plainint, public_key):
	e, n = public_key
	if plainint < n:
		return pow(plainint, e, n)
	else:
		return None

def RSA_DecInt(cypherint, private_key):
	d, n = private_key
	return pow(cypherint, d, n)

def RSA_EncStr(plainstr, size, public_key):
	e, n = public_key
	hex_str = binascii.hexlify(plainstr.encode())
	decoded_hex = hex_str.decode()
	split_str = [decoded_hex[i:i+int(size/4)] for i in range(0, len(decoded_hex), int(size/4))]
	encoded_list = []
	for i in range(0, len(split_str)):
	    encoded_list.append(RSA_EncInt(int(split_str[i].encode(), 16), public_key))
	return encoded_list

def RSA_DecStr(cyphintlst, private_key):
	d, n = private_key
	decyphered_list = []
	for i in range(0, len(cyphintlst)):
	    decyphered_list.append(binascii.unhexlify(hex(RSA_DecInt(cyphintlst[i], private_key))[2:]).decode())
	return "".join(decyphered_list)