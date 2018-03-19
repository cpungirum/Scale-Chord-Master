# Change code to a functional paradigm
from time import sleep

# The dictionary key is the musical note that defines the major scale
major_scales = {"C": ["C", "D", "E", "F", "G", "A", "B"],
                "C#": ["C#", "Eb", "F", "F#", "Ab", "Bb", "C"],
                "D": ["D", "E", "F#", "G", "A", "B", "C#"],
                "Eb": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
                "D#": ["D#", "F", "G", "Ab", "Bb", "C", "D"],
                "E": ["E", "F#", "Ab", "A", "B", "C#", "Eb"],
                "F": ["F", "G", "A", "Bb", "C", "D", "E"],
                "F#": ["F#", "Ab", "Bb", "B", "C#", "Eb", "F"],
                "G": ["G", "A", "B", "C", "D", "E", "F#"],
                "Ab": ["Ab", "Bb", "C", "C#", "Eb", "F", "G"],
                "G#": ["G#", "Bb", "C", "C#", "Eb", "F", "G"],
                "A": ["A", "B", "C#", "D", "E", "F#", "Ab"],
                "Bb": ["Bb", "C", "D", "Eb", "F", "G", "A"],
                "A#": ["A#", "C", "D", "Eb", "F", "G", "A"],
                "B": ["B", "C#", "Eb", "E", "F#", "Ab", "Bb"]}

# The dictionary key is the musical note that defines the minor scale
minor_scales = {"A": ["A", "B", "C", "D", "E", "F", "G"],
                "Bb": ["Bb", "C", "C#", "Eb", "F", "F#", "Ab"],
                "A#": ["A#", "C", "C#", "D#", "F", "F#", "G#"],
                "B": ["B", "C#", "D", "E", "F#", "G", "A"],
                "C": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],
                "C#": ["C#", "Eb", "E", "F#", "Ab", "A", "B"],
                "D": ["D", "E", "F", "G", "A", "Bb", "C"],
                "Eb": ["Eb", "F", "F#", "Ab", "Bb", "B", "C#"],
                "D#": ["D#", "F", "F#", "G#", "A#", "B", "C#"],
                "E": ["E", "F#", "G", "A", "B", "C", "D"],
                "F": ["F", "G", "Ab", "Bb", "C", "C#", "Eb"],
                "F#": ["F#", "Ab", "A", "B", "C#", "D", "E"],
                "G": ["G", "A", "Bb", "C", "D", "Eb", "F"],
                "Ab": ["Ab", "Bb", "B", "C#", "Eb", "E", "F#"],
                "G#": ["G#", "A#", "B", "C#", "D#", "E", "F#"]}


def quit():  # It shadows the built-in function but includes a delayed message
    print("Quitting...")
    sleep(2)
    exit()


def check_note(note1):  # Validates input from user.
    if note1 in "QUIT":
        quit()
    elif note1 not in major_scales and (len(note1) > 1 and note1[1] == "B"):
        note_list = list(note1)
        note_list[1] = "b"
        note1 = "".join(note_list)
    elif note1 not in major_scales:
        print(f"{note1} is not a valid key!")
        quit()
    return note1


def is_minor(m):  # It checks second input from user to determine whether note is minor
    if m in "YES":
        return True
    elif m in "NO":
        return False
    elif m in "QUIT":
        quit()


def get_scale():  # It returns a minor or major scale, depending on the user's choice
    if minor:
        minor_scale = minor_scales[note]
        print(f"\nThe minor scale based on key of {note} is: \n\033[34m{minor_scale}\033[m")
        return minor_scale
    elif not minor:
        major_scale = major_scales[note]
        print(f"\nThe major scale based on key of {note} is: \n\033[34m{major_scale}\033[m")
        return major_scale


def get_chords():  # It prints the appropriate chords that go with the scale
    if minor:
        print(f"\nThe main chords available to play a song in {note} minor are: ")
        for scale_note in scale:
            if scale_note == scale[0] or scale_note == scale[3] or scale_note == scale[4]:
                scale_note += "m"
            elif scale_note == scale[1]:
                scale_note += "dim"
            print(f"\033[31m{scale_note}", end="  ")
    elif not minor:
        print(f"\nThe main chords available to play a song in {note} major are: ")
        for scale_note in scale:
            if scale_note == scale[1] or scale_note == scale[2] or scale_note == scale[5]:
                scale_note += "m"
            elif scale_note == scale[6]:
                scale_note += "dim"
            print(f"\033[31m{scale_note}", end="  ")


note = check_note(str(input("\nPlease type the key you want to see a scale of: ")).strip().upper())
minor = is_minor(str(input("Do you want a natural minor scale? [Yes] or [No]")).strip().upper())
scale = get_scale()
get_chords()









