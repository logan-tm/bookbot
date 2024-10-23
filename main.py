def main(title):
  with open(title) as f:
    print(f"--- Begin report of {title} ---")
    file_contents = f.read()
  print(f"{len(file_contents.split())} words found in the document\n")
  character_counts = {}
  for char in file_contents:
    if char.isalpha():
      char = char.lower()
      if char in character_counts:
        character_counts[char] += 1
      else:
        character_counts[char] = 1

  sorted_chars = dict(sorted(character_counts.items(), key=lambda item: item[1], reverse=True))
  for char, count in sorted_chars.items():
    print(f"The '{char}' character was found {count} times")
  print("--- End report ---")
main("books/frankenstein.txt")