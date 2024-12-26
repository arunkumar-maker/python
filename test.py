import demo
print("In test file")
print(__name__)

'''
When we import the demo module, if there is no name condition written in the demo file
then just because of importing that file as module, we see the print statements getting executed
when we run this test file.

To restrict that we have to tell in the demo file explicitly that you run this main code only if you are getting run by the developer. But
if you are imported in another file, you should not execute the print statements.
'''
