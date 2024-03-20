#help_settings= <get the help settings for your software>

#full_dict = <get the complete dict / help container, inlclude flagged API files or so>
# Any keyerror should exit the release script, so not catching the error here.
f1 = open('help_all_container1.txt','w')

for first_dict in full_dict['cont1']:
	first_name = first_dict['name']
	f1.write("\nCONTAINER:\n"+cont1_name +"\n\n" "ELEMENTS:\n\n")
	for end_cont_dict in first_dict['elements']:
		help_text = gp.HelpInfoToTextConverter.convert_element_help(element_dict)
		f1.write(">>  ")
		f1.write(help_text +"\n")
f1.close()


f2 = open('help_all_class.txt','w')
for cls_dict in full_dict['classes']:
#    	writer.add_document(title_=convert_to_unicode(cls_dict['name']), class_name_=convert_to_unicode(cls_dict['name']), content_=convert_to_unicode(cls_dict['brief']))
	class_name= cls_dict['name']
	f2.write("\nCLASS:\n"+class_name +"\n"+cls_dict['brief']+ "\n\n" + "SEE ALSO:\n")
	try:
		for i in cls_dict['see_also']:
			f2.write(i + "\n")
	except:
		pass	
	try:
		f2.write("\n\nDETAILS:\n")
		f2.write(cls_dict['details']+"\n")
	except:
		pass	
	

	f2.write("\n\nELEMENTS:\n\n")
 
	for element_dict in cls_dict['elements']:
		help_text = gp.HelpInfoToTextConverter.convert_element_help(element_dict)
		f2.write(">>  ")
		f2.write(help_text +"\n")
f2.close()

#        element_name = element_dict['real_name'] if 'real_name' in element_dict else element_dict['name']
