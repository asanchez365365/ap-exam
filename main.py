#AaronSanchez
#Playlist Organizer  
# List of songs, function to filter by genre or mood.

songs = []
answers = []

def choose_song(question):

    song = input("Do you want to hear a song? ")
    if song == "no":
        print("Okay, you're missing out!")

    while song == "yes":
        print("Amazing, lets listen!")
    question = input("Do you want to hear a song that is joyful, sadness, nostalgic, or calm? ")
    joke = choose_song(question)

    if question == "sadness":
        input("Are you feeling sadness?")
        input("Heres a sad song for ya!")

    if question == "joyful":
        input("Are you feeling joyful?")
        input("Heres a joyful for ya!")

    if question == "nostalgia":
        input("Are you feeling nostalgia?")
        input("Heres a nostalgic song for ya!")

    if question == "calm":
        input("Are you feeling calm?")
        input("Heres a calm song for ya!")


        answers.append(question)
        return input(" Do you want to listen to another song or are you finished?")
    
def countdown(sec):
        import time
        for i in range(sec, 0, -1):
            print(i)
            time.sleep(1)

        countdown(3)
        print("Playing song now...")