def prin(*arg):
	print(f'\n\n{arg}\n\n')


def resp_fun(msg, lod_link, alert_type):
	if alert_type == 'success':
		title = 'Success'
	else:
		title = 'Please notice !'
	return {'title': title, 'msg': msg, 'lod_link': lod_link, 'alert_type': alert_type}
