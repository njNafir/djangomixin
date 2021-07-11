from django.utils.http import is_safe_url

"""
class mixin stands for django class based view mixin.
It's can be inherited in your view defination to extend functionality.
"""

class RequestAttachMixin(object):
	"""
		Mixin to attach session request object to your class view
	"""
	def get_form_kwargs(self):
		kwargs = super(RequestAttachMixin, self).get_form_kwargs()
		kwargs['request'] = self.request
		return kwargs


class NextUrlMixin(object):
	"""
		Mixin to attach method for ?next=anything to your class view
		Retrive the next url by calling into get_next_url method
	"""
	default_path = '/'
	def get_next_url(self):
		request = self.request
		next_page 		= request.GET.get('next')
		next_post 		= request.POST.get('next')
		redirect_path 	= next_page or next_post or None
		if is_safe_url(redirect_path, request.get_host()):
			return redirect_path
		else:
			return self.default_path
