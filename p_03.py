import vlc

import pafy

url = "https://www.youtube.com/watch?v=u2NAuswnTKs"

video = pafy.new(url)
  
best = video.getbest()
  
media = vlc.MediaPlayer(best.url)
  
media.play()