import sys
def request_handler(all_socket_dictionary):
	print all_socket_dictionary
	if all_socket_dictionary['method'] == 'POST':
		
		request_data = all_socket_dictionary['request_data'].split('&')
		N1 = request_data[0].split('=')
		N2 = request_data[1].split('=')
		summ = float(N1[1]) + float(N2[1])
		summ_str = str(summ)
		all_socket_dictionary['body'] = "<html><body><h1>Summ=%s</h1></body></html>" % summ_str	 
	elif all_socket_dictionary['method'] == 'GET':
		print all_socket_dictionary['url']
		request_data_split = socket_dictionary['url'].split('?')
		request_data = request_data_split[1].split('&')
		
		N1 = request_data[0].split('=')
		N2 = request_data[1].split('=')
		summ = float(N1[1]) + float(N2[1])
		summ_str = str(summ)
		all_socket_dictionary['body'] = "<html><body><h1>Summ=%s</h1></body></html>" % summ_str	 
		
	return all_socket_dictionary['body']
