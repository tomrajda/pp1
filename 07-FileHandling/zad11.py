# 11.	An array film_titles contains any five film titles. Write a program 
# that writes the film titles to a text file, each title on a separate line.

film_titles = ["Harry Potter", "Lord of the Rings", "The Witcher", "Wednesday",
                "Poranek Kojota"]

file = open("films.txt", "w")

for film in film_titles:
    file.writelines(film + "\n")

file.close()