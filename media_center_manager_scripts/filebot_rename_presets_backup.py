

# https://www.filebot.net/naming.html

{ if (f.subtitle) '(' + fn.match(/_(\d+)$/) + ')' }

# post_filebot_movies/{n.colon(' - ')} ({y}){' CD'+pi} [{vf}]{subt}/{n.colon(' - ')} ({y}){' CD'+pi} [{vf}]{subt}
# post_filebot_movies/{n.colon(' - ')} ({y}){' CD'+pi} [{vf}]/{n.colon(' - ')} ({y}){' CD'+pi} [{vf}]{subt}
# post_filebot_movies/{n.colon(' - ')} ({y}){' CD'+pi} [{vf}]/{n.colon(' - ')} ({y}){' CD'+pi} [{vf}]{[source]}{subt}{ if (f.subtitle) '(' + fn.match(/_(\d+)$/) + ')' }
post_filebot_movies/{n.colon(' - ')} ({y}){' CD'+pi} [{vf}]{subt}/{n.colon(' - ')} ({y}){' CD'+pi} [{vf}]{ if (f.subtitle) '(' + fn.match(/_(\d+)$/) + ')' }{subt}