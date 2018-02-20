import mechanize

br = mechanize.Browser()
response = br.open("https://www.timetablegenerator.io/")
#print(response.read())      # the text of the page
response1 = br.response()  # get the response again
#print(response1.read())     # can apply lxml.html.fromstring()

#print("Headers:", response.info()) # headers

for form in br.forms():
    print("Form name:", form.name)
    #print(form)
    br.select_form(form.name) # form selection
    #br.form['university_selector'] = 'mcmaster'
    #br.submit(id='course_add_button')
    print("End of form\n")

print("Finished")


