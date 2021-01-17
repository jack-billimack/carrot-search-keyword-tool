import requests

def keyword_request(keyword_input):
	url = "https://search.carrot2.org/#/search/web/{0}/folders".format(keyword_input)
	r = requests.get(url)
	return r.text

if __name__ == "__main__":
	print(keyword_request(input("ENTER YOUR KEYWORD TO RESEARCH HERE \n")))
