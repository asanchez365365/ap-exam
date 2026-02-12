#AaronSanchez
#Playlist Organizer  
# List of songs, function to filter by genre or mood.

playlist = []
# this list stores songs as dictionaries (song name +genre/mood)

def show_playlist(song_list, chosen_category):

    found= False # checks and makes sure if a matching song exists
    

    for song in song_list: 
        # this is iteration that goes through each song
        name = song["name"]
        category = song["category"]

        if category.lower() == chosen_category.lower():
            # checking if categroy matches using selection
            print("Song:", name)
            print("Genre/Mood", category)
            print()
            found=True

    if found == False:
        print("No songs found")
        # This is just in case no songs are found

print ("Welcome to your Playlist Organizer!")

while True:

    print()
    print("1 Add a song")
    print("2 View songs by genre or mood")
    print("3 Exit")

    choice= input("Choose option: ")

    #to add a song...

    if choice == "1":
        song_name = input("Please enter song name :")
        song_category = input ("Enter genre or mood")

        song_data = {
            "name": song_name,
            "category": song_category
        }

        playlist.append(song_data)
        print("Song added.")

    #now we shall view the songs
    elif choice == "2":
        if len(playlist) == 0:
            print("Playlist is empty")
        else:
            search = input("Enter genre or mood:")
            show_playlist(playlist, search)

    elif choice == "3":
        print("Goodbye for now.")
        break

    else:
        print("Invalid choice")