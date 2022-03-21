forth_line = ["","suck her thumb","tie her shoe","climb a tree","shut the door",
                "take a dive","pick up sticks","pray to heaven",
                "check the gate","check the time",'say “The End!”']
def sing_verse(verse_num):
    print(f"the ants go matching {verse_num} by {verse_num} hurrah hurrah")
    print(f"the ants go matching {verse_num} by {verse_num} hurrah hurrah")
    print(f"the ants go matching {verse_num} by {verse_num}")
    print(f"the little one stops to {forth_line[verse_num]}")
    print("""and they all go martching down
to the ground
to get out of the rain
BOOM BOOM BOOM
    """)
def main():
    for verse in range(1,11):
        sing_verse(verse)
main()
