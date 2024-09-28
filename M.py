import random
import telegram
from telegram.ext import Updater, CommandHandler

# Replace with your actual bot token
TOKEN = "YOUR_BOT_TOKEN"

# Lists for generating movie information
adjectives = ["The", "Epic", "Action", "Dark", "Funny", "Strange", "Scary", "Romantic", "Magical", "Mysterious"]
nouns = ["Adventures", "Journey", "Quest", "Escape", "Battle", "Story", "Secret", "Love", "Time", "Future"]
plots = [
    "A group of friends embark on a dangerous quest to find a lost treasure.",
    "A young hero must overcome their fears to save the world from an evil villain.",
    "Two lovers from different worlds must find a way to be together.",
    "A scientist's experiment goes wrong, creating a monster that threatens humanity.",
    "A time traveler goes back in time to prevent a tragedy.",
]
actors = ["Tom Hanks", "Jennifer Lawrence", "Leonardo DiCaprio", "Scarlett Johansson", "Chris Pratt", "Meryl Streep", "Robert Downey Jr.", "Margot Robbie", "Dwayne Johnson", "Will Smith"]
genres = ["Action", "Adventure", "Comedy", "Drama", "Fantasy", "Horror", "Romance", "Sci-Fi", "Thriller"]


def generate_movie_title():
  """Generates a random movie title."""
  adjective = random.choice(adjectives)
  noun = random.choice(nouns)
  title = f"{adjective} {noun}"
  return title

def generate_movie_plot():
  """Generates a random movie plot."""
  plot = random.choice(plots)
  return plot

def generate_movie_cast():
  """Generates a random movie cast."""
  cast = random.sample(actors, random.randint(3, 7))
  return cast

def generate_movie_genre():
  """Generates a random movie genre."""
  genre = random.choice(genres)
  return genre

def generate_movie_poster(update, context):
  """Generates and sends a movie poster to the user."""
  title = generate_movie_title()
  genre = generate_movie_genre()
  cast = ", ".join(generate_movie_cast())

  poster = f"""
     ______                                      
    / ____/___  _________  ____  ____  ____  ____  
   / /   / __ / ___/ __ / __ / __ / __ / __  
  / /___/ /_/ / /  / /_/ / /_/ / /_/ / /_/ / /_/ / 
 /_____/____/_/   ____/____/ .___/____/____/  
                       /_/                   
  
  {title} ({genre})
  Starring: {cast}
  
  Coming Soon!
  """
  context.bot.send_message(chat_id=update.effective_chat.id, text=poster)

def main():
  """Starts the Telegram bot."""
  updater = Updater(TOKEN, use_context=True)
  dispatcher = updater.dispatcher

  dispatcher.add_handler(CommandHandler("movie", generate_movie_poster))

  updater.start_polling()
  updater.idle()

if __name__ == "__main__":
  main()
