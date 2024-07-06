# Write code below 💖
liked_songs = {
  'Master P':'Kaytramine',
  'Witchy': 'Childish Gambino',
  'Navajo': 'Masego',
  'Girl':'The Internet',
  'Them Changes':'Thundercat',
  'NxWorries': 'Suede',
  'Sir': 'Devils',
  'Believe It': 'PartyNextDoor',
  'I Like That': 'Janelle Monae'
}

def write_liked_songs_to_file(songs, file_name):
  with open(file_name, 'w') as file:
    file.write('Liked Songs:\n')
    for song, artist in songs.items():
      file.write(f' {song} by {artist}\n')

# Call the function to write liked songs to 'liked_songs.txt'
write_liked_songs_to_file(liked_songs, 'liked_songs.txt')
