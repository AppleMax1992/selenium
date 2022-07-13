"""
URL管理
"""


class UrlManager(object):
	def __init__(self):
		"""初始化已爬取URL集合、未爬取URL集合"""
		self.new_urls = set()
		self.old_urls = set()

	def add_new_url(self, url):
		"""添加未爬取URL"""
		if url is None:
			return
		if (url not in self.new_urls) and (url not in self.old_urls):
			self.new_urls.add(url)

	def add_new_urls(self, urls):
		"""批量添加未爬取URL"""
		if (urls is None) or (len(urls) == 0):
			return
		for url in urls:
			self.add_new_url(url)

	def get_new_url(self):
		"""取出未爬取URL并添加至已爬取URL集合"""
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url

	def has_new_url(self):
		"""确认是否还有未爬取URL"""
		return len(self.new_urls) != 0