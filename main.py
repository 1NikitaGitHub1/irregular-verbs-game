import pandas
import random

from encouragements import encouragements

def random_encouragement():
  print(random.choice(encouragements))

def remove_all_by_value(d, value):
    keys_to_remove = [key for key, val in d.items() if val == value]
    for key in keys_to_remove:
        del d[key]
    return d

def run(df):
  print("NOTE: if words can be two words seperete by ,")
  while True:
    print()
    # consts
    ALL_TIMES = list(df.columns)
    # random test request
    lengh = len(df)
    current_random = random.randint(0, lengh - 1)
    random_time = random.choice(list(ALL_TIMES))
    # some data to player requests
    word = df.loc[current_random, random_time]
    # for cycle requests
    last_times_and_words = dict()
    for time in ALL_TIMES:
      last_times_and_words[time] =  df.loc[current_random, time]
    del last_times_and_words[random_time]
    # player request  
    while last_times_and_words:
      print() 
      correct_words = list(df.loc[current_random, last_times_and_words.keys()])
      print(f"In {random_time} time. Word(s) - ({word})")
      answer = str(input(f"Enter word in this(ese) time(s) {last_times_and_words.keys()} only one word(s) in the time ")) 
      print()

      if answer.lower() in correct_words:
        # input answer, last_times 
        last_times_and_words = remove_all_by_value(last_times_and_words, answer)               
        random_encouragement()
      else:
        print("Incorrect")
        print(f"Maybe you mean {correct_words}. Try again")
    print()
    random_encouragement()
def main():
  df = pandas.read_csv("C:\\Programming\\Educations\\irregular verbs game\\irregular-verbs-de.csv", header=None, usecols=[0, 1, 2])
  df.columns = ["Present", "Past", "Perfect"]
  run(df)

if __name__ == "__main__":
  main()