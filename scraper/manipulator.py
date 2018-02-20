import mechanize

br = mechanize.Browser()
br.set_all_readonly(False)    # allow everything to be written to
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this
#br.addheaders = 	      	# [('User-agent', 'Firefox')]

response = br.open("https://applicants.mcmaster.ca/psp/prepprd/EMPLOYEE/PSFT_LS/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL")
print(response.read())      # the text of the page
response1 = br.response()  # get the response again
print(response1.read())     # can apply lxml.html.fromstring()

for form in br.forms():
    print("Form name:", form.name)
    print(form)
