# https://github.com/devilking15292/IMDB_Api_python
# https://rapidapi.com/blog/how-to-use-imdb-api/

from IMDBAPI import IMDB

imdb = IMDB()
# 
# # print(getRuntime('darknight rises'))
print("Movie rated: "+imdb.getRating('darknight rises')+" out of 10")
# 
m = imdb.getMovie('The Dark Knight Rises')
# 
# print(m.title)
# # print(m.runTime)
print(m.titleYear)