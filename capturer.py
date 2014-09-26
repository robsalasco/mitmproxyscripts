import os,re

def request(context, flow):
  if(re.search(".*--.*\\.googlevideo\\.com", flow.request.host)):
        url="%s%s" % (flow.request.host, flow.request.path)
        os.system("echo \"https://%s\"|pbcopy" % url)
